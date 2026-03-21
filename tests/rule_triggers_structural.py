"""Trigger text for each structural rule - used by test_rules_per_rule.py.

All structural-only languages (de, generic, af, sq, ...) share the same regex patterns
from _structural.py; only the rule names (messages) differ per language.
This module provides one trigger per rule row so each rule can be tested.
"""
from lyxgc.tokenizer import LATEX_BS

# Ordered list: trigger for structural rule at index i (matches _structural.py order).
# Each trigger is chosen to fire that specific rule with minimal overlap.
TRIGGERS_STRUCTURAL = [
    r"$$ $$",                                    # 0: empty_mathblock
    r"x\fooCTLbar ",                             # 1: macro_no_brace
    r"x \cite{key}" + "\n\n",                    # 2: no_fullstop_after_cite
    r"\cite{key}x",                              # 3: no_space_after_cite
    r"x\cite{key}",                             # 4: no_space_before_cite
    r"\uline{ ",                                 # 5: uline_starts_early
    r"\uline{x }",                               # 6: uline_ends_late
    r" \footnote{",                              # 7: space_before_footnote
    r"\footnote{x}.",                            # 8: footnote_period_comma
    ", .",                                       # 9: double_punct
    r"(\implies)",                               # 10: implies_in_proof
    r"\ref{lem:x}y",                             # 11: no_space_after_ref
    " x ",                                       # 12: single_char
    r"\begin{lem}\end{lem}",                     # 13: empty_begin_end
    r"x\begin{proof}",                          # 14: proof_not_newline
    r"x\prettyref{sec:a}",                       # 15: no_space_ref_left
    r"\prettyref{sec:a}",                        # 16: no_space_ref_right
    ". .",                                       # 17: too_many_dots (first pattern)
    ". .",                                       # 18: too_many_dots (second)
    "  B",                                       # 19: too_many_dots (third pattern)
    r"\cite{key} ,",                             # 20: space_cite_punct
    ".X",                                        # 21: space_after_period_cap
    ".foo ",                                     # 22: space_after_period_word
    r"\textquotedbl{}",                          # 23: textquotedbl
    r"$x$ ,",                                    # 24: math_punct
    r"x $a$ Bar",                                # 25: cap_after_math
    r"$a$ = $b$",                                # 26: equals_outside_math
    r"x$x$",                                     # 27: no_space_before_math
    r"x\cite{key}",                             # 28: no_space_before_cite
    r"x \footnote{x} Bar",                       # 29: footnote_no_stop
    r"x \footnote{x} Bar",                       # 30: footnote_no_stop (duplicate)
    r"$x$y",                                     # 31: no_space_after_math
    r"x\term{foo}",                              # 32: no_space_before_macro
    r"\term{foo}x",                              # 33: no_space_after_macro
    r"$f: x$",                                   # 34: colon_in_math
    "1/2",                                       # 35: ugly_fraction
    "0000",                                      # 36: too_many_zeros
    "foo foo",                                   # 37: duplicated_word
    "x\n\n",                                     # 38: para_no_stop
    "\n\nfoo",                                   # 39: para_no_cap
    "\n\n.",                                     # 40: para_starts_dot
    r"$x,$",                                     # 41: punct_in_math
    ". .",                                       # 42: double_dot
    r"$x$ ;",                                    # 43: space_before_punct_math
    r"$x$ )",                                    # 44: space_before_rparen
    "\n\n" + r"\end{proof}",                      # 45: proof_no_begin
    r"\section{foo.}",                           # 46: section_has_dot
    r"x \end{definition}",                       # 47: no_stop_def
    r"x \end{equation}",                         # 48: no_stop_end
]
