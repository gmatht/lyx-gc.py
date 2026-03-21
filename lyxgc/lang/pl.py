"""Polish grammar rules - LaTeX structural rules with Polish messages."""
from ._structural import structural_rules
from ..rules import simple_rule

_MSGS = {
    "empty_mathblock": ("Pusty blok matematyczny", ""),
    "macro_no_brace": ("Makro bez {}", "Prawdopodobnie po makrze potrzebne jest {}."),
    "no_fullstop_after_cite": ("Brak kropki po cytacie na końcu akapitu", "Kropka może brakować."),
    "no_space_after_cite": ("Brak spacji po cytacie", ""),
    "no_space_before_cite": ("Brak spacji przed cytatem", ""),
    "uline_starts_early": ("Podkreślenie zaczyna się zbyt wcześnie", ""),
    "uline_ends_late": ("Podkreślenie kończy się zbyt późno", ""),
    "space_before_footnote": ("Spacja przed przypisem", ""),
    "footnote_period_comma": ("Kropka/przecinek po przypisie", "Jeśli przypis odnosi się do całego zdania, umieść go po kropce."),
    "double_punct": ("Podwójny znak interpunkcyjny", ""),
    "implies_in_proof": ("Użycie \\implies w dowodzie", "Użyj \\Longrightarrow dla kierunku dowodu."),
    "no_space_after_ref": ("Brak spacji po odwołaniu", ""),
    "single_char": ("Pojedynczy znak", "Pojedynczy znak zwykle nie ma sensu."),
    "empty_begin_end": ("Pusty blok begin/end", ""),
    "proof_not_newline": ("Dowód nie zaczyna się od nowej linii", "Wstaw podział akapitu między twierdzeniem a dowodem (Enter w LyX)."),
    "no_space_ref_left": ("Brak spacji po lewej stronie odwołania", "Może niełamliwa spacja (~) przed odwołaniem?"),
    "no_space_ref_right": ("Brak spacji po prawej stronie odwołania", "Może niełamliwa spacja (~) po odwołaniu?"),
    "too_many_dots": ("Zbyt wiele kropek", "Dlaczego więcej niż jedna '.'?"),
    "space_cite_punct": ("Spacja między cytatem a znakiem interpunkcyjnym", ""),
    "space_after_period_cap": ("Brakująca spacja między kropką a wielką literą", ""),
    "space_after_period_word": ("Brakująca spacja między kropką a słowem", ""),
    "textquotedbl": ("Błędne użycie \\textquotedbl", "Użyj `` lub ''."),
    "math_punct": ("Spacja między blokiem matematycznym a znakiem interpunkcyjnym", ""),
    "cap_after_math": ("Wielka litera po bloku matematycznym", "Dlaczego wielka litera po bloku matematycznym?"),
    "equals_outside_math": ("Znak równości poza blokiem matematycznym", "'=' powinno być wewnątrz bloku matematycznego."),
    "no_space_before_math": ("Brak spacji przed blokiem matematycznym", ""),
    "no_space_before_cite": ("Brak spacji przed cytatem", ""),
    "footnote_no_stop": ("Przypis bez kropki", ""),
    "no_space_after_math": ("Brak spacji po bloku matematycznym", ""),
    "no_space_before_macro": ("Brak spacji przed makrem", ""),
    "no_space_after_macro": ("Brak spacji po makrze", ""),
    "colon_in_math": (": w trybie matematycznym", "Użyj \\colon do definiowania funkcji."),
    "ugly_fraction": ("Nieładny ułamek", r"Użyj \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Zbyt wiele zer bez separatora", ""),
    "duplicated_word": ("Powtórzone słowo", ""),
    "para_no_stop": ("Akapit kończy się bez kropki", ""),
    "para_no_cap": ("Akapit zaczyna się bez wielkiej litery", ""),
    "para_starts_dot": ("Akapit zaczyna się od kropki?", ""),
    "punct_in_math": ("Znak interpunkcyjny wewnątrz trybu matematycznego", "Przenieś ARG1 poza tryb matematyczny."),
    "double_dot": ("Podwójna kropka", "Jedna kropka wystarczy."),
    "space_before_punct_math": ("Spacja przed końcem bloku matematycznego", ""),
    "space_before_rparen": ("Spacja przed )", ""),
    "proof_no_begin": ("\\end{proof} bez \\begin", "Usunąć podział akapitu przed \\end{proof}?"),
    "section_has_dot": ("Sekcja z kropką", "Sekcje zwykle nie kończą się kropką."),
    "no_stop_def": ("Brak kropki przed \\end{definition}", ""),
    "no_stop_end": ("Brak kropki przed \\end{...}", ""),
}


def _polish_specific_rules() -> list:
    """Top 20 Polish grammatical/typographical errors."""
    return [
        simple_rule("wogóle", "w ogóle"),
        simple_rule("napewno", "na pewno"),
        simple_rule("na prawdę", "naprawdę"),
        simple_rule("naprawde", "naprawdę"),
        simple_rule("wogule", "w ogóle"),
        simple_rule("miszcz", "mistrz"),
        simple_rule("swetr", "sweter"),
        simple_rule("japko", "jabłko"),
        simple_rule("dobże", "dobrze"),
        simple_rule("odrazu", "od razu"),
        simple_rule("poprostu", "po prostu"),
        simple_rule("narazie", "na razie"),
        simple_rule("wkoncu", "w końcu"),
        simple_rule("powinnismy", "powinniśmy"),
        simple_rule("moglibysmy", "mogliśmy"),
        simple_rule("trzymac", "trzymać"),
        simple_rule("rozumiec", "rozumieć"),
        simple_rule("znalezc", "znaleźć"),
        simple_rule("przyjsc", "przyjść"),
        simple_rule("isc", "iść"),
        simple_rule("wziasc", "wziąć"),
        simple_rule("rzeczywiscie", "rzeczywiście"),
    ]


def generate_error_types() -> list:
    """Return Polish rules."""
    return structural_rules(_MSGS) + _polish_specific_rules()
