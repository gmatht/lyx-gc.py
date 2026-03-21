"""Shared language-specific rules - common academic/LateX misspellings.

Used by languages that don't yet have their own top-20 grammatical rules.
These catch common English misspellings in international academic writing.
"""
from ..rules import simple_rule

# 20 common academic misspellings (English terms often appear in LaTeX globally)
COMMON_ACADEMIC_RULES = [
    simple_rule("concensus", "consensus"),
    simple_rule("occurence", "occurrence"),
    simple_rule("seperately", "separately"),
    simple_rule("definately", "definitely"),
    simple_rule("accomodate", "accommodate"),
    simple_rule("refered", "referred"),
    simple_rule("occured", "occurred"),
    simple_rule("tommorow", "tomorrow"),
    simple_rule("reccomend", "recommend"),
    simple_rule("neccesary", "necessary"),
    simple_rule("acheive", "achieve"),
    simple_rule("occuring", "occurring"),
    simple_rule("seperate", "separate"),
    simple_rule("independant", "independent"),
    simple_rule("recieve", "receive"),
    simple_rule("beleive", "believe"),
    simple_rule("wierd", "weird"),
    simple_rule("thier", "their"),
    simple_rule("teh", "the"),
    simple_rule("taht", "that"),
]


def common_academic_rules() -> list:
    """Return common academic misspellings for languages without native rules."""
    return COMMON_ACADEMIC_RULES
