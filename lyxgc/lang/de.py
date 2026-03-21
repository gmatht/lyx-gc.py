"""German grammar rules - LaTeX structural rules with German messages."""
from ._structural import structural_rules
from ..rules import simple_rule

# German messages for structural rules
_MSGS = {
    "empty_mathblock": ("Leerer Math-Block", ""),
    "macro_no_brace": ("Makro ohne {}", "Eine {} ist wahrscheinlich nach dem Makro nötig."),
    "no_fullstop_after_cite": ("Kein Punkt nach Zitat am Absatzende", "Ein Satzzeichen fehlt möglicherweise."),
    "no_space_after_cite": ("Kein Leerzeichen nach Zitat", ""),
    "no_space_before_cite": ("Kein Leerzeichen vor Zitat", ""),
    "uline_starts_early": ("Unterstreichung beginnt zu früh", ""),
    "uline_ends_late": ("Unterstreichung endet zu spät", ""),
    "space_before_footnote": ("Leerzeichen vor Fußnote", ""),
    "footnote_period_comma": ("Punkt/Komma nach Fußnote", "Wenn die Fußnote den ganzen Satz bezieht, gehört sie nach den Satz."),
    "double_punct": ("Doppelte Interpunktion", ""),
    "implies_in_proof": ("\\implies in Beweis", "Verwenden Sie \\Longrightarrow für die Beweisrichtung."),
    "no_space_after_ref": ("Kein Leerzeichen nach Referenz", ""),
    "single_char": ("Einzelnes Zeichen", "Ein einzelnes Zeichen ergibt kaum Sinn."),
    "empty_begin_end": ("Leerer Begin/End-Block", ""),
    "proof_not_newline": ("Beweis nicht auf neuer Zeile", "Bitte Absatzumbruch zwischen Lemma/Theorem und Beweis einfügen (Enter in LyX)."),
    "no_space_ref_left": ("Kein Leerzeichen vor Referenz", "Vielleicht geschütztes Leerzeichen (~) vor der Referenz?"),
    "no_space_ref_right": ("Kein Leerzeichen nach Referenz", "Vielleicht geschütztes Leerzeichen (~) nach der Referenz?"),
    "too_many_dots": ("Zu viele Punkte", "Warum mehrere '.' ?"),
    "space_cite_punct": ("Leerzeichen zwischen Zitat und Satzzeichen", ""),
    "space_after_period_cap": ("Fehlendes Leerzeichen zwischen Punkt und Majuskel", ""),
    "space_after_period_word": ("Fehlendes Leerzeichen zwischen Punkt und Wort", ""),
    "textquotedbl": ("Falsche Verwendung von \\textquotedbl", "Verwenden Sie `` oder ''."),
    "math_punct": ("Leerzeichen zwischen Math-Block und Satzzeichen", ""),
    "cap_after_math": ("Majuskel nach Math-Block", "Warum eine Majuskel nach dem Math-Block?"),
    "equals_outside_math": ("Gleichheitszeichen außerhalb Math", "Das '=' gehört vermutlich in den Math-Block."),
    "no_space_before_math": ("Kein Leerzeichen vor Math-Block", ""),
    "no_space_before_cite": ("Kein Leerzeichen vor Zitat", ""),
    "footnote_no_stop": ("Fußnote ohne Punkt", ""),
    "no_space_after_math": ("Kein Leerzeichen nach Math-Block", ""),
    "no_space_before_macro": ("Kein Leerzeichen vor Makro", ""),
    "no_space_after_macro": ("Kein Leerzeichen nach Makro", ""),
    "colon_in_math": (": im Math-Modus", "Verwenden Sie \\colon für Funktionsdefinitionen."),
    "ugly_fraction": ("Hässlicher Bruch", r"Verwenden Sie \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Zu viele Nullen ohne Trennzeichen", ""),
    "duplicated_word": ("Doppeltes Wort", ""),
    "para_no_stop": ("Absatz endet ohne Punkt", ""),
    "para_no_cap": ("Absatz beginnt ohne Majuskel", ""),
    "para_starts_dot": ("Absatz beginnt mit Punkt?", ""),
    "punct_in_math": ("Satzzeichen im Math-Modus", "ARG1 außerhalb des Math-Modus platzieren."),
    "double_dot": ("Doppelte Punkte", "Ein Punkt genügt."),
    "space_before_punct_math": ("Leerzeichen vor Math-Ende", ""),
    "space_before_rparen": ("Leerzeichen vor )", ""),
    "proof_no_begin": ("\\end{proof} ohne \\begin", "Absatzumbruch vor \\end{proof} entfernen?"),
    "section_has_dot": ("Section mit Punkt", "Sections enden üblicherweise ohne Punkt."),
    "no_stop_def": ("Kein Punkt vor \\end{definition}", ""),
    "no_stop_end": ("Kein Punkt vor \\end{...}", ""),
}


def _german_specific_rules() -> list:
    """Top 20 German grammatical/typographical errors."""
    return [
        simple_rule("aufgrund dem", "aufgrund des"),
        simple_rule("aus einander", "auseinander"),
        simple_rule("daß", "dass"),
        simple_rule("erfolgricher wie", "erfolgreicher als"),
        simple_rule("gemäß dem", "gemäß des"),
        simple_rule("trotz dem", "trotz des"),
        simple_rule("während dem", "während des"),
        simple_rule("sichtbar wie nie", "sichtbar als nie"),
        simple_rule("besser wie", "besser als"),
        simple_rule("als wie", "als"),
        simple_rule("seit dem", "seitdem"),
        simple_rule("weitgehendst", "weitgehend"),
        simple_rule("standart", "Standard"),
        simple_rule("des weiteren", "des Weiteren"),
        simple_rule("im folgendem", "im Folgenden"),
        simple_rule("zur zeit", "zurzeit"),
        simple_rule("einzigste", "einzige"),
        simple_rule("wieviel", "wie viel"),
        simple_rule("naechste", "nächste"),
        simple_rule("muessen", "müssen"),
    ]


def generate_error_types() -> list:
    """Return German rules. No capital-in-middle rule: in German nouns are capitalized."""
    return structural_rules(_MSGS) + _german_specific_rules()
