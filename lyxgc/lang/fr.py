"""French grammar rules - ported from chktex_fr.pl."""
from ..tokenizer import START_MATH_CHAR, END_MATH_CHAR, C_BACKSLASH
from ..rules import simple_rule
import re


def generate_error_types() -> list:
    """Return list of [Name, Regex, Special, Description]."""
    capword = r"\b(Monsieur|Madame|M\.|Mme\.|Lundi|Dimanche)\b"
    lowerword = r"\b(?<!\\)[a-z]+\b"

    return [
        ["Empty mathblock", START_MATH_CHAR + "  *" + END_MATH_CHAR, "", ""],
        ["Macro sans {}.", r"[^\\]\\[a-zA-Z0-9]+CTL[a-zA-Z0-9]+\s", "", ""],
        ["Espace après citation", re.escape(C_BACKSLASH) + r"cite\{[^}]*\}[a-zA-Z0-9]", "", ""],
        simple_rule("our selves", "ourselves"),
    ]
