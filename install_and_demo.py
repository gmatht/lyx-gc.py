#!/usr/bin/env python3
"""
Install LyX-GC from the GitHub release tarball (Linux/macOS).

1. Downloads the latest release tarball from lyx-gc.py
2. Extracts and runs check_deps.py --all to install dependencies
3. Launches LyX with a sample .lyx file that prompts to try Tools > Check Text
   and contains sample errors (internal rules, ChkTeX, lacheck, LanguageTool)

Usage:
  python install_and_demo.py
  # or: ./install_and_demo.py  (if chmod +x)

Requires: Python 3.9+, curl, tar
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = "https://github.com/gmatht/lyx-gc.py"
RELEASE_TAG = "v0.1.0dev2"


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    """Run command; raise on failure if check=True."""
    return subprocess.run(cmd, cwd=cwd, check=check, text=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Install lyx-gc from release and run demo")
    parser.add_argument(
        "--tag",
        default=RELEASE_TAG,
        help=f"Release tag to install (default: {RELEASE_TAG})",
    )
    parser.add_argument(
        "--no-deps",
        action="store_true",
        help="Skip running check_deps.py (use if deps already installed)",
    )
    parser.add_argument(
        "--no-lyx",
        action="store_true",
        help="Skip launching LyX (install only)",
    )
    args = parser.parse_args()

    if sys.platform == "win32":
        print("This script is for Linux and macOS. Use install_and_demo.ps1 on Windows.")
        return 1

    if not shutil.which("curl"):
        print("Error: curl is required to download the release")
        return 1

    url = f"{REPO}/archive/refs/tags/{args.tag}.tar.gz"
    extract_dir_name = f"lyx-gc.py-{args.tag.lstrip('v')}"

    print(f"Downloading {url} ...")
    with tempfile.TemporaryDirectory() as tmp:
        tarball = Path(tmp) / "release.tar.gz"
        try:
            subprocess.run(
                ["curl", "-fsSL", "-o", str(tarball), url],
                check=True,
                timeout=120,
            )
        except subprocess.CalledProcessError:
            print(f"Failed to download. Try: curl -fsSL -o release.tar.gz {url}")
            return 1
        except FileNotFoundError:
            print("curl not found in PATH")
            return 1

        print("Extracting ...")
        run(["tar", "xzf", str(tarball)], cwd=Path(tmp))

        extracted = Path(tmp) / extract_dir_name
        if not extracted.is_dir():
            # GitHub tarball dir can be lyx-gc.py-<tag> e.g. lyx-gc.py-v0.1.0dev1
            alt = Path(tmp) / f"lyx-gc.py-{args.tag}"
            if alt.is_dir():
                extracted = alt
            else:
                dirs = list(Path(tmp).iterdir())
                if len(dirs) == 1 and dirs[0].is_dir():
                    extracted = dirs[0]
                else:
                    print(f"Unexpected tarball structure under {tmp}")
                    return 1

        py_dir = extracted / "py"
        if not (py_dir / "chktex.py").is_file():
            py_dir = extracted
        if not (py_dir / "chktex.py").is_file():
            print(f"chktex.py not found in {extracted}")
            return 1

        if not args.no_deps:
            print("\nRunning check_deps.py --all ...")
            run([sys.executable, str(py_dir / "check_deps.py"), "--all"], cwd=py_dir)

        sample = py_dir / "sample_errors.lyx"
        lyx_args = [str(sample)] if sample.is_file() else []

        if not args.no_lyx:
            run_lyx = py_dir / "run_lyx.py"
            if not run_lyx.is_file():
                print("run_lyx.py not found")
                return 1
            if lyx_args:
                print("\nLaunching LyX with sample document ...")
            else:
                print("\nLaunching LyX (sample_errors.lyx not in this release).")
            print("Use Tools > Check Text to run lyx-gc on any document.\n")
            run(
                [sys.executable, str(run_lyx)] + lyx_args,
                cwd=py_dir,
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
