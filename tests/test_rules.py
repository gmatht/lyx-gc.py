"""Tests for rules - from Perl Rassert in chktex_en.pl and rules logic."""
import pytest
from lyxgc.rules import set_diff, simple_rule, generate_vowel_regex, rassert
from lyxgc.tokenizer import tokenize, START_MATH_CHAR, END_MATH_CHAR


class TestSetDiff:
    """From chktex_en.pl: setDiff for consonants."""

    def test_set_diff_basic(self):
        assert set_diff("abcdefghijklmnopqrstuvwxyz", "aeiou") == "bcdfghjklmnpqrstvwxyz"
        assert set_diff("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "AEIOU") == "BCDFGHJKLMNPQRSTVWXYZ"
        assert set_diff("0123456789", "8") == "012345679"


class TestGenerateVowelRegex:
    """From chktex_en.pl - GenerateVowelRegex produces valid regex."""

    def test_consonant_number(self):
        """Rassert($consonantnumber,"1800 180 a 8 2","180,2")."""
        endnumber = r"(?=[^0-9]|$)"
        funnynumber = r"(?:11|18)(?:[0-9]{2})?(?:[0-9]{3})*" + endnumber
        # Negative lookahead: (?!funnynumber) - use (?!...) not (?!(...)) for correct capture
        consonantnumber = r"\b(?!" + funnynumber + r")[012345679][0-9]*" + endnumber
        rassert(consonantnumber, "1800 180 a 8 2", "180,2")

    def test_vowel_consonant_sounds(self):
        """Rassert($ConsonantSound,...) and Rassert($VowelSound,...)."""
        endnumber = r"(?=[^0-9]|$)"
        funnynumber = r"(?:11|18)(?:[0-9]{2})?(?:[0-9]{3})*" + endnumber
        vowelnumber = r"\b(?:8[0-9]*" + endnumber + "|" + funnynumber + ")"
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
        consonantnumber = r"\b(?!" + funnynumber + r")[012345679][0-9]*" + endnumber
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

        rassert(ConsonantSound, "apple Apple pear X-ray 1800 180 0", "pear,ray,180,0")
        rassert(VowelSound, "apple Apple pear X-ray 1800 180 0", "apple,Apple,X,1800")
        # "An \$500" in Perl = backslash-dollar; consonant "500" matches
        rassert("An " + ConsonantSound, "An \\$500 An \\$1800", "An \\$500")


class TestSimpleRule:
    """SimpleRule output format."""

    def test_simple_rule_with_correction(self):
        """SimpleRule("we that", "we see that")."""
        r = simple_rule("we that", "we see that")
        assert r[0] == "we that"
        assert r[2] == ""
        assert "we see that" in r[3]
        # Should match "we that"
        import re
        assert re.search(r[1], "This is we that correct")

    def test_simple_rule_without_correction(self):
        """SimpleRule("is are","")."""
        r = simple_rule("is are", None)
        assert r[0] == "is are"
        assert r[3] == ""

    def test_simple_rule_spelt(self):
        """SimpleRule("spelt correctly", "spelled correctly")."""
        r = simple_rule("spelt correctly", "spelled correctly")
        import re
        assert re.search(r[1], "spelt correctly")
        assert re.search(r[1], "Spelt correctly")
