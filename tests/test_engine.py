"""Tests for engine - FindErrors on sample .tex files."""
import io
import pytest
from lyxgc.engine import find_errors
from lyxgc.lang.en import generate_error_types


def test_find_errors_simple_rules():
    """FindErrors should detect 'we that', 'spelt correctly', etc."""
    tex = r"""
\documentclass{article}
\begin{document}
This is we that wrong.
Also spelt correctly is wrong.
We need into to fix this.
Our selves think the both are errors.
\end{document}
"""
    error_types = generate_error_types()
    out = io.StringIO()
    n = find_errors(
        error_types,
        [out],
        tex,
        "test.tex",
        min_block_size=0,
        output_format="-v0",
    )
    output = out.getvalue()
    assert n >= 4
    assert "we that" in output or "we see that" in output
    assert "spelt" in output or "spelled" in output
    assert "into to" in output or "into" in output
    assert "our selves" in output or "ourselves" in output
    assert "the both" in output or "both" in output
