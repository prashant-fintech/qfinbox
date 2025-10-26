@echo off
REM Development helper script for qfinbox (Windows)

if "%1"=="setup" goto setup
if "%1"=="format" goto format
if "%1"=="lint" goto lint
if "%1"=="type-check" goto type_check
if "%1"=="test" goto test
if "%1"=="test-cov" goto test_cov
if "%1"=="security" goto security
if "%1"=="pre-commit" goto pre_commit
if "%1"=="clean" goto clean
if "%1"=="build" goto build_pkg
if "%1"=="docs" goto docs
if "%1"=="all" goto all
if "%1"=="help" goto help
if "%1"=="" goto help

echo Unknown command: %1
echo Use 'dev.bat help' for usage information.
exit /b 1

:help
echo qfinbox Development Helper
echo ========================
echo.
echo Usage: dev.bat [COMMAND]
echo.
echo Commands:
echo   setup         Set up development environment
echo   format        Format code with ruff
echo   lint          Run linting with ruff
echo   type-check    Run mypy type checking
echo   test          Run tests with pytest
echo   test-cov      Run tests with coverage
echo   security      Run security checks
echo   pre-commit    Run all pre-commit hooks
echo   clean         Clean build artifacts and cache
echo   build         Build package distributions
echo   docs          Build documentation
echo   all           Run format, lint, type-check, test
echo   help          Show this help
exit /b 0

:setup
echo 🔧 Setting up development environment...
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install -e .
pre-commit install
pre-commit install --hook-type pre-push
echo ✅ Development environment ready!
exit /b 0

:format
echo 🎨 Formatting code with ruff...
ruff format src\ tests\
ruff check --fix src\ tests\
echo ✅ Code formatted!
exit /b 0

:lint
echo 🔍 Linting code with ruff...
ruff check src\ tests\
echo ✅ Linting complete!
exit /b 0

:type_check
echo 🔍 Running type checks with mypy...
mypy src\ --ignore-missing-imports
echo ✅ Type checking complete!
exit /b 0

:test
echo 🧪 Running tests...
pytest tests\ -v
echo ✅ Tests complete!
exit /b 0

:test_cov
echo 🧪 Running tests with coverage...
pytest tests\ -v --cov=qfinbox --cov-report=html --cov-report=term
echo 📊 Coverage report generated in htmlcov\
echo ✅ Tests with coverage complete!
exit /b 0

:security
echo 🔒 Running security checks...
echo Running bandit...
bandit -r src\
echo Running safety...
safety check
echo ✅ Security checks complete!
exit /b 0

:pre_commit
echo 🔧 Running pre-commit hooks...
pre-commit run --all-files
echo ✅ Pre-commit hooks complete!
exit /b 0

:clean
echo 🧹 Cleaning build artifacts...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info
if exist .pytest_cache rmdir /s /q .pytest_cache
if exist htmlcov rmdir /s /q htmlcov
if exist .coverage del .coverage
for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
del /s *.pyc 2>nul
echo ✅ Cleanup complete!
exit /b 0

:build_pkg
echo 📦 Building package...
python -m build
echo ✅ Package built in dist\
exit /b 0

:docs
echo 📚 Building documentation...
cd docs
make clean
make html
cd ..
echo 📖 Documentation built in docs\_build\html\
echo ✅ Documentation complete!
exit /b 0

:all
echo 🚀 Running full development workflow...
call :format
call :lint
call :type_check
call :test
echo 🎉 All checks passed!
exit /b 0
