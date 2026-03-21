"""Serbian grammar rules - LaTeX structural rules with Serbian messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Празан математички блок", ""),
    "macro_no_brace": ("Макро без {}", "Вероватно је потребно {} после макра."),
    "no_fullstop_after_cite": ("Без тачке после цитата на крају параграфа", "Чини се да недостаје тачка."),
    "no_space_after_cite": ("Без размака после цитата", ""),
    "no_space_before_cite": ("Без размака пре цитата", ""),
    "uline_starts_early": ("Подвучвање почиње прерано", ""),
    "uline_ends_late": ("Подвучвање се завршава прекасно", ""),
    "space_before_footnote": ("Размак пре фусноте", ""),
    "footnote_period_comma": ("Тачка/зарез после фусноте", "Ако се фуснота односи на целу реченицу, ставите је после тачке."),
    "double_punct": ("Двоструки интерпункцијски знак", ""),
    "implies_in_proof": ("Употреба \\implies у доказу", "Користите \\Longrightarrow за смер доказа."),
    "no_space_after_ref": ("Без размака после референце", ""),
    "single_char": ("Један знак", "Један знак обично нема смисла."),
    "empty_begin_end": ("Празан begin/end блок", ""),
    "proof_not_newline": ("Доказ не почиње у новом реду", "Унесите раздвајач параграфа између теореме и доказа (Enter у LyX-у)."),
    "no_space_ref_left": ("Без размака лево од референце", "Можда непробивни размак (~) пре референце?"),
    "no_space_ref_right": ("Без размака десно од референце", "Можда непробивни размак (~) после референце?"),
    "too_many_dots": ("Превише тачака", "Зашто више од једне '.'?"),
    "space_cite_punct": ("Размак између цитата и интерпункције", ""),
    "space_after_period_cap": ("Недостаје размак између тачке и великог слова", ""),
    "space_after_period_word": ("Недостаје размак између тачке и речи", ""),
    "textquotedbl": ("Погрешна употреба \\textquotedbl", "Користите `` или ''."),
    "math_punct": ("Размак између математичког блока и интерпункције", ""),
    "cap_after_math": ("Велико слово после математичког блока", "Зашто велико слово после математичког блока?"),
    "equals_outside_math": ("Знак једнакости ван математичког блока", "'=' би требало да буде унутар математичког блока."),
    "no_space_before_math": ("Без размака пре математичког блока", ""),
    "no_space_before_cite": ("Без размака пре цитата", ""),
    "footnote_no_stop": ("Фуснота без тачке", ""),
    "no_space_after_math": ("Без размака после математичког блока", ""),
    "no_space_before_macro": ("Без размака пре макра", ""),
    "no_space_after_macro": ("Без размака после макра", ""),
    "colon_in_math": (": у математичком режиму", "Користите \\colon за дефинисање функција."),
    "ugly_fraction": ("Ругоба разломак", r"Користите \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Превише нула без сепаратора", ""),
    "duplicated_word": ("Двострука реч", ""),
    "para_no_stop": ("Параграф се завршава без тачке", ""),
    "para_no_cap": ("Параграф почиње без великог слова", ""),
    "para_starts_dot": ("Параграф почиње тачком?", ""),
    "punct_in_math": ("Интерпункција унутар математичког режима", "Померите ARG1 изван математичког режима."),
    "double_dot": ("Двострука тачка", "Једна тачка је довољна."),
    "space_before_punct_math": ("Размак пре краја математичког блока", ""),
    "space_before_rparen": ("Размак пре )", ""),
    "proof_no_begin": ("\\end{proof} без \\begin", "Уклонити раздвајач параграфа пре \\end{proof}?"),
    "section_has_dot": ("Одељак са тачком", "Одељци обично не завршавају тачком."),
    "no_stop_def": ("Без тачке пре \\end{definition}", ""),
    "no_stop_end": ("Без тачке пре \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Serbian rules."""
    return structural_rules(_MSGS) + common_academic_rules()
