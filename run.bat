@echo off

REM Function to activate virtual environment
if exist .venv\Scripts\activate (
    echo Activating virtual environment...
    call .venv\Scripts\activate
) else (
    echo Virtual environment does not exist. Please run setup.bat to create it.
    exit /b 1
)

REM Execute Python script
python run.py

REM Deactivate the virtual environment
deactivate
