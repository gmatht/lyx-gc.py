"""Interlingua grammar rules - LaTeX structural rules with Interlingua messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Blocco mathematic vacue", ""),
    "macro_no_brace": ("Macro sin {}", "Un {} es probabilmente necessari post le macro."),
    "no_fullstop_after_cite": ("Nulle puncto post citation al fin del paragrafo", "Un puncto pote mancar."),
    "no_space_after_cite": ("Nulle spatio post citation", ""),
    "no_space_before_cite": ("Nulle spatio ante citation", ""),
    "uline_starts_early": ("Sublineamento comencia troppo tosto", ""),
    "uline_ends_late": ("Sublineamento fini troppo tarde", ""),
    "space_before_footnote": ("Spatio ante nota de pede", ""),
    "footnote_period_comma": ("Puncto/virgula post nota", "Si le nota refere al phrase integre, pone lo post le puncto."),
    "double_punct": ("Punctuation duple", ""),
    "implies_in_proof": ("Uso de \\implies in demonstration", "Usa \\Longrightarrow pro le direction del demonstration."),
    "no_space_after_ref": ("Nulle spatio post referentia", ""),
    "single_char": ("Un sol character", "Un sol character normalmente ha nulle senso."),
    "empty_begin_end": ("Blocco begin/end vacue", ""),
    "proof_not_newline": ("Demonstration non comencia in nove linea", "Insere disruption de paragrafo inter theorema e demonstration (Enter in LyX)."),
    "no_space_ref_left": ("Nulle spatio a sinistra del referentia", "Forsan un spatio non-disruptibile (~) ante le referentia?"),
    "no_space_ref_right": ("Nulle spatio a dextra del referentia", "Forsan un spatio non-disruptibile (~) post le referentia?"),
    "too_many_dots": ("Tro multo punctos", "Proque plus que un '.'?"),
    "space_cite_punct": ("Spatio inter citation e punctuation", ""),
    "space_after_period_cap": ("Spatio mancante inter puncto e majuscula", ""),
    "space_after_period_word": ("Spatio mancante inter puncto e parola", ""),
    "textquotedbl": ("Uso incorrecte de \\textquotedbl", "Usa `` o ''."),
    "math_punct": ("Spatio inter blocco mathematic e punctuation", ""),
    "cap_after_math": ("Majuscula post blocco mathematic", "Proque majuscula post le blocco mathematic?"),
    "equals_outside_math": ("Signo de equalitate foras del blocco mathematic", "Le '=' deberea esser intra le blocco mathematic."),
    "no_space_before_math": ("Nulle spatio ante blocco mathematic", ""),
    "no_space_before_cite": ("Nulle spatio ante citation", ""),
    "footnote_no_stop": ("Nota sin puncto", ""),
    "no_space_after_math": ("Nulle spatio post blocco mathematic", ""),
    "no_space_before_macro": ("Nulle spatio ante macro", ""),
    "no_space_after_macro": ("Nulle spatio post macro", ""),
    "colon_in_math": (": in modo mathematic", "Usa \\colon pro definir functiones."),
    "ugly_fraction": ("Fraction inesthetic", r"Usa \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Tro multo zeros sin separator", ""),
    "duplicated_word": ("Parola duplicate", ""),
    "para_no_stop": ("Paragrafo fini sin puncto", ""),
    "para_no_cap": ("Paragrafo comencia sin majuscula", ""),
    "para_starts_dot": ("Paragrafo comencia con puncto?", ""),
    "punct_in_math": ("Punctuation intra modo mathematic", "Move ARG1 foras del modo mathematic."),
    "double_dot": ("Duo punctos", "Un puncto suffice."),
    "space_before_punct_math": ("Spatio ante fin del blocco mathematic", ""),
    "space_before_rparen": ("Spatio ante )", ""),
    "proof_no_begin": ("\\end{proof} sin \\begin", "Remove disruption de paragrafo ante \\end{proof}?"),
    "section_has_dot": ("Section con puncto", "Le sectiones normalmente non fini con puncto."),
    "no_stop_def": ("Nulle puncto ante \\end{definition}", ""),
    "no_stop_end": ("Nulle puncto ante \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Interlingua rules."""
    return structural_rules(_MSGS) + common_academic_rules()
