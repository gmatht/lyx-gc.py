"""Rule utilities: setDiff, GenerateVowelRegex, SimpleRule."""
import re
from .tokenizer import (
    START_MATH_CHAR,
    END_MATH_CHAR,
    tokenize,
    detokenize,
)


def set_diff(a: str, b: str) -> str:
    """Set difference: chars in a that are not in b (treat strings as char sets)."""
    pattern = re.compile("[" + re.escape(b) + "]*")
    return pattern.sub("", a)


def simple_rule(bad: str, good: str | None = None) -> list:
    """Create a SimpleRule entry: [name, regex, "", description]."""
    bad_regex = bad.replace(" ", r"\s+")
    if len(bad_regex) >= 1:
        first_char = bad_regex[0]
        uc_first = first_char.upper()
        remainder = bad_regex[1:]
        bad_regex = r"\b[" + first_char + uc_first + "]" + remainder + r"\b"
        # Perl: $bad_regex=~s/[.].b$/./g  - replace trailing .\b with .
        if bad_regex.endswith(r".\b"):
            bad_regex = bad_regex[:-2] + "."
    else:
        bad_regex = r"\b" + bad_regex + r"\b"

    if good is not None:
        return [bad, bad_regex, "", f"Perhaps you mean '{good}'?"]
    return [bad, bad_regex, "", ""]


def generate_vowel_regex(
    set_of_vowels: dict,
    m_: str = r"(?:(?<!\\)[$])",
) -> str:
    """Build regex for vowel (or consonant) sounds. Used for a/an rules."""
    is_vowel_set = set_of_vowels.get("isvowelset", True)
    l_chars = set_of_vowels.get("l", "aeiou")
    u_chars = set_of_vowels.get("U", "FHILMANXAEIOS")
    d_chars = set_of_vowels.get("d", "8")
    number = set_of_vowels.get("number", r"\b[0123456789]+\b")
    excludewords = set_of_vowels.get("excludewords", "")
    includewords = set_of_vowels.get("includewords", "")

    # Characters only vowels/consonants in certain case
    uo = set_diff(u_chars, l_chars.upper())
    lo = set_diff(l_chars, u_chars.lower())
    li = l_chars + l_chars.upper()
    ui = u_chars + u_chars.lower()

    # Word starting with vowel letter or digit
    simple_word = r"\b[" + li + r"][a-zA-Z0-9]+\b"
    excluded_word = r"\b" + excludewords + r"\b"
    good_simple_word = "(?!" + excluded_word + ")" + simple_word
    complex_word = r"\b" + includewords + r"\b"
    word = "(?:(?:" + complex_word + ")|(?:" + good_simple_word + "))"

    # Letter that sounds like vowel (e.g. F=eff)
    letter = r"\b[" + ui + r"]\b"

    # LaTeX commands with no sound - skip in math
    mathignorelist = [
        "frac", "hat", "acute", "bar", "dot",
        "check", "grave", "vec", "ddot", "breve", "tilde",
    ]
    # Matches \frac{ or \acute{ etc. (LaTeX commands that don't affect vowel sound)
    mathignore = r"\\\\" + (r"|\\\\").join(m + r"\\s*\{ " for m in mathignorelist)

    # LaTeX symbol with vowel sound
    mathsymbol = "(?!" + mathignore + r")\\\[" + li + r"][a-zA-Z]*(?![a-zA-Z])"

    # Math block with vowel sound
    math = (
        START_MATH_CHAR
        + "(?:" + mathignore + "|[(])*"
        + "(?:"
        + "[" + d_chars + ui + "]|"
        + r"\[" + li + "]"
        + ")"
        + "[^" + END_MATH_CHAR + "]*" + END_MATH_CHAR
    )

    vowel_sound = "(?:" + word + "|" + letter + "|" + math + "|(?:\\\\\\$)?" + number + ")"
    return vowel_sound


def rassert(reg: str, text: str, expected: str) -> None:
    """Assert regex matches produce expected comma-joined string. Raises on failure."""
    try:
        pattern = re.compile(reg)
        matches = pattern.findall(text)
        result = ",".join(matches)
        if matches and result == "":
            result = "EMPTYSTR"
    except Exception as e:
        result = str(e)
    if result != expected:
        raise AssertionError(
            f"regex did not behave as expected:\n"
            f"input: {repr(text)}\nexpected: {repr(expected)}\nactual: {repr(result)}\nregex: {repr(reg)}"
        )
