"""Engine: FindErrors, FindMismatchs - applies rules to LaTeX text."""
import re
from .tokenizer import (
    tokenize,
    tokens_to_user,
    num_newlines,
    START_MATH_CHAR,
    END_MATH_CHAR,
)
from .report import report_error


def _max(a: int, b: int) -> int:
    return a if a > b else b


def _bracket_count(regex_str: str) -> int:
    """Count capturing groups (open parens not in char class)."""
    bracket_re = re.compile(r"(?<!\[)\((?!\?)")
    return len(bracket_re.findall(regex_str))


def find_mismatchs(out_files: list, text: str, filename: str, output_format: str) -> None:
    """Report style mismatches (e.g. formulae vs formulas)."""
    eitheror = [
        ["", r"[Ff]ormulas", r"(?<![\\\\])[Ff]ormulae"],
        ["", r"[Ll]emmas", r"(?<![\\\\])[Ll]emmata"],
        ["Case Mismatch", r"(?<![.]\s)(Lemma|Corollary)\s+.ref", r"(lemma|corollary)\s+.ref"],
        ["", r"[Cc]olour", r"(?<![\\\\])[Cc]olor"],
        ["", r"axiomatisation", r"axiomatization"],
        ["Case Mismatch[2]", r"(?<![.]\s)Theorem\s+.ref", r"theorem\s+.ref"],
    ]
    for row in eitheror:
        rule_type = row[0] or "Style Mismatch"
        prior = ""
        for i in range(1, len(row)):
            pat = re.compile("(" + row[i] + ")")
            m = pat.search(text)
            if m:
                if prior:
                    line_num = 1 + text[: m.start()].count("\n")
                    report_error(
                        out_files,
                        line_num,
                        1,
                        669,
                        rule_type,
                        f"Both {prior} and {m.group(1)} exist",
                        "",
                        "",
                        "",
                        filename,
                        output_format=output_format,
                    )
                prior = m.group(1)


def find_errors(
    error_types: list,
    out_files: list,
    filetext: str,
    filename: str,
    min_block_size: int = 200,
    output_format: str = "-v1",
) -> int:
    """Apply error rules and report violations."""
    n_errors = 0
    prev_newlines = 0

    find_mismatchs(out_files, filetext, filename, output_format)

    # Remove comments (keep %\n)
    filetext = re.sub(r"(?<!\\)%.*(?:\$|\n)", "%\n", filetext)
    filetext = tokenize(filetext)

    # Take content after \begin{document}
    parts = re.split(r"\\begin\{document\}", filetext)
    if len(parts) > 1:
        filetext = parts[1]
        prev_newlines = num_newlines(parts[0])
        if len(parts) > 2:
            raise ValueError('More than one "\\begin{document}" in file')

    # Compile regexes and count brackets for each rule
    # Normalize: [name, regex, special, desc] or [name, regex, desc] -> 4-tuple
    bracket_re = re.compile(r"(?<!\[)\((?!\?)")
    for i, rule in enumerate(error_types):
        r = list(rule)
        if len(r) == 3:
            r.insert(2, "")  # [name, regex, desc] -> [name, regex, "", desc]
        name, regex_str, special, desc = r[:4]
        flags = 0
        if "(?i)" in regex_str:
            regex_str = regex_str.replace("(?i)", "")
            flags = re.IGNORECASE
        wrap_regex = "(" + regex_str + ")"
        rule_pattern = re.compile(wrap_regex, flags)
        n_brackets = len(bracket_re.findall(wrap_regex))
        error_types[i] = r + [rule_pattern, n_brackets]

    # Split by paragraph blocks - simplified: use whole text for small files
    blocks = [filetext]

    old_pars = {}

    for blocktext in blocks:
        if not blocktext.strip():
            continue
        par_pat = re.compile(r"(?:^|\n\s*\n|\Z)", re.MULTILINE)
        pars = par_pat.split(blocktext)
        linenum = 1 + prev_newlines
        for partext in pars:
            if len(partext) > 80 and partext.strip():
                if partext in old_pars:
                    report_error(
                        out_files,
                        linenum,
                        1,
                        667,
                        f"Duplicated paragraph {old_pars[partext]}",
                        "",
                        "",
                        "",
                        "",
                        filename,
                        output_format=output_format,
                    )
                    n_errors += 1
                else:
                    old_pars[partext] = linenum
            linenum += num_newlines(partext) + 2

        for rule in error_types:
            # Last two elements are always rule_pattern, n_brackets (appended during compile)
            rule_pattern, n_brackets = rule[-2], rule[-1]
            error_name, regex_str, special, desc = rule[:4]
            blocktext_ = blocktext

            if special.startswith("erase:"):
                erase_pat = special[6:]
                blocktext_ = re.sub(erase_pat, "", blocktext_)

            offset = 0
            linenum = 1 + prev_newlines
            for m in rule_pattern.finditer(blocktext_):
                trigger_text = m.group(1) if m.lastindex else m.group(0)
                start, end = m.start(), m.end()
                before_text = blocktext_[offset:start]
                after_text = blocktext_[end:]
                merged = before_text + trigger_text
                linenum = linenum + num_newlines(merged)

                trigger_user = tokens_to_user(trigger_text)
                amount = _max(0, 35 - len(trigger_user))
                context_before = "..." + tokens_to_user(before_text[-amount:] if amount else "")
                context_after = tokens_to_user(after_text[:amount])
                error_context = context_before + trigger_user + context_after + ".."

                spaces = " " * len(context_before)
                rule_ptrs = ("^" * len(trigger_user) if trigger_user else "^")
                rule_ptrs = spaces + rule_ptrs

                this_desc = desc
                for n in range(1, n_brackets + 1):
                    if m.lastindex and n <= m.lastindex:
                        arg = m.group(n)
                        this_desc = this_desc.replace(f"ARG{n}.CAP", f'"{arg}" does not appear to be a name')
                        this_desc = this_desc.replace(f"ARG{n}", f'"{arg}"')

                report_error(
                    out_files,
                    linenum,
                    1,
                    666,
                    error_name,
                    this_desc,
                    trigger_text,
                    error_context,
                    rule_ptrs,
                    filename,
                    output_format=output_format,
                )
                n_errors += 1
                offset = end

        prev_newlines += num_newlines(blocktext)

    return n_errors
