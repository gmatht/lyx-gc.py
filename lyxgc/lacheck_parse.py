"""Parse lacheck output."""
import re
import subprocess


def parse_lacheck_output(filename: str, out_files: list, output_format: str = "-v1") -> int:
    """Run lacheck and parse output."""
    try:
        result = subprocess.run(
            ["lacheck", filename],
            capture_output=True,
            text=True,
            timeout=10,
        )
        output = result.stdout
    except Exception:
        return 0

    from .report import report_error

    ignore_reg = re.compile(
        r"possible unwanted space at|Could not open|Whitespace before punctation|"
        r"bad character in label|unmatched"
    )
    n_errors = 0

    for line in output.splitlines():
        m = re.match(r'"([^"]+)", line (\d+): (.*)', line)
        if m:
            error_filename, line_num, error_name = m.group(1), m.group(2), m.group(3)
            if not ignore_reg.search(error_name):
                report_error(
                    out_files,
                    int(line_num),
                    1,
                    "lacheck",
                    error_name,
                    "",
                    "",
                    "",
                    "",
                    error_filename,
                    output_format=output_format,
                )
                n_errors += 1

    return n_errors
