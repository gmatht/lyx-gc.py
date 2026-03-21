"""Korean grammar rules - LaTeX structural rules with Korean messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("빈 수학 블록", ""),
    "macro_no_brace": ("매크로에 {} 없음", "매크로 뒤에 {}가 필요할 수 있습니다."),
    "no_fullstop_after_cite": ("단락 끝 인용 뒤에 마침표 없음", "마침표가 누락되었을 수 있습니다."),
    "no_space_after_cite": ("인용 뒤 공백 없음", ""),
    "no_space_before_cite": ("인용 앞 공백 없음", ""),
    "uline_starts_early": ("밑줄이 너무 일찍 시작됨", ""),
    "uline_ends_late": ("밑줄이 너무 늦게 끝남", ""),
    "space_before_footnote": ("각주 앞 공백", ""),
    "footnote_period_comma": ("각주 뒤 마침표/쉼표", "각주가 전체 문장을 가리키면 마침표 뒤에 배치하세요."),
    "double_punct": ("중복된 구두점", ""),
    "implies_in_proof": ("증명에서 \\implies 사용", "증명 방향에는 \\Longrightarrow를 사용하세요."),
    "no_space_after_ref": ("참조 뒤 공백 없음", ""),
    "single_char": ("단일 문자", "단일 문자는 보통 의미가 없습니다."),
    "empty_begin_end": ("빈 begin/end 블록", ""),
    "proof_not_newline": ("증명이 새 줄에서 시작하지 않음", "정리와 증명 사이에 단락 구분을 넣으세요 (LyX에서 Enter)."),
    "no_space_ref_left": ("참조 왼쪽에 공백 없음", "참조 앞에 비분리 공백(~)이 필요할 수 있습니다."),
    "no_space_ref_right": ("참조 오른쪽에 공백 없음", "참조 뒤에 비분리 공백(~)이 필요할 수 있습니다."),
    "too_many_dots": ("점이 너무 많음", "왜 '.'가 여러 개인가요?"),
    "space_cite_punct": ("인용과 구두점 사이의 공백", ""),
    "space_after_period_cap": ("마침표와 대문자 사이 공백 누락", ""),
    "space_after_period_word": ("마침표와 단어 사이 공백 누락", ""),
    "textquotedbl": ("\\textquotedbl 잘못된 사용", "`` 또는 ''를 사용하세요."),
    "math_punct": ("수학 블록과 구두점 사이의 공백", ""),
    "cap_after_math": ("수학 블록 뒤 대문자", "왜 수학 블록 뒤에 대문자인가요?"),
    "equals_outside_math": ("수학 블록 밖의 등호", "'='는 수학 블록 안에 있어야 합니다."),
    "no_space_before_math": ("수학 블록 앞 공백 없음", ""),
    "no_space_before_cite": ("인용 앞 공백 없음", ""),
    "footnote_no_stop": ("마침표 없는 각주", ""),
    "no_space_after_math": ("수학 블록 뒤 공백 없음", ""),
    "no_space_before_macro": ("매크로 앞 공백 없음", ""),
    "no_space_after_macro": ("매크로 뒤 공백 없음", ""),
    "colon_in_math": (": 수학 모드에서", "함수 정의에 \\colon을 사용하세요."),
    "ugly_fraction": ("보기 흉한 분수", r"\\nicefrac{ARG1}{ARG2}를 사용하세요."),
    "too_many_zeros": ("구분자 없는 0이 너무 많음", ""),
    "duplicated_word": ("중복된 단어", ""),
    "para_no_stop": ("단락이 마침표 없이 끝남", ""),
    "para_no_cap": ("단락이 대문자 없이 시작함", ""),
    "para_starts_dot": ("단락이 마침표로 시작함?", ""),
    "punct_in_math": ("수학 모드 안의 구두점", "ARG1을 수학 모드 밖으로 옮기세요."),
    "double_dot": ("이중 마침표", "마침표 하나로 충분합니다."),
    "space_before_punct_math": ("수학 블록 끝 앞의 공백", ""),
    "space_before_rparen": (") 앞의 공백", ""),
    "proof_no_begin": ("\\end{proof}에 \\begin 없음", "\\end{proof} 앞의 단락 구분을 제거할까요?"),
    "section_has_dot": ("마침표가 있는 섹션", "섹션은 보통 마침표로 끝나지 않습니다."),
    "no_stop_def": ("\\end{definition} 앞에 마침표 없음", ""),
    "no_stop_end": ("\\end{...} 앞에 마침표 없음", ""),
}


def generate_error_types() -> list:
    """Return Korean rules."""
    return structural_rules(_MSGS) + common_academic_rules()
