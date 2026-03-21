# lyxgc - Python Grammar Checker for LyX/LaTeX

Python port of the lyx-gc Perl grammar checker.

## Setup

```bash
cd py
pip install -e .
pip install pytest  # for tests
```

## Usage

```bash
python chktex.py myfile.tex
python chktex.py -v0 -o output.txt myfile.tex
python chktex.py -l "French (Canada)" myfile.tex
```

**Language selection** (priority: `-l/--lang` > `LYX_LANGUAGE` env > `LANG` env):
- `-l "English (USA)"` or `-l en_US` - English rules
- `-l "French"` or `-l fr` - French rules
- Supported LyX languages: Afrikaans, Albanian, Arabic, Armenian, Basque, etc. English and French variants use the same rules (no duplication). Other languages use no custom rules (LanguageTool still runs).

## Tests

```bash
pytest tests/ -v
```

## Structure

- `lyxgc/` - main package
  - `tokenizer.py` - LaTeX tokenization
  - `rules.py` - setDiff, GenerateVowelRegex, SimpleRule
  - `engine.py` - FindErrors, rule application
  - `report.py` - LyX-compatible error output
  - `lang/en.py`, `lang/fr.py` - language rules
  - `lang/registry.py` - LyX language names and locale → rule module mapping
  - `languagetool.py` - LanguageTool integration
  - `chktex_parse.py`, `lacheck_parse.py` - external tool parsers
- `chktex.py` - CLI entry point
- `run_jlanguagetool.py` - LanguageTool runner (background)
