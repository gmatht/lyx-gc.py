"""Portuguese grammar rules - LaTeX structural rules with Portuguese messages."""
from ..rules import simple_rule
from ._structural import structural_rules

_MSGS = {
    "empty_mathblock": ("Bloco matemático vazio", ""),
    "macro_no_brace": ("Macro sem {}", "Provavelmente é necessário {} após a macro."),
    "no_fullstop_after_cite": ("Falta ponto após citação no fim do parágrafo", "Parece faltar um ponto."),
    "no_space_after_cite": ("Sem espaço após citação", ""),
    "no_space_before_cite": ("Sem espaço antes de citação", ""),
    "uline_starts_early": ("O sublinhado começa cedo demais", ""),
    "uline_ends_late": ("O sublinhado termina tarde demais", ""),
    "space_before_footnote": ("Espaço antes de nota de rodapé", ""),
    "footnote_period_comma": ("Ponto/vírgula após nota", "Se a nota refere-se à frase inteira, deve vir após o ponto."),
    "double_punct": ("Pontuação dupla", ""),
    "implies_in_proof": ("Uso de \\implies na demonstração", "Use \\Longrightarrow para a direção da demonstração."),
    "no_space_after_ref": ("Sem espaço após referência", ""),
    "single_char": ("Caractere único", "Um único caractere não faz sentido."),
    "empty_begin_end": ("Bloco begin/end vazio", ""),
    "proof_not_newline": ("A demonstração não começa em nova linha", "Inserir quebra de parágrafo entre teorema e demonstração (Enter no LyX)."),
    "no_space_ref_left": ("Sem espaço antes da referência", "Talvez um espaço insecável (~) antes da referência?"),
    "no_space_ref_right": ("Sem espaço após a referência", "Talvez um espaço insecável (~) após a referência?"),
    "too_many_dots": ("Muitos pontos", "Por que vários '.'?"),
    "space_cite_punct": ("Espaço entre citação e pontuação", ""),
    "space_after_period_cap": ("Falta espaço entre ponto e maiúscula", ""),
    "space_after_period_word": ("Falta espaço entre ponto e palavra", ""),
    "textquotedbl": ("Uso incorreto de \\textquotedbl", "Use `` ou ''."),
    "math_punct": ("Espaço entre bloco matemático e pontuação", ""),
    "cap_after_math": ("Maiúscula após bloco matemático", "Por que há maiúscula após o bloco matemático?"),
    "equals_outside_math": ("Sinal de igual fora do bloco matemático", "O '=' deve estar dentro do bloco matemático."),
    "no_space_before_math": ("Sem espaço antes do bloco matemático", ""),
    "no_space_before_cite": ("Sem espaço antes de citação", ""),
    "footnote_no_stop": ("Nota sem ponto", ""),
    "no_space_after_math": ("Sem espaço após bloco matemático", ""),
    "no_space_before_macro": ("Sem espaço antes de macro", ""),
    "no_space_after_macro": ("Sem espaço após macro", ""),
    "colon_in_math": (": em modo matemático", "Use \\colon para definir funções."),
    "ugly_fraction": ("Fração feia", r"Use \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Muitos zeros sem separador", ""),
    "duplicated_word": ("Palavra duplicada", ""),
    "para_no_stop": ("O parágrafo termina sem ponto", ""),
    "para_no_cap": ("O parágrafo começa sem maiúscula", ""),
    "para_starts_dot": ("O parágrafo começa com ponto?", ""),
    "punct_in_math": ("Pontuação dentro do modo matemático", "Mova ARG1 para fora do modo matemático."),
    "double_dot": ("Dois pontos", "Um só ponto basta."),
    "space_before_punct_math": ("Espaço antes do fim do bloco matemático", ""),
    "space_before_rparen": ("Espaço antes de )", ""),
    "proof_no_begin": ("\\end{proof} sem \\begin", "Remover quebra de parágrafo antes de \\end{proof}?"),
    "section_has_dot": ("Section com ponto", "Sections geralmente não terminam com ponto."),
    "no_stop_def": ("Sem ponto antes de \\end{definition}", ""),
    "no_stop_end": ("Sem ponto antes de \\end{...}", ""),
}


def _portuguese_specific_rules() -> list:
    """Top 20 Portuguese grammatical/typographical errors."""
    return [
        simple_rule("interviu", "interveio"),
        simple_rule("concerteza", "com certeza"),
        simple_rule("a fim", "afim"),
        simple_rule("ao invés", "em vez"),
        simple_rule("no entanto", "no entanto"),
        simple_rule("por outro lado", "por outro lado"),
        simple_rule("alem disso", "além disso"),
    ]


def generate_error_types() -> list:
    """Return Portuguese rules."""
    return structural_rules(_MSGS) + _portuguese_specific_rules()
