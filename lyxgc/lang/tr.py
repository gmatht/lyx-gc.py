"""Turkish grammar rules - LaTeX structural rules with Turkish messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Boş matematik bloğu", ""),
    "macro_no_brace": ("Makro {} olmadan", "Makrodan sonra {} gerekebilir."),
    "no_fullstop_after_cite": ("Paragraf sonunda alıntıdan sonra nokta yok", "Nokta eksik olabilir."),
    "no_space_after_cite": ("Alıntıdan sonra boşluk yok", ""),
    "no_space_before_cite": ("Alıntıdan önce boşluk yok", ""),
    "uline_starts_early": ("Alt çizgi çok erken başlıyor", ""),
    "uline_ends_late": ("Alt çizgi çok geç bitiyor", ""),
    "space_before_footnote": ("Dipnottan önce boşluk", ""),
    "footnote_period_comma": ("Dipnottan sonra nokta/virgül", "Dipnot tüm cümleye atıfta bulunuyorsa, noktadan sonraya koyun."),
    "double_punct": ("Çift noktalama", ""),
    "implies_in_proof": ("Kanıtta \\implies kullanımı", "Kanıt yönü için \\Longrightarrow kullanın."),
    "no_space_after_ref": ("Referanstan sonra boşluk yok", ""),
    "single_char": ("Tek karakter", "Tek karakter genellikle anlam ifade etmez."),
    "empty_begin_end": ("Boş begin/end bloğu", ""),
    "proof_not_newline": ("Kanıt yeni satırda başlamıyor", "Teorem ile kanıt arasına paragraf ayırıcı ekleyin (LyX'te Enter)."),
    "no_space_ref_left": ("Referansın solunda boşluk yok", "Belki referanstan önce kesilmez boşluk (~)?"),
    "no_space_ref_right": ("Referansın sağında boşluk yok", "Belki referanstan sonra kesilmez boşluk (~)?"),
    "too_many_dots": ("Çok fazla nokta", "Neden birden fazla '.'?"),
    "space_cite_punct": ("Alıntı ile noktalama arasında boşluk", ""),
    "space_after_period_cap": ("Nokta ile büyük harf arasında boşluk eksik", ""),
    "space_after_period_word": ("Nokta ile kelime arasında boşluk eksik", ""),
    "textquotedbl": ("\\textquotedbl yanlış kullanımı", "`` veya '' kullanın."),
    "math_punct": ("Matematik bloğu ile noktalama arasında boşluk", ""),
    "cap_after_math": ("Matematik bloğundan sonra büyük harf", "Neden matematik bloğundan sonra büyük harf?"),
    "equals_outside_math": ("Matematik bloğunun dışında eşittir işareti", "'=' matematik bloğunun içinde olmalı."),
    "no_space_before_math": ("Matematik bloğundan önce boşluk yok", ""),
    "no_space_before_cite": ("Alıntıdan önce boşluk yok", ""),
    "footnote_no_stop": ("Noktasız dipnot", ""),
    "no_space_after_math": ("Matematik bloğundan sonra boşluk yok", ""),
    "no_space_before_macro": ("Makrodan önce boşluk yok", ""),
    "no_space_after_macro": ("Makrodan sonra boşluk yok", ""),
    "colon_in_math": (": matematik modunda", "Fonksiyonları tanımlamak için \\colon kullanın."),
    "ugly_fraction": ("Çirkin kesir", r"\\nicefrac{ARG1}{ARG2} kullanın."),
    "too_many_zeros": ("Ayırıcı olmadan çok fazla sıfır", ""),
    "duplicated_word": ("Yinelenen kelime", ""),
    "para_no_stop": ("Paragraf nokta olmadan bitiyor", ""),
    "para_no_cap": ("Paragraf büyük harf olmadan başlıyor", ""),
    "para_starts_dot": ("Paragraf noktayla mı başlıyor?", ""),
    "punct_in_math": ("Matematik modunda noktalama", "ARG1'i matematik modunun dışına taşıyın."),
    "double_dot": ("Çift nokta", "Tek nokta yeterli."),
    "space_before_punct_math": ("Matematik bloğu sonundan önce boşluk", ""),
    "space_before_rparen": (") öncesinde boşluk", ""),
    "proof_no_begin": ("\\end{proof} \\begin olmadan", "\\end{proof} öncesindeki paragraf ayırıcıyı kaldıralım mı?"),
    "section_has_dot": ("Noktalı bölüm", "Bölümler genellikle noktayla bitmez."),
    "no_stop_def": ("\\end{definition} öncesinde nokta yok", ""),
    "no_stop_end": ("\\end{...} öncesinde nokta yok", ""),
}


def generate_error_types() -> list:
    """Return Turkish rules."""
    return structural_rules(_MSGS) + common_academic_rules()
