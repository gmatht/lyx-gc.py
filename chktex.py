#!/usr/bin/env python3
"""ChkTeX replacement - grammar checker for LyX/LaTeX. Port of path/chktex.pl"""
import os
import sys
import argparse
import subprocess
from pathlib import Path

# Add py dir to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from lyxgc.engine import find_errors
from lyxgc.languagetool import parse_languagetool_output
from lyxgc.chktex_parse import parse_chktex_output
from lyxgc.lacheck_parse import parse_lacheck_output
from lyxgc.lang.registry import resolve_language, get_generate_error_types


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", help=".tex file to check")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-x", dest="input_file", help="Input file (LyX uses -x file.tex)")
    parser.add_argument("-v", "--verbose", choices=["0", "1", "3"], default="1")
    parser.add_argument(
        "-l", "--lang",
        help="Language: LyX name (e.g. 'English (USA)') or locale (e.g. en_US, fr). Overrides LYX_LANGUAGE/LANG.",
    )
    args, rest = parser.parse_known_args()

    output_format = f"-v{args.verbose}"
    fileout = args.output or ""
    filename = args.input_file or args.filename or "stdin"

    if filename == "stdin":
        filetext = sys.stdin.read()
    else:
        filename = os.path.abspath(filename)
        with open(filename, encoding="utf-8") as f:
            filetext = f.read()

    out_files = []
    if fileout:
        out_files = [open(fileout, "w", encoding="utf-8")]
    else:
        out_files = [sys.stdout]

    # -l/--lang > LYX_LANGUAGE > LANG (locale e.g. en_AU.UTF-8)
    lang_spec = args.lang or os.environ.get("LYX_LANGUAGE") or os.environ.get("LANG", "en")
    rule_module = resolve_language(lang_spec)
    if rule_module is None:
        low = lang_spec.lower()
        if low in ("c", "posix") or low.startswith("c."):
            rule_module = "en"  # LANG=C or C.UTF-8: fall back to English
    generate_error_types = get_generate_error_types(rule_module)
    error_types = generate_error_types()

    n_errors = find_errors(
        error_types,
        out_files,
        filetext,
        filename,
        min_block_size=0,  # Check all text including short paragraphs
        output_format=output_format,
    )
    if out_files and hasattr(out_files[0], "flush"):
        out_files[0].flush()

    if filename != "stdin":
        n_errors += parse_languagetool_output(filename, out_files, output_format)
        n_errors += parse_lacheck_output(filename, out_files, output_format)
        n_errors += parse_chktex_output(filename, out_files, output_format)

    if fileout:
        out_files[0].close()
        if n_errors == 0:
            with open(fileout, "a", encoding="utf-8") as f:
                f.write("X:1:1: All OK (^_^)\n")
        else:
            subprocess.Popen(
                [sys.executable, str(Path(__file__).parent / "run_jlanguagetool.py"), filename],
                cwd=os.path.dirname(filename),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )


if __name__ == "__main__":
    main()
