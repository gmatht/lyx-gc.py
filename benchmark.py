#!/usr/bin/env python3
"""Benchmark Perl (path/chktex.pl) vs Python (py/) lyx-gc grammar checker.

Compares:
  - Python rules engine (find_errors API) - the core logic ported from Perl
  - Python full CLI (chktex.py) - rules + optional ChkTeX/lacheck/LanguageTool
  - Perl (if path/chktex.pl exists)

Usage:
  python benchmark.py [OPTIONS] [FILES...]
  python benchmark.py -n 50                    # 50 iterations, default fixtures
  python benchmark.py tests/fixtures/*.tex    # custom fixtures
  python benchmark.py --py-only              # skip Perl even if available
"""
from __future__ import annotations

import io
import os
import subprocess
import sys
import time
from pathlib import Path

# Add py dir for imports
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

REPO_ROOT = SCRIPT_DIR.parent
PERL_CHKTEX_PL = REPO_ROOT / "path" / "chktex.pl"
PERL_CHKTEX = REPO_ROOT / "path" / "chktex"
DEFAULT_FIXTURES = [
    SCRIPT_DIR / "tests" / "fixtures" / "simple_errors.tex",
]

# Larger sample from test_correct_text (grammatically correct)
SAMPLE_EN = r"""
\documentclass{article}
\begin{document}

\section{Introduction}

This paper studies the complexity of model checking for branching-time temporal
logics. We show that the problem is PSPACE-complete for a broad class of
formulas. Our results extend earlier work by Clarke and Emerson, who established
the decidability of the problem for computational tree logic (CTL).

The remainder of this paper is organised as follows. In Section~2 we recall
the necessary definitions. Section~3 presents our main theorem. We conclude
with a discussion of open problems. All proofs have been formalised with
Isabelle.

\section{Preliminary Definitions}

Let $\mathcal{M}$ be a Kripke structure over a set of atomic propositions.
A path $\pi$ in $\mathcal{M}$ is an infinite sequence of states. We say that
$\pi$ satisfies a CTL formula $\phi$ when $\phi$ holds at the initial state
of $\pi$ under the usual semantics of path quantifiers and temporal operators.

For example, the formula $\mathbf{AG}\, p$ states that $p$ holds at every
state along every path. We refer the reader to Clarke and Emerson for a
comprehensive treatment of these notions.
\end{document}
"""

# Sample with intentional errors (triggers rules)
SAMPLE_ERRORS = r"""
\documentclass{article}
\begin{document}
This is we that wrong.
Also spelt correctly is wrong.
We need into to fix this.
Our selves think the both are errors.
Empty math: $$ $$ here.
\end{document}
"""


def _time_iterations(callback, n: int, warmup: int = 2) -> list[float]:
    """Run callback n times; first warmup runs discarded. Returns list of timings (seconds)."""
    for _ in range(warmup):
        callback()
    timings = []
    for _ in range(n):
        t0 = time.perf_counter()
        callback()
        timings.append(time.perf_counter() - t0)
    return timings


def bench_py_rules(text: str, n: int) -> tuple[int, list[float]]:
    """Benchmark Python find_errors (rules engine only). Returns (error_count, timings)."""
    from lyxgc.engine import find_errors
    from lyxgc.lang.en import generate_error_types

    error_types = generate_error_types()
    out = io.StringIO()

    def run():
        out.seek(0)
        out.truncate()
        find_errors(
            error_types,
            [out],
            text,
            "bench.tex",
            min_block_size=0,
            output_format="-v0",
        )

    timings = _time_iterations(run, n)
    out.seek(0)
    err_count = out.getvalue().count("\n")  # Approximate error lines
    return err_count, timings


def bench_py_cli(fixture_path: Path, n: int, env: dict) -> tuple[list[float], str]:
    """Benchmark Python chktex.py CLI. Returns (timings, stderr_preview)."""
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", suffix=".out", delete=False, encoding="utf-8") as f:
        out_path = f.name
    try:
        cmd = [
            sys.executable,
            str(SCRIPT_DIR / "chktex.py"),
            "-v0",
            "-o", out_path,
            str(fixture_path),
        ]
        err_preview = ""

        def run():
            r = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=str(SCRIPT_DIR),
                env=env,
                timeout=30,
            )
            if r.stderr:
                nonlocal err_preview
                err_preview = (r.stderr[:200] + "..." if len(r.stderr) > 200 else r.stderr)

        timings = _time_iterations(run, n)
        return timings, err_preview
    finally:
        try:
            if Path(out_path).exists():
                Path(out_path).unlink()
        except OSError:
            pass


