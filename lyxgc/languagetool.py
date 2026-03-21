"""JLanguageTool integration - run LanguageTool and parse output."""
import os
import re
import subprocess
import shutil


def find_java() -> str:
    """Find Java executable."""
    return shutil.which("java") or "java"


def get_languagetool_path() -> str:
    """Get LanguageTool installation path from env or default."""
    default = os.path.expanduser("~/.data/LanguageTool-2.1/")
    return os.environ.get("LANGUAGETOOL_PATH", default)


def run_languagetool(tex_path: str) -> str | None:
    """
    Run LanguageTool on .tex file, write output to .tex.languagetool.
    Returns path to output file, or None if failed.
    """
    if not os.path.isabs(tex_path):
        tex_path = os.path.abspath(tex_path)

    out_file = tex_path + ".languagetool"
    java = find_java()
    lt_path = get_languagetool_path()
    jar = os.path.join(lt_path, "languagetool-commandline.jar")

    if not os.path.isfile(jar):
        return None

    try:
        result = subprocess.run(
            [java, "-jar", jar, tex_path],
            cwd=lt_path,
            capture_output=True,
            text=True,
            timeout=60,
        )
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(result.stdout)
        return out_file
    except Exception:
        return None


def parse_languagetool_output(filename: str, out_files: list, output_format: str = "-v1") -> int:
    """Parse .tex.languagetool file and report errors."""
    ignore_rules = {
        "ARTICLE_MISSING", "NOW", "EG_NO_COMMA", "IE_NO_COMMA",
        "EN_A_VS_AN", "WHITESPACE_RULE", "UNPAIRED_BRACKETS",
        "EN_UNPAIRED_BRACKETS", "COMMA_WHITESPACE", "WORD_REPEAT_RULE",
        "COMP_THAN_2", "COMMA_PARENTHESIS_WHITESPACE", "ENGLISH_WORD_REPEAT_BEGINNING_RULE",
        "EN_QUOTES[3]", "DOUBLE_PUNCTUATION",
    }

    out_file = filename + ".languagetool"
    if not os.path.isfile(out_file):
        return 0

    n_errors = 0
    from .report import report_error

    with open(out_file, encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    i = 0
    while i < len(lines):
        m = re.search(r"Line (\d+), column (\d+),.*Rule ID: (.*)$", lines[i])
        if m:
            line_num, col_num, rule_id = int(m.group(1)), int(m.group(2)), m.group(3).strip()
            error_name = error_context = error_ptr = ""
            if i + 1 < len(lines) and "Message:" in lines[i + 1]:
                error_name = lines[i + 1].replace("Message:", "").strip()
            if i + 2 < len(lines):
                error_context = lines[i + 2]
            if i + 3 < len(lines):
                error_ptr = lines[i + 3]
            if rule_id not in ignore_rules:
                report_error(
                    out_files,
                    line_num,
                    col_num,
                    rule_id,
                    error_name,
                    "",
                    "",
                    error_context,
                    error_ptr,
                    filename,
                    output_format=output_format,
                )
                n_errors += 1
            i += 4
            continue
        i += 1

    return n_errors
