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


def get_lang_module(lang: str):
    """Load language module by code (en, fr)."""
    if lang == "fr":
        from lyxgc.lang import fr
        return fr.generate_error_types
    from lyxgc.lang import en
    return en.generate_error_types


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", help=".tex file to check")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-v", "--verbose", choices=["0", "1", "3"], default="1")
    args, rest = parser.parse_known_args()

    output_format = f"-v{args.verbose}"
    fileout = args.output or ""
    filename = args.filename or "stdin"

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

    lang = os.environ.get("LANG", "en")[:2]
    generate_error_types = get_lang_module(lang)
    error_types = generate_error_types()

    n_errors = find_errors(
        error_types,
        out_files,
        filetext,
        filename,
        min_block_size=200,
        output_format=output_format,
    )

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
