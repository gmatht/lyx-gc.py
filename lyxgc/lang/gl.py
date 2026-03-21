"""Galician grammar rules - LaTeX structural rules with Galician messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Bloque matemático baleiro", ""),
    "macro_no_brace": ("Macro sen {}", "Probablemente fai falta {} despois do macro."),
    "no_fullstop_after_cite": ("Sen punto tras a cita ao final do parágrafo", "Semella que falta un punto."),
    "no_space_after_cite": ("Sen espazo tras a cita", ""),
    "no_space_before_cite": ("Sen espazo antes da cita", ""),
    "uline_starts_early": ("O subliñado comeza demasiado cedo", ""),
    "uline_ends_late": ("O subliñado remata demasiado tarde", ""),
    "space_before_footnote": ("Espazo antes da nota de pé", ""),
    "footnote_period_comma": ("Punto/vírgula tras a nota", "Se a nota refírese á frase completa, póñaa tras o punto."),
    "double_punct": ("Signos de puntuación dobres", ""),
    "implies_in_proof": ("Uso de \\implies na demostración", "Use \\Longrightarrow para a dirección da demostración."),
    "no_space_after_ref": ("Sen espazo tras a referência", ""),
    "single_char": ("Un só carácter", "Un só carácter normalmente non ten sentido."),
    "empty_begin_end": ("Bloque begin/end baleiro", ""),
    "proof_not_newline": ("A demostración non comeza en nova liña", "Introduza un separador de parágrafo entre o teorema e a demostración (Enter en LyX)."),
    "no_space_ref_left": ("Sen espazo á esquerda da referência", "Quizais un espazo non separable (~) antes da referência?"),
    "no_space_ref_right": ("Sen espazo á dereita da referência", "Quizais un espazo non separable (~) tras a referência?"),
    "too_many_dots": ("Demasiados puntos", "Por que máis dun '.'?"),
    "space_cite_punct": ("Espazo entre a cita e os signos de puntuación", ""),
    "space_after_period_cap": ("Falta espazo entre o punto e a maiúscula", ""),
    "space_after_period_word": ("Falta espazo entre o punto e a palabra", ""),
    "textquotedbl": ("Uso incorrecto de \\textquotedbl", "Use `` ou ''."),
    "math_punct": ("Espazo entre o bloque matemático e os signos de puntuación", ""),
    "cap_after_math": ("Maiúscula tras o bloque matemático", "Por que maiúscula tras o bloque matemático?"),
    "equals_outside_math": ("Sinal de igual fóra do bloque matemático", "O '=' debería estar dentro do bloque matemático."),
    "no_space_before_math": ("Sen espazo antes do bloque matemático", ""),
    "no_space_before_cite": ("Sen espazo antes da cita", ""),
    "footnote_no_stop": ("Nota sen punto", ""),
    "no_space_after_math": ("Sen espazo tras o bloque matemático", ""),
    "no_space_before_macro": ("Sen espazo antes do macro", ""),
    "no_space_after_macro": ("Sen espazo tras o macro", ""),
    "colon_in_math": (": en modo matemático", "Use \\colon para definir funcións."),
    "ugly_fraction": ("Fracción pouco estética", r"Use \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Demasiados ceros sen separador", ""),
    "duplicated_word": ("Palabra duplicada", ""),
    "para_no_stop": ("O parágrafo remata sen punto", ""),
    "para_no_cap": ("O parágrafo comeza sen maiúscula", ""),
    "para_starts_dot": ("O parágrafo comeza con punto?", ""),
    "punct_in_math": ("Signo de puntuación dentro do modo matemático", "Mova ARG1 fóra do modo matemático."),
    "double_dot": ("Dous puntos", "Un punto abonda."),
    "space_before_punct_math": ("Espazo antes do final do bloque matemático", ""),
    "space_before_rparen": ("Espazo antes de )", ""),
    "proof_no_begin": ("\\end{proof} sen \\begin", "Eliminar o separador de parágrafo antes de \\end{proof}?"),
    "section_has_dot": ("Sección con punto", "As seccións normalmente non rematan con punto."),
    "no_stop_def": ("Sen punto antes de \\end{definition}", ""),
    "no_stop_end": ("Sen punto antes de \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Galician rules."""
    return structural_rules(_MSGS) + common_academic_rules()
