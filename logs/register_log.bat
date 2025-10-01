:: Generato con ChatGPT

@echo off
setlocal enabledelayedexpansion

:: cartelle
set TMP_DIRECTORY=%TEMP%\trento_smart_move
set VENV_DIRECTORY=%TMP_DIRECTORY%\logs_venv
set SCRIPT_DIRECTORY=%~dp0

if not exist "%TMP_DIRECTORY%" (
    mkdir "%TMP_DIRECTORY%"
)

:: controlla se l'ambiente virtuale esiste
if exist "%VENV_DIRECTORY%\Scripts\activate.bat" (
    call "%VENV_DIRECTORY%\Scripts\activate.bat"
) else (
    python -m venv "%VENV_DIRECTORY%"
    call "%VENV_DIRECTORY%\Scripts\activate.bat"
    pip install -r "%SCRIPT_DIRECTORY%requirements.txt"
)

:: esegui lo script python con tutti gli argomenti
python "%SCRIPT_DIRECTORY%working_log.py" %*

:: disattiva il virtualenv
deactivate

endlocal
