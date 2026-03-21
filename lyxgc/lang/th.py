"""Thai grammar rules - LaTeX structural rules with Thai messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("บล็อกคณิตศาสตร์ว่าง", ""),
    "macro_no_brace": ("มาโครไม่มี {}", "อาจต้องมี {} หลังมาโคร"),
    "no_fullstop_after_cite": ("ไม่มีจุดหลังอ้างอิงที่ท้ายย่อหน้า", "อาจขาดจุด"),
    "no_space_after_cite": ("ไม่มีช่องว่างหลังอ้างอิง", ""),
    "no_space_before_cite": ("ไม่มีช่องว่างก่อนอ้างอิง", ""),
    "uline_starts_early": ("เส้นขีดเริ่มต้นเร็วเกินไป", ""),
    "uline_ends_late": ("เส้นขีดสิ้นสุดช้าเกินไป", ""),
    "space_before_footnote": ("ช่องว่างก่อนเชิงอรรถ", ""),
    "footnote_period_comma": ("จุด/จุลภาคหลังเชิงอรรถ", "ถ้าเชิงอรรถอ้างถึงทั้งประโยค วางไว้หลังจุด"),
    "double_punct": ("เครื่องหมายวรรคตอนซ้อน", ""),
    "implies_in_proof": ("ใช้ \\implies ในการพิสูจน์", "ใช้ \\Longrightarrow สำหรับทิศทางการพิสูจน์"),
    "no_space_after_ref": ("ไม่มีช่องว่างหลังอ้างอิง", ""),
    "single_char": ("ตัวอักษรเดี่ยว", "ตัวอักษรเดี่ยวมักไม่มีความหมาย"),
    "empty_begin_end": ("บล็อก begin/end ว่าง", ""),
    "proof_not_newline": ("การพิสูจน์ไม่ได้ขึ้นต้นบรรทัดใหม่", "ใส่ตัวคั่นย่อหน้าระหว่างทฤษฎีบทกับการพิสูจน์ (Enter ใน LyX)"),
    "no_space_ref_left": ("ไม่มีช่องว่างทางซ้ายของอ้างอิง", "อาจต้องมีช่องว่างไม่ขึ้นบรรทัดใหม่ (~) ก่อนอ้างอิง?"),
    "no_space_ref_right": ("ไม่มีช่องว่างทางขวาของอ้างอิง", "อาจต้องมีช่องว่างไม่ขึ้นบรรทัดใหม่ (~) หลังอ้างอิง?"),
    "too_many_dots": ("จุดมากเกินไป", "ทำไมมากกว่าหนึ่ง '.'?"),
    "space_cite_punct": ("ช่องว่างระหว่างอ้างอิงกับเครื่องหมายวรรคตอน", ""),
    "space_after_period_cap": ("ขาดช่องว่างระหว่างจุดกับตัวพิมพ์ใหญ่", ""),
    "space_after_period_word": ("ขาดช่องว่างระหว่างจุดกับคำ", ""),
    "textquotedbl": ("การใช้ \\textquotedbl ผิด", "ใช้ `` หรือ ''"),
    "math_punct": ("ช่องว่างระหว่างบล็อกคณิตศาสตร์กับเครื่องหมายวรรคตอน", ""),
    "cap_after_math": ("ตัวพิมพ์ใหญ่หลังบล็อกคณิตศาสตร์", "ทำไมตัวพิมพ์ใหญ่หลังบล็อกคณิตศาสตร์?"),
    "equals_outside_math": ("เครื่องหมายเท่ากันอยู่นอกบล็อกคณิตศาสตร์", "'=' ควรอยู่ในบล็อกคณิตศาสตร์"),
    "no_space_before_math": ("ไม่มีช่องว่างก่อนบล็อกคณิตศาสตร์", ""),
    "no_space_before_cite": ("ไม่มีช่องว่างก่อนอ้างอิง", ""),
    "footnote_no_stop": ("เชิงอรรถไม่มีจุด", ""),
    "no_space_after_math": ("ไม่มีช่องว่างหลังบล็อกคณิตศาสตร์", ""),
    "no_space_before_macro": ("ไม่มีช่องว่างก่อนมาโคร", ""),
    "no_space_after_macro": ("ไม่มีช่องว่างหลังมาโคร", ""),
    "colon_in_math": (": ในโหมดคณิตศาสตร์", "ใช้ \\colon เพื่อกำหนดฟังก์ชัน"),
    "ugly_fraction": ("เศษส่วนไม่สวย", r"ใช้ \\nicefrac{ARG1}{ARG2}"),
    "too_many_zeros": ("ศูนย์มากเกินไปโดยไม่มีตัวคั่น", ""),
    "duplicated_word": ("คำซ้ำ", ""),
    "para_no_stop": ("ย่อหน้าสิ้นสุดโดยไม่มีจุด", ""),
    "para_no_cap": ("ย่อหน้าเริ่มต้นโดยไม่มีตัวพิมพ์ใหญ่", ""),
    "para_starts_dot": ("ย่อหน้าเริ่มต้นด้วยจุด?", ""),
    "punct_in_math": ("เครื่องหมายวรรคตอนในโหมดคณิตศาสตร์", "ย้าย ARG1 ออกจากโหมดคณิตศาสตร์"),
    "double_dot": ("จุดคู่", "จุดเดียวก็พอ"),
    "space_before_punct_math": ("ช่องว่างก่อนสิ้นสุดบล็อกคณิตศาสตร์", ""),
    "space_before_rparen": ("ช่องว่างก่อน )", ""),
    "proof_no_begin": ("\\end{proof} โดยไม่มี \\begin", "ลบตัวคั่นย่อหน้าก่อน \\end{proof}?"),
    "section_has_dot": ("ส่วนมีจุด", "ส่วนมักไม่ลงท้ายด้วยจุด"),
    "no_stop_def": ("ไม่มีจุดก่อน \\end{definition}", ""),
    "no_stop_end": ("ไม่มีจุดก่อน \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Thai rules."""
    return structural_rules(_MSGS) + common_academic_rules()
