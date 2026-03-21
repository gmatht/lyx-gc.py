"""Tokenizer for LaTeX: replaces \\, $, $$ with tokens for regex processing."""
import re

# Special chars used as tokens (must not appear in normal text)
START_MATH_CHAR = chr(1)
END_MATH_CHAR = chr(2)
C_BACKSLASH = chr(3)
C_DOLLAR_SIGN = chr(4)
NEW_ERROR_TYPE = chr(5)

# Token replacement table: (from_pattern, to_char, name, replacement_for_detokenize)
# Order matters: process \\ and \$ before $ for math
# replacement_for_detokenize: string to output when reversing (r"\\" would output 4 chars in Python!)
TOKEN_TABLE = [
    (r"\\\\", C_BACKSLASH, "BACKSLASH/", "\\\\"),  # output 2 backslashes
    (r"\\\$", C_DOLLAR_SIGN, "DOLLAR_SIGN/", r"\$"),
    ("$", START_MATH_CHAR, "cMATH", "$"),
    ("$", END_MATH_CHAR, "/cMATH", "$"),
]

# Regex patterns for tokenization (first two only, before $ handling)
_BACKSLASH_PAT = re.compile(r"\\\\")
_DOLLAR_ESC_PAT = re.compile(r"\\\$")

# Paragraph boundary
PAR = r"(?:(?m)\A|\n\s*\n|\Z)"
FULLSTOP = r"(?:(?<![.].)[.])"
MACROBLOCK = r"\\\\term\{[^}]*\}"

# Recursive brace (nested 5 levels like Perl)
_RECURSIVE_BRACE = r"\{[^{}]*\}"
for _ in range(4):
    _RECURSIVE_BRACE = r"\{(?:[^{}]|" + _RECURSIVE_BRACE + r")*\}"
RECURSIVE_BRACE = _RECURSIVE_BRACE

# Math block: $...$ or $$...$$
MATHBLOCK = START_MATH_CHAR + r"[^" + END_MATH_CHAR + r"]*" + END_MATH_CHAR

# Not in math lookahead
NOTINMATH = r"(?![^" + re.escape(START_MATH_CHAR) + r"]*" + re.escape(END_MATH_CHAR) + r")"


def tokenize(text: str) -> str:
    """Replace \\, \\$, $$...$$, $...$ with token chars."""
    # First pass: \\ and \$ (use first two entries of TOKEN_TABLE)
    result = _BACKSLASH_PAT.sub(TOKEN_TABLE[0][1], text)
    result = _DOLLAR_ESC_PAT.sub(TOKEN_TABLE[1][1], result)

    # Display math $$...$$
    result = re.sub(r"\$\$([^\$]*)\$\$",
                    START_MATH_CHAR + START_MATH_CHAR + r"\1" + END_MATH_CHAR + END_MATH_CHAR,
                    result)

    # Inline math $...$
    result = re.sub(r"\$([^\$]+)\$",
                    START_MATH_CHAR + r"\1" + END_MATH_CHAR,
                    result)

    return result


def detokenize(text: str) -> str:
    """Inverse of tokenize: convert tokens back to LaTeX."""
    # Process in reverse order, use replacement string not regex pattern
    for entry in reversed(TOKEN_TABLE):
        to_char = entry[1]
        from_replacement = entry[3] if len(entry) > 3 else entry[0]
        text = text.replace(to_char, from_replacement)
    return text


def tokens_to_user(text: str) -> str:
    """Convert tokens to user-visible format (same as detokenize)."""
    return detokenize(text)


def name_tokens(text: str) -> str:
    """Replace tokens with human-readable names for debug output."""
    for entry in reversed(TOKEN_TABLE):
        to_char, name = entry[1], entry[2]
        text = text.replace(to_char, "<" + name + ">")
    return text


def num_newlines(s: str) -> int:
    """Count newlines in string."""
    return s.count("\n")
