"""Error reporting for LyX-compatible output formats."""
import re

from .tokenizer import tokens_to_user, C_BACKSLASH, START_MATH_CHAR, END_MATH_CHAR


def embed_error_tags(rule_context: str, rule_ptrs: str, s_tag: str, e_tag: str) -> str:
    """Wrap the error part of rule_context with tags."""
    f = rule_ptrs.find("^")
    l = rule_ptrs.rfind("^")
    if f >= 0 and l >= 0:
        rule_context = (
            rule_context[:f]
            + s_tag
            + rule_context[f : l + 1]
            + e_tag
            + rule_context[l + 1 :]
        )
    return rule_context


def report_error(
    out_files: list,
    line_num: int,
    col_num: int,
    rule_id,
    rule_name: str,
    rule_description: str,
    rule_trigger: str,
    rule_context: str,
    rule_ptrs: str,
    error_filename: str,
    suggestion: str = "",
    output_format: str = "-v1",
    filename: str = "",
) -> None:
    """Report an error in ChkTeX/LyX compatible format."""
    import os
    import sys

    rule_name = rule_name.rstrip()
    rule_context = rule_context.rstrip()
    rule_id_str = f"{rule_id}; {rule_name}"
    lyx_gui = (os.environ.get("LYX_GUI") or "").lower()

    if output_format in ("-v0", "-v3"):
        error_text = ""
        if rule_description:
            error_text += rule_description.strip() + ".\n\n"
        if rule_context:
            rule_context_flat = rule_context.replace("\n", " ").replace("\r", " ")
            rule_context_flat = re.sub(r"^\s*", " ", rule_context_flat)  # Perl: s/^\s*/ /g
            error_text += "> " + embed_error_tags(
                rule_context_flat, " " + rule_ptrs, ">>", "<<"
            ) + ".\n\n  "
        error_text = error_text.rstrip()
        if suggestion:
            error_text += "\n" + suggestion
        newline_hack = "  "
        par_hack = "  "
        error_text = error_text.replace("\n\n", par_hack)
        error_text = error_text.replace("\n", newline_hack)
        error_text = error_text.replace(":", "<COLON/>")
        rule_id_str = rule_id_str.replace(":", "<COLON/>")

        error_text = tokens_to_user(error_text)

        if output_format == "-v0":
            error_filename_safe = error_filename.replace(":", "<COLON/>")
            line = f"{error_filename_safe}:{line_num}:{col_num}:{rule_id_str}:{error_text}\n"
        else:
            line = f'"{error_filename}", line {line_num}: {error_text}\n'
    else:
        error_text = (rule_description or "").replace("\n", " ")
        if error_text:
            error_text += ".  "
        rule_context_flat = rule_context.replace("\n", " ").replace("\r", " ")
        rule_ptrs_flat = rule_ptrs.replace("\n", " ").replace("\r", " ")
        error_text = tokens_to_user(error_text)
        line = (
            f"Warning {rule_id_str} in {error_filename} line {line_num}: {error_text}\n"
            f"{rule_context_flat}\n"
            f"{rule_ptrs_flat}\n"
        )

    for out in out_files:
        if hasattr(out, "write"):
            out.write(line)
        else:
            sys.stderr.write(line)
