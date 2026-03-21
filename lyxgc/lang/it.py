"""Italian grammar rules - LaTeX structural rules with Italian messages."""
from ._structural import structural_rules
from ..rules import simple_rule

_MSGS = {
    "empty_mathblock": ("Blocco matematico vuoto", ""),
    "macro_no_brace": ("Macro senza {}", "Probabilmente serve {} dopo la macro."),
    "no_fullstop_after_cite": ("Manca punto dopo citazione a fine paragrafo", "Sembra mancare un punto."),
    "no_space_after_cite": ("Nessuno spazio dopo citazione", ""),
    "no_space_before_cite": ("Nessuno spazio prima di citazione", ""),
    "uline_starts_early": ("La sottolineatura inizia troppo presto", ""),
    "uline_ends_late": ("La sottolineatura finisce troppo tardi", ""),
    "space_before_footnote": ("Spazio prima di nota a pie' di pagina", ""),
    "footnote_period_comma": ("Punto/virgola dopo nota", "Se la nota si riferisce all'intera frase, va dopo il punto."),
    "double_punct": ("Punteggiatura doppia", ""),
    "implies_in_proof": ("Uso di \\implies in dimostrazione", "Usare \\Longrightarrow per la direzione della dimostrazione."),
    "no_space_after_ref": ("Nessuno spazio dopo riferimento", ""),
    "single_char": ("Carattere singolo", "Un solo carattere non ha senso."),
    "empty_begin_end": ("Blocco begin/end vuoto", ""),
    "proof_not_newline": ("La dimostrazione non inizia su nuova riga", "Inserire interruzione di paragrafo tra teorema e dimostrazione (Invio in LyX)."),
    "no_space_ref_left": ("Nessuno spazio prima del riferimento", "Forse serve uno spazio unificatore (~) prima del riferimento?"),
    "no_space_ref_right": ("Nessuno spazio dopo il riferimento", "Forse serve uno spazio unificatore (~) dopo il riferimento?"),
    "too_many_dots": ("Troppi punti", "Perche' piu' di un '.'?"),
    "space_cite_punct": ("Spazio tra citazione e punteggiatura", ""),
    "space_after_period_cap": ("Manca spazio tra punto e maiuscola", ""),
    "space_after_period_word": ("Manca spazio tra punto e parola", ""),
    "textquotedbl": ("Uso scorretto di \\textquotedbl", "Usare `` o ''."),
    "math_punct": ("Spazio tra blocco matematico e punteggiatura", ""),
    "cap_after_math": ("Maiuscola dopo blocco matematico", "Perche' c'e' una maiuscola dopo il blocco matematico?"),
    "equals_outside_math": ("Segno uguale fuori dal blocco matematico", "Il '=' dovrebbe essere dentro il blocco matematico."),
    "no_space_before_math": ("Nessuno spazio prima del blocco matematico", ""),
    "no_space_before_cite": ("Nessuno spazio prima di citazione", ""),
    "footnote_no_stop": ("Nota senza punto", ""),
    "no_space_after_math": ("Nessuno spazio dopo blocco matematico", ""),
    "no_space_before_macro": ("Nessuno spazio prima di macro", ""),
    "no_space_after_macro": ("Nessuno spazio dopo macro", ""),
    "colon_in_math": (": in modalita' matematica", "Usare \\colon per definire funzioni."),
    "ugly_fraction": ("Frazione poco elegante", r"Usare \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Troppi zeri senza separatore", ""),
    "duplicated_word": ("Parola duplicata", ""),
    "para_no_stop": ("Il paragrafo termina senza punto", ""),
    "para_no_cap": ("Il paragrafo inizia senza maiuscola", ""),
    "para_starts_dot": ("Il paragrafo inizia con punto?", ""),
    "punct_in_math": ("Punteggiatura dentro modalita' matematica", "Spostare ARG1 fuori dalla modalita' matematica."),
    "double_dot": ("Due punti", "Un solo punto basta."),
    "space_before_punct_math": ("Spazio prima della fine del blocco matematico", ""),
    "space_before_rparen": ("Spazio prima di )", ""),
    "proof_no_begin": ("\\end{proof} senza \\begin", "Rimuovere l'interruzione di paragrafo prima di \\end{proof}?"),
    "section_has_dot": ("Section con punto", "Le sezioni di solito non terminano con un punto."),
    "no_stop_def": ("Nessun punto prima di \\end{definition}", ""),
    "no_stop_end": ("Nessun punto prima di \\end{...}", ""),
}


def _italian_specific_rules() -> list:
    """Top 20 Italian grammatical/typographical errors."""
    return [
        simple_rule("perchè", "perché"),
        simple_rule("perche", "perché"),
        simple_rule("anccora", "ancora"),
        simple_rule("qual'è", "qual è"),
        simple_rule("daccordo", "d'accordo"),
        simple_rule("affinche", "affinché"),
        simple_rule("bensi", "bensì"),
        simple_rule("un amica", "un'amica"),
        simple_rule("finche", "finché"),
        simple_rule("giacche", "giacché"),
        simple_rule("sicche", "sicché"),
        simple_rule("poiche", "poiché"),
        simple_rule("ciononostante", "ciò nonostante"),
        simple_rule("sopratutto", "soprattutto"),
        simple_rule("anche", "anche"),
        simple_rule("oppure", "oppure"),
        simple_rule("altrimenti", "altrimenti"),
    ]


def generate_error_types() -> list:
    """Return Italian rules."""
    return structural_rules(_MSGS) + _italian_specific_rules()
