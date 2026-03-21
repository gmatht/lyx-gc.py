"""Occitan grammar rules - LaTeX structural rules with Occitan messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Blòc matematic void", ""),
    "macro_no_brace": ("Macro sens {}", "Un {} es benlèu necessari aprèp lo macro."),
    "no_fullstop_after_cite": ("Sens punt aprèp la citacion a la fin del paragraf", "Sembla que manca un punt."),
    "no_space_after_cite": ("Sens espaci aprèp la citacion", ""),
    "no_space_before_cite": ("Sens espaci abans la citacion", ""),
    "uline_starts_early": ("Lo soulignat comença tròp lèu", ""),
    "uline_ends_late": ("Lo soulignat acaba tròp tard", ""),
    "space_before_footnote": ("Espaci abans la nòta de pè", ""),
    "footnote_period_comma": ("Punt/virgula aprèp la nòta", "Se la nòta se referís a tota la frasa, metètz-la aprèp lo punt."),
    "double_punct": ("Ponctuacion dobla", ""),
    "implies_in_proof": ("Usatge de \\implies dins la demostracion", "Utilizatz \\Longrightarrow per la direccion de la demostracion."),
    "no_space_after_ref": ("Sens espaci aprèp la referéncia", ""),
    "single_char": ("Un sol caractèr", "Un sol caractèr a pas de sens d'ordina."),
    "empty_begin_end": ("Blòc begin/end void", ""),
    "proof_not_newline": ("La demostracion comença pas sus linha novèla", "Inseritz un separator de paragraf entre lo teorèma e la demostracion (Enter dins LyX)."),
    "no_space_ref_left": ("Sens espaci a esquèrra de la referéncia", "Benlèu un espaci non trencable (~) abans la referéncia?"),
    "no_space_ref_right": ("Sens espaci a drecha de la referéncia", "Benlèu un espaci non trencable (~) aprèp la referéncia?"),
    "too_many_dots": ("Tròp de punts", "Perqué mai qu'un '.'?"),
    "space_cite_punct": ("Espaci entre citacion e ponctuacion", ""),
    "space_after_period_cap": ("Espaci mancant entre punt e majuscula", ""),
    "space_after_period_word": ("Espaci mancant entre punt e mot", ""),
    "textquotedbl": ("Usatge incorrecte de \\textquotedbl", "Utilizatz `` o ''."),
    "math_punct": ("Espaci entre blòc mathematic e ponctuacion", ""),
    "cap_after_math": ("Majuscula aprèp lo blòc mathematic", "Perqué majuscula aprèp lo blòc mathematic?"),
    "equals_outside_math": ("Signe egal fòra del blòc mathematic", "Lo '=' deuriá èsser dins lo blòc mathematic."),
    "no_space_before_math": ("Sens espaci abans lo blòc mathematic", ""),
    "no_space_before_cite": ("Sens espaci abans la citacion", ""),
    "footnote_no_stop": ("Nòta sens punt", ""),
    "no_space_after_math": ("Sens espaci aprèp lo blòc mathematic", ""),
    "no_space_before_macro": ("Sens espaci abans lo macro", ""),
    "no_space_after_macro": ("Sens espaci aprèp lo macro", ""),
    "colon_in_math": (": en mòde mathematic", "Utilizatz \\colon per definir las foncions."),
    "ugly_fraction": ("Fraccion pauc estetica", r"Utilizatz \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Tròp de zeros sens separador", ""),
    "duplicated_word": ("Mot duplicat", ""),
    "para_no_stop": ("Lo paragraf acaba sens punt", ""),
    "para_no_cap": ("Lo paragraf comença sens majuscula", ""),
    "para_starts_dot": ("Lo paragraf comença amb punt?", ""),
    "punct_in_math": ("Ponctuacion dins lo mòde mathematic", "Desplaçatz ARG1 fòra del mòde mathematic."),
    "double_dot": ("Doas punts", "Un punct basta."),
    "space_before_punct_math": ("Espaci abans la fin del blòc mathematic", ""),
    "space_before_rparen": ("Espaci abans )", ""),
    "proof_no_begin": ("\\end{proof} sens \\begin", "Suprimitz lo separator de paragraf abans \\end{proof}?"),
    "section_has_dot": ("Seccion amb punt", "Las seccions acaban pas d'ordina amb punt."),
    "no_stop_def": ("Sens punt abans \\end{definition}", ""),
    "no_stop_end": ("Sens punt abans \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Occitan rules."""
    return structural_rules(_MSGS) + common_academic_rules()
