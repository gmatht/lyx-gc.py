@echo off
REM Wrapper: LyX must find "chktex" (this file) not chktex.py.
REM Fallback for environments that prefer .cmd over .bat
set "BIN_DIR=%~dp0"
set "CHKTEX_PY=%BIN_DIR%..\chktex.py"
python "%CHKTEX_PY%" %*
