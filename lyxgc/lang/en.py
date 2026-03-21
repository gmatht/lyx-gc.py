"""English grammar rules - ported from chktex_en.pl."""
import re
from ..tokenizer import (
    START_MATH_CHAR,
    END_MATH_CHAR,
    C_BACKSLASH,
    RECURSIVE_BRACE,
    MATHBLOCK,
    NOTINMATH,
)
from ..rules import set_diff, simple_rule, generate_vowel_regex


def generate_error_types() -> list:
    """Return list of [Name, Regex, Special, Description]."""
    endnumber = r"(?=[^0-9]|$)"
    funnynumber = r"(?:11|18)(?:[0-9]{2})?(?:[0-9]{3})*" + endnumber
    vowelnumber = r"\b(?:8[0-9]*" + endnumber + "|" + funnynumber + ")"
    consonantnumber = r"\b(?!" + funnynumber + r")[012345679][0-9]*" + endnumber

    SetOfVowels = {
        "l": "aeiou",
        "U": "FHILMANXAEIOS",
        "d": "8",
        "number": vowelnumber,
        "includewords": r"(?:MF|NP|NL|LP|MPC|RTL|RMS|heir|RME|ME|heirloom|honest|honor|honorable|honorarium|honorary|honorific|honour|hour|hourglass|hourly|HTML|XML|FBI|SGML|SDL|HAA|LTL|SAA|S5|FSA|SSPM)",
        "excludewords": r"(?:US[a-zA-Z]*|Eur[a-zA-Z]*|Unix|eurhythmic|eurhythmy|euripus|one|unary|US|usage|useful|user|UK|unanimous|utrees?|uni[a-zA-Z]*|util[a-zA-Z]*|usual)",
        "s": "=",
        "isvowelset": True,
    }
    SetOfConsonants = {
        "l": set_diff("abcdefghijklmnopqrstuvwxyz", SetOfVowels["l"]),
        "U": set_diff("ABCDEFGHIJKLMNOPQRSTUVWXYZ", SetOfVowels["U"]),
        "d": set_diff("0123456789", SetOfVowels["d"]),
        "number": consonantnumber,
        "includewords": SetOfVowels["excludewords"],
        "excludewords": SetOfVowels["includewords"],
        "s": "+-<>#",
        "isvowelset": False,
    }

    VowelSound = generate_vowel_regex(SetOfVowels)
    ConsonantSound = generate_vowel_regex(SetOfConsonants)

    names = "Hilbert|Gentzen|Xu|Priorean|Schwendimann|Achilles|Dam|Mally|Kant|Kamp|Burgess|Rabin|Broersen|Johnsson|Saari|Nanson|Condorcet|Borda|Fishburn|Laslier|Dodgson|Tideman|Pratt|Lei|Clarke|Emerson|Sistla|Wolper|Vardi|Schnoebelen|Turing|Broesen|Intel|Until|Since|Hodkinson|Dedekind|Borel|Achilles|Zeno|Zenoness|Leonard|Stavi|Dedekind|Planck|Hintikka|Lange|Waldmeister|Moore|Reynolds|Fisher|Wright|Muller|Belnap|Perloff"

    lowerword = r"\b(?<!\\)[a-z]+\b"
    capword = r"\b(SSPM|Case|Ubuntu|Figure|Algorithm|Boolean|Australia|Dr|Prof|Table|" + names + r")\b"

    error_types = [
        simple_rule("we that", "we see that"),
        simple_rule("spelt correctly", "spelled correctly"),
        simple_rule("into to", "into"),
        simple_rule("never-the-less", "nevertheless"),
        simple_rule("the automata", "the automaton"),
        simple_rule("but and", "but"),
        simple_rule("in terms on the", "in terms of the"),
        simple_rule("in terms if the", "in terms of the"),
        simple_rule("psuedo", "pseudo"),
        simple_rule("visa-versa", "vice versa"),
        simple_rule("visa versa", "vice versa"),
        simple_rule("our selves", "ourselves"),
        simple_rule("the both", "both"),
        simple_rule("sch that", "such that"),
        ["Empty mathblock", START_MATH_CHAR + "  *" + END_MATH_CHAR, "", ""],
        # In tokenized text, \ is C_BACKSLASH
        ["No space after cite", re.escape(C_BACKSLASH) + r"cite\{[^}]*\}[a-zA-Z0-9]", "", ""],
        ["No space before cite", r"[a-zA-Z0-9]" + re.escape(C_BACKSLASH) + r"cite\{[^}]*\}", "", ""],
    ]

    return error_types
