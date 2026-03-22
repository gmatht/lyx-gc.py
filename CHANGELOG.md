# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0dev2] - 2025-03-21

### Added

- `install_and_demo.py` - one-command install from release (Linux/macOS)
- `install_and_demo.ps1` - one-command install from release (Windows)
- `sample_errors.lyx` - demo document with deliberate errors for Tools > Check Text

## [0.1.0dev1] - 2025-03-21

### Added

- Python port of lyx-gc (LyX/LaTeX grammar checker)
- Grammar rules from JSON data files for 60+ languages
- Integration with LanguageTool, lacheck, and system ChkTeX
- `check_deps.py` - scan and optionally install soft dependencies
- `run_lyx.py` - launch LyX with our chktex in PATH
- LyX-compatible error output formats (-v0, -v1, -v3)

### Notes

- Maintains bug-for-bug compatibility with the Perl version during development
- Soft dependencies (LyX, lacheck, chktex, LanguageTool, Java) are optional but enable more error checks
