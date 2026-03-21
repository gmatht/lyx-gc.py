"""Czech grammar rules - LaTeX structural rules with Czech messages."""
from ._structural import structural_rules
from ..rules import simple_rule

_MSGS = {
    "empty_mathblock": ("Prázdný matematický blok", ""),
    "macro_no_brace": ("Makro bez {}", "Za makrem je pravděpodobně potřeba {}."),
    "no_fullstop_after_cite": ("Bez tečky za odkazem na konci odstavce", "Zdá se, že chybí tečka."),
    "no_space_after_cite": ("Bez mezery za odkazem", ""),
    "no_space_before_cite": ("Bez mezery před odkazem", ""),
    "uline_starts_early": ("Podtržení začíná příliš brzy", ""),
    "uline_ends_late": ("Podtržení končí příliš pozdě", ""),
    "space_before_footnote": ("Mezera před poznámkou pod čarou", ""),
    "footnote_period_comma": ("Tečka/čárka za poznámkou", "Pokud se poznámka vztahuje na celou větu, umístěte ji za tečku."),
    "double_punct": ("Dvojité interpunkční znaménko", ""),
    "implies_in_proof": ("Použití \\implies v důkazu", "Pro směr důkazu použijte \\Longrightarrow."),
    "no_space_after_ref": ("Bez mezery za odkazem", ""),
    "single_char": ("Jediný znak", "Jediný znak obvykle nedává smysl."),
    "empty_begin_end": ("Prázdný begin/end blok", ""),
    "proof_not_newline": ("Důkaz nezačíná na novém řádku", "Vložte oddělovač odstavce mezi větu a důkaz (Enter v LyX)."),
    "no_space_ref_left": ("Bez mezery vlevo od odkazu", "Možná nezlomitelná mezera (~) před odkazem?"),
    "no_space_ref_right": ("Bez mezery vpravo od odkazu", "Možná nezlomitelná mezera (~) za odkazem?"),
    "too_many_dots": ("Příliš mnoho teček", "Proč víc než jedna '.'?"),
    "space_cite_punct": ("Mezera mezi odkazem a interpunkcí", ""),
    "space_after_period_cap": ("Chybějící mezera mezi tečkou a velkým písmenem", ""),
    "space_after_period_word": ("Chybějící mezera mezi tečkou a slovem", ""),
    "textquotedbl": ("Nesprávné použití \\textquotedbl", "Použijte `` nebo ''."),
    "math_punct": ("Mezera mezi matematickým blokem a interpunkcí", ""),
    "cap_after_math": ("Velké písmeno za matematickým blokem", "Proč velké písmeno za matematickým blokem?"),
    "equals_outside_math": ("Rovnítko mimo matematický blok", "'=' by mělo být uvnitř matematického bloku."),
    "no_space_before_math": ("Bez mezery před matematickým blokem", ""),
    "no_space_before_cite": ("Bez mezery před odkazem", ""),
    "footnote_no_stop": ("Poznámka bez tečky", ""),
    "no_space_after_math": ("Bez mezery za matematickým blokem", ""),
    "no_space_before_macro": ("Bez mezery před makrem", ""),
    "no_space_after_macro": ("Bez mezery za makrem", ""),
    "colon_in_math": (": v matematickém režimu", "Pro definici funkcí použijte \\colon."),
    "ugly_fraction": ("Ošklivý zlomek", r"Použijte \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Příliš mnoho nul bez oddělovače", ""),
    "duplicated_word": ("Duplicitní slovo", ""),
    "para_no_stop": ("Odstavec končí bez tečky", ""),
    "para_no_cap": ("Odstavec začíná bez velkého písmene", ""),
    "para_starts_dot": ("Odstavec začíná tečkou?", ""),
    "punct_in_math": ("Interpunkce uvnitř matematického režimu", "Přesuňte ARG1 mimo matematický režim."),
    "double_dot": ("Dvojitá tečka", "Stačí jedna tečka."),
    "space_before_punct_math": ("Mezera před koncem matematického bloku", ""),
    "space_before_rparen": ("Mezera před )", ""),
    "proof_no_begin": ("\\end{proof} bez \\begin", "Odstranit oddělovač odstavce před \\end{proof}?"),
    "section_has_dot": ("Sekce s tečkou", "Sekce obvykle nekončí tečkou."),
    "no_stop_def": ("Bez tečky před \\end{definition}", ""),
    "no_stop_end": ("Bez tečky před \\end{...}", ""),
}


def _czech_specific_rules() -> list:
    """Top 20 Czech grammatical/typographical errors."""
    return [
        simple_rule("aby jsme", "abychom"),
        simple_rule("by jste", "byste"),
        simple_rule("byjste", "byste"),
        simple_rule("by jsi", "bys"),
        simple_rule("barysta", "barista"),
        simple_rule("bizardní", "bizarní"),
        simple_rule("briliantní", "brilantní"),
        simple_rule("ekzaktní", "exaktní"),
        simple_rule("konfort", "komfort"),
        simple_rule("inplementace", "implementace"),
        simple_rule("viz.", "viz"),
        simple_rule("desinformace", "dezinformace"),
        simple_rule("bedminton", "badminton"),
        simple_rule("histerie", "hysterie"),
        simple_rule("cenník", "ceník"),
        simple_rule("datumy", "data"),
        simple_rule("aliby", "alibi"),
        simple_rule("spravně", "správně"),
        simple_rule("cesky", "česky"),
        simple_rule("rekl", "řekl"),
        simple_rule("zkouska", "zkouška"),
        simple_rule("radši", "raději"),
    ]


def generate_error_types() -> list:
    """Return Czech rules."""
    return structural_rules(_MSGS) + _czech_specific_rules()
