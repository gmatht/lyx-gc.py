"""Chinese grammar rules - LaTeX structural rules with Chinese messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("空的数学块", ""),
    "macro_no_brace": ("宏缺少 {}", "宏后面可能需要 {}。"),
    "no_fullstop_after_cite": ("段落末尾引用后缺少句号", "可能缺少句号。"),
    "no_space_after_cite": ("引用后无空格", ""),
    "no_space_before_cite": ("引用前无空格", ""),
    "uline_starts_early": ("下划线开始过平", ""),
    "uline_ends_late": ("下划线结束过晚", ""),
    "space_before_footnote": ("脚注前有空格", ""),
    "footnote_period_comma": ("脚注后使用句号/逗号", "若脚注针对整句，应放在句号之后。"),
    "double_punct": ("双重标点", ""),
    "implies_in_proof": ("证明中使用 \\implies", "证明方向应使用 \\Longrightarrow。"),
    "no_space_after_ref": ("引用后无空格", ""),
    "single_char": ("单字符", "单字符通常无意义。"),
    "empty_begin_end": ("空的 begin/end 块", ""),
    "proof_not_newline": ("证明未另起一行", "请在定理与证明之间插入段落分隔（在 LyX 中按 Enter）。"),
    "no_space_ref_left": ("引用前无空格", "引用前是否应加不换行空格 (~)？"),
    "no_space_ref_right": ("引用后无空格", "引用后是否应加不换行空格 (~)？"),
    "too_many_dots": ("点号过多", "为何有多个 '.'？"),
    "space_cite_punct": ("引用与标点之间有空格", ""),
    "space_after_period_cap": ("句号与大写字母之间缺少空格", ""),
    "space_after_period_word": ("句号与单词之间缺少空格", ""),
    "textquotedbl": ("错误使用 \\textquotedbl", "请使用 `` 或 ''。"),
    "math_punct": ("数学块与标点之间的空格", ""),
    "cap_after_math": ("数学块后使用大写", "为何在数学块后使用大写？"),
    "equals_outside_math": ("等号在数学块外", "'=' 应在数学块内。"),
    "no_space_before_math": ("数学块前无空格", ""),
    "no_space_before_cite": ("引用前无空格", ""),
    "footnote_no_stop": ("脚注无句号", ""),
    "no_space_after_math": ("数学块后无空格", ""),
    "no_space_before_macro": ("宏前无空格", ""),
    "no_space_after_macro": ("宏后无空格", ""),
    "colon_in_math": ("数学模式中的冒号", "定义函数时请使用 \\colon。"),
    "ugly_fraction": ("不美观的分数", r"请使用 \\nicefrac{ARG1}{ARG2}。"),
    "too_many_zeros": ("零过多且无分隔符", ""),
    "duplicated_word": ("重复的词语", ""),
    "para_no_stop": ("段落未以句号结束", ""),
    "para_no_cap": ("段落未以大写开头", ""),
    "para_starts_dot": ("段落以句号开头？", ""),
    "punct_in_math": ("数学模式内使用标点", "请将 ARG1 移到数学模式外。"),
    "double_dot": ("双重句号", "一个句号即可。"),
    "space_before_punct_math": ("数学块结束前有空格", ""),
    "space_before_rparen": (") 前有空格", ""),
    "proof_no_begin": ("\\end{proof} 无对应 \\begin", "是否删除 \\end{proof} 前的段落分隔？"),
    "section_has_dot": ("小节带句号", "小节通常不以句号结束。"),
    "no_stop_def": ("\\end{definition} 前无句号", ""),
    "no_stop_end": ("\\end{...} 前无句号", ""),
}


def generate_error_types() -> list:
    """Return Chinese rules."""
    return structural_rules(_MSGS) + common_academic_rules()
