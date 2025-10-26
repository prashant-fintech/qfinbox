@echo off
REM Windows batch script for setting up qfinbox development environment

echo Setting up qfinbox development environment...

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip setuptools wheel

REM Install development dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Install package in development mode
echo Installing qfinbox in development mode...
pip install -e .

REM Install pre-commit hooks
echo Installing pre-commit hooks...
pre-commit install

echo ✅ Development environment setup complete!
echo To activate the environment, run: venv\Scripts\activate.bat

pause
