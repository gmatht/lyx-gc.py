"""Parse ChkTeX (system binary) output."""
import os
import re
import subprocess


def parse_chktex_output(filename: str, out_files: list, output_format: str = "-v1") -> int:
    """Run ChkTeX binary and parse output, report in LyX format."""
    orig_chktex = os.environ.get("ORIG_CHKTEX", "chktex")
    if not orig_chktex:
        return 0

    cmd = [
        orig_chktex,
        filename,
        "-n26", "-n24", "-n15", "-n16", "-n1", "-n31", "-n27", "-n36", "-n40", "-n2",
        "-v1",
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        output = result.stdout
    except Exception:
        return 0

    from .report import report_error

    n_errors = 0
    error_pos = 1
    line_num = col_num = rule_id = error_name = error_context = error_ptr = "0"

    for line in output.splitlines():
        if error_pos == 1:
            m = re.match(
                r"(Warning|Error|Message) ([^ ]+) in (.*) line ([1-9][0-9]*): (.*)",
                line,
            )
            if m:
                rule_id = m.group(2)
                error_filename = m.group(3)
                line_num = m.group(4)
                error_name = m.group(5).rstrip(".")
                error_pos = 2
        elif error_pos == 2:
            error_context = line.rstrip(".")
            error_pos = 3
        elif error_pos == 3:
            error_ptr = line
            report_error(
                out_files,
                int(line_num),
                1,
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
            error_pos = 1

    return n_errors
