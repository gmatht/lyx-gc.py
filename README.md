# lyxgc - Python Grammar Checker for LyX/LaTeX

Python port of the lyx-gc Perl grammar checker.

## Quick Start

**Linux / macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/gmatht/lyx-gc.py/master/install_and_demo.py | python3
-o install_and_demo.py
python3 install_and_demo.py
```

**Windows (PowerShell):**
```powershell
curl -fsSL -o install_and_demo.ps1 https://raw.githubusercontent.com/gmatht/lyx-gc.py/master/install_and_demo.ps1
.\install_and_demo.ps1
```

Then use **Tools > Check Text** in LyX on the sample document.

## Install from release (Linux/macOS/Windows)

Quick install from GitHub release tarball/zip: downloads lyx-gc, runs dependency check, and launches LyX with a sample document.

**Linux / macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/gmatht/lyx-gc.py/master/install_and_demo.py -o install_and_demo.py
python install_and_demo.py
```

**Windows (PowerShell):**
```powershell
curl -fsSL -o install_and_demo.ps1 https://raw.githubusercontent.com/gmatht/lyx-gc.py/master/install_and_demo.ps1
.\install_and_demo.ps1
```

The sample document (`sample_errors.lyx`) prompts you to try **Tools > Check Text** and contains deliberate errors (internal rules, ChkTeX, lacheck, LanguageTool).

### Security notes

**curl (all platforms):** Use `-f` (fail on HTTP errors), `-s` (silent), `-L` (follow redirects), and HTTPS. Download to a file first (`-o`) so you can inspect the script before running.

**PowerShell (Windows):** Downloaded scripts are often blocked (Zone.Identifier). To run: right‑click the file → Properties → Unblock; or in PowerShell: `Unblock-File .\install_and_demo.ps1`. You may need `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` (one-time) if scripts are disabled. Or run one-off without changing policy: `powershell -ExecutionPolicy Bypass -File .\install_and_demo.ps1`.

## Setup (from source)

```bash
cd py
pip install -e .
pip install pytest  # for tests
```

### Checking soft dependencies

LyX, lacheck, chktex, and LanguageTool are optional; they allow finding more errors.
Run the checker to scan for them:

```bash
python check_deps.py              # Report status, offer to install missing
python check_deps.py --no-install  # Only report status
python check_deps.py --all        # Install all missing (may prompt for sudo)
```

Supported on Linux, WSL, macOS, and Windows (manual install instructions on Windows).

## Running LyX with lyx-gc

LyX must find our **chktex** (not the system one). The executable must be named exactly `chktex`; we use `chktex.py` for the implementation and `py/bin/chktex` + `py/bin/chktex.bat` as wrappers.

**Option 1 (recommended):** Run LyX via our launcher so our chktex is first in PATH:

```bash
python run_lyx.py
python run_lyx.py mydoc.lyx
```

**Option 2:** Add `py/bin` to PATH *before* system directories (e.g. in `~/.bashrc`):

```bash
export PATH="/path/to/lyx-gc/py/bin:$PATH"
```

Then start LyX as usual; Tools → Check Text will use our grammar checker.

## Usage (standalone checker)

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
  - `lang/` - language rules (JSON data in `lang/data/*.json`) and registry
  - `languagetool.py` - LanguageTool integration
  - `chktex_parse.py`, `lacheck_parse.py` - external tool parsers
- `chktex.py` - CLI entry point (implementation)
- `bin/chktex` - Wrapper named "chktex" for LyX (Unix)
- `bin/chktex.bat`, `bin/chktex.cmd` - Same for Windows
- `run_jlanguagetool.py` - LanguageTool runner (background)
