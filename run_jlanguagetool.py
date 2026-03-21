#!/usr/bin/env python3
"""Run LanguageTool on a .tex file - port of chktex.pl.JLanguageTool.pl"""
import os
import sys
import shutil
import subprocess


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: run_jlanguagetool.py <file.tex>\n")
        sys.exit(1)

    in_path = sys.argv[1]
    if os.path.isabs(in_path):
        in_file = in_path
    else:
        in_file = os.path.abspath(in_path)

    out_file = in_file + ".languagetool"
    lt_path = os.environ.get("LANGUAGETOOL_PATH", os.path.expanduser("~/.data/LanguageTool-2.1/"))
    jar = os.path.join(lt_path, "languagetool-commandline.jar")
    java = shutil.which("java") or "java"

    need_update = not os.path.isfile(out_file)
    if not need_update and os.path.isfile(in_file):
        need_update = os.path.getmtime(in_file) > os.path.getmtime(out_file)

    if need_update and os.path.isfile(jar):
        try:
            tmp = out_file + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                subprocess.run(
                    [java, "-jar", jar, in_file],
                    cwd=lt_path,
                    stdout=f,
                    stderr=subprocess.DEVNULL,
                    timeout=120,
                )
            if os.path.isfile(out_file):
                os.remove(out_file)
            os.rename(tmp, out_file)
        except Exception as e:
            sys.stderr.write(f"LanguageTool error: {e}\n")


if __name__ == "__main__":
    main()