def bench_perl(fixture_path: Path, n: int, env: dict) -> tuple[list[float] | None, str]:
    """Benchmark Perl chktex. Returns (timings, None) or (None, error_msg)."""
    perl = __import__("shutil").which("perl")
    if not perl:
        return None, "perl not found"

    # Prefer chktex.pl; fallback to chktex wrapper (which invokes chktex.pl)
    if PERL_CHKTEX_PL.exists():
        cmd = [perl, str(PERL_CHKTEX_PL), "-v0", str(fixture_path)]
        cwd = str(REPO_ROOT)
    elif PERL_CHKTEX.exists():
        # chktex is a shell script; run it (may require Unix)
        cmd = [str(PERL_CHKTEX), "-v0", str(fixture_path)]
        cwd = str(REPO_ROOT)
    else:
        return None, f"Perl chktex not found (looked for {PERL_CHKTEX_PL}, {PERL_CHKTEX})"

    def run():
        subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=cwd,
            env=env,
            timeout=30,
        )

    try:
        timings = _time_iterations(run, n)
        return timings, ""
    except Exception as e:
        return None, str(e)


def _stats(timings: list[float]) -> str:
    if not timings:
        return "N/A"
    avg = sum(timings) / len(timings)
    mn, mx = min(timings), max(timings)
    return f"avg={avg*1000:.2f}ms min={mn*1000:.2f}ms max={mx*1000:.2f}ms"


def main():
    import argparse
    p = argparse.ArgumentParser(description="Benchmark Perl vs Python lyx-gc")
    p.add_argument("-n", "--iterations", type=int, default=20, help="Iterations per benchmark")
    p.add_argument("--py-only", action="store_true", help="Skip Perl benchmark")
    p.add_argument("files", nargs="*", help=".tex files to benchmark (default: fixtures)")
    args = p.parse_args()

    n = args.iterations
    env = {**os.environ, "PYTHONPATH": str(SCRIPT_DIR)}
    env["HOME"] = env.get("HOME", os.path.expanduser("~"))
    env["USERPROFILE"] = env.get("USERPROFILE", env["HOME"])
    env["ORIG_CHKTEX"] = env.get("ORIG_CHKTEX", "")  # Disable external ChkTeX for fair comparison
    # Ensure LanguageTool path doesn't exist to avoid long Java startup
    env["LANGUAGETOOL_PATH"] = "/nonexistent"

    fixtures = [Path(f) for f in args.files] if args.files else DEFAULT_FIXTURES
    fixtures = [f for f in fixtures if f.exists()]
    samples = []
    temp_fixture = None
    if not fixtures:
        print("No fixture files found. Using in-memory samples.")
        samples = [
            ("small (errors)", SAMPLE_ERRORS),
            ("medium (~1 page)", SAMPLE_EN),
        ]
        import tempfile
        with tempfile.NamedTemporaryFile(mode="w", suffix=".tex", delete=False, encoding="utf-8") as f:
            f.write(SAMPLE_ERRORS)
            temp_fixture = Path(f.name)
            fixtures = [temp_fixture]

    try:
        _run_benchmark(args, n, env, fixtures, samples)
    finally:
        if temp_fixture and temp_fixture.exists():
            try:
                temp_fixture.unlink()
            except OSError:
                pass


def _run_benchmark(args, n: int, env: dict, fixtures: list[Path], samples: list[tuple[str, str]]):
    print("=" * 60)
    print("lyx-gc Benchmark: Perl vs Python")
    print("=" * 60)
    print(f"Iterations: {n}\n")

    # 1. Python rules engine (in-memory)
    print("--- Python rules engine (find_errors) ---")
    for name, text in samples:
        errs, timings = bench_py_rules(text, n)
        print(f"  {name}: errors~{errs}  {_stats(timings)}")
    if not samples:
        for fp in fixtures:
            text = fp.read_text(encoding="utf-8", errors="replace")
            errs, timings = bench_py_rules(text, n)
            print(f"  {fp.name}: errors~{errs}  {_stats(timings)}")

    # 2. Python CLI (only when we have file fixtures)
    if fixtures:
        print("\n--- Python CLI (chktex.py) ---")
        for fp in fixtures:
            timings, err = bench_py_cli(fp, n, env)
            print(f"  {fp.name}: {_stats(timings)}")
            if err:
                print(f"    stderr: {err[:100]}...")

    # 3. Perl
    if not args.py_only:
        print("\n--- Perl (path/chktex.pl) ---")
        for fp in fixtures:
            timings, msg = bench_perl(fp, n, env)
            if timings is not None:
                print(f"  {fp.name}: {_stats(timings)}")
            else:
                print(f"  {fp.name}: SKIP - {msg}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
