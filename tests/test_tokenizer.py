"""Tests for tokenizer - from Perl Assert/Rassert in chktex.pl."""
import pytest
from lyxgc.tokenizer import (
    tokenize,
    detokenize,
    START_MATH_CHAR,
    END_MATH_CHAR,
    C_BACKSLASH,
    C_DOLLAR_SIGN,
    PAR,
    FULLSTOP,
    MATHBLOCK,
    tokens_to_user,
)
import re


def _rassert(reg: str, text: str, expected: str, flags: int = 0) -> None:
    """Mirror Perl Rassert: regex global match, join with comma."""
    pattern = re.compile(reg, flags)
    matches = pattern.findall(text)
    result = ",".join(str(m) for m in matches)
    if matches and result == "":
        result = "EMPTYSTR"
    assert result == expected, f"regex {reg!r} on {text!r}: expected {expected!r}, got {result!r}"


def _assert_equal(actual: str, expected: str) -> None:
    """Mirror Perl Assert."""
    assert actual == expected, f"expected {expected!r}, got {actual!r}"


class TestTokenize:
    """From chktex.pl Assert and Rassert calls."""

    def test_tokenize_complex(self):
        """Assert(tokenize('$$ $$\\$\\\\$\\$$\\$'), ...)."""
        text = "$$ $$\\$\\\\$\\$$\\$"
        expected = (
            START_MATH_CHAR + START_MATH_CHAR + " "
            + END_MATH_CHAR + END_MATH_CHAR
            + C_DOLLAR_SIGN + C_BACKSLASH + START_MATH_CHAR
            + C_DOLLAR_SIGN + END_MATH_CHAR + C_DOLLAR_SIGN
        )
        _assert_equal(tokenize(text), expected)

    def test_detokenize_reverses_tokenize(self):
        """detokenize(tokenize($test)) == $test. Perl: q! $ $ \\\\!"""
        # In Perl q! $ $ \\\\! = space $ space $ space + 2 backslashes
        test = " $ $ " + "\\\\"  # "\\\\" = two backslash chars
        result = detokenize(tokenize(test))
        _assert_equal(result, test)

    def test_fullstop(self):
        """Rassert($fullstop,"i.e.",".") and Rassert($fullstop,"i.  e.",".,.")."""
        _rassert(FULLSTOP, "i.e.", ".")
        _rassert(FULLSTOP, "i.  e.", ".,.")

    def test_par_aZ(self):
        """Rassert("aZ","a\\n","")."""
        _rassert("aZ", "a\n", "")

    def test_par_boundaries(self):
        """Rassert($par b," b"," b") etc. PAR = start, blank line, or end."""
        # Use re.MULTILINE for \A \Z; avoid (?m) in middle of pattern
        par = r"(?:^|\n\s*\n|\Z)"
        _rassert(par + " b", " b", " b", re.MULTILINE)
        _rassert("b " + par, "b ", "b ", re.MULTILINE)
        _rassert("b " + par, "b \n\n", "b \n\n", re.MULTILINE)

    def test_mathblock(self):
        """Rassert($mathblock,"$start abd$end edf","$start abd$end")."""
        text = START_MATH_CHAR + " abd" + END_MATH_CHAR + " edf"
        _rassert(MATHBLOCK, text, START_MATH_CHAR + " abd" + END_MATH_CHAR)


class TestTokensToUser:
    """tokens_to_user is alias for detokenize."""

    def test_tokens_to_user(self):
        assert tokens_to_user(START_MATH_CHAR + "x" + END_MATH_CHAR) == "$x$"
