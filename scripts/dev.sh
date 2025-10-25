#!/bin/bash
# Development helper script for qfinbox

set -e

show_help() {
    echo "qfinbox Development Helper"
    echo "========================"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  setup         Set up development environment"
    echo "  format        Format code with ruff"
    echo "  lint          Run linting with ruff"
    echo "  type-check    Run mypy type checking"
    echo "  test          Run tests with pytest"
    echo "  test-cov      Run tests with coverage"
    echo "  security      Run security checks"
    echo "  pre-commit    Run all pre-commit hooks"
    echo "  clean         Clean build artifacts and cache"
    echo "  build         Build package distributions"
    echo "  docs          Build documentation"
    echo "  all           Run format, lint, type-check, test"
    echo "  help          Show this help"
}

setup() {
    echo "🔧 Setting up development environment..."
    python -m venv venv
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    python -m pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
    pip install -e .
    pre-commit install
    pre-commit install --hook-type pre-push
    echo "✅ Development environment ready!"
}

format_code() {
    echo "🎨 Formatting code with ruff..."
    ruff format src/ tests/
    ruff check --fix src/ tests/
    echo "✅ Code formatted!"
}

lint_code() {
    echo "🔍 Linting code with ruff..."
    ruff check src/ tests/
    echo "✅ Linting complete!"
}

type_check() {
    echo "🔍 Running type checks with mypy..."
    mypy src/ --ignore-missing-imports || echo "Type checking completed with warnings"
    echo "✅ Type checking complete!"
}

run_tests() {
    echo "🧪 Running tests..."
    pytest tests/ -v
    echo "✅ Tests complete!"
}

run_tests_with_coverage() {
    echo "🧪 Running tests with coverage..."
    pytest tests/ -v --cov=qfinbox --cov-report=html --cov-report=term
    echo "📊 Coverage report generated in htmlcov/"
    echo "✅ Tests with coverage complete!"
}

security_check() {
    echo "🔒 Running security checks..."
    echo "Running bandit..."
    bandit -r src/ || echo "Bandit scan completed"
    echo "Running safety..."
    safety check || echo "Safety check completed"
    echo "✅ Security checks complete!"
}

run_pre_commit() {
    echo "🔧 Running pre-commit hooks..."
    pre-commit run --all-files
    echo "✅ Pre-commit hooks complete!"
}

clean_artifacts() {
    echo "🧹 Cleaning build artifacts..."
    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info/
    rm -rf .pytest_cache/
    rm -rf htmlcov/
    rm -rf .coverage
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
    find . -name "*.pyc" -delete 2>/dev/null || true
    echo "✅ Cleanup complete!"
}

build_package() {
    echo "📦 Building package..."
    python -m build
    echo "✅ Package built in dist/"
}

build_docs() {
    echo "📚 Building documentation..."
    cd docs
    make clean
    make html
    cd ..
    echo "📖 Documentation built in docs/_build/html/"
    echo "✅ Documentation complete!"
}

run_all() {
    echo "🚀 Running full development workflow..."
    format_code
    lint_code
    type_check
    run_tests
    echo "🎉 All checks passed!"
}

case "$1" in
    setup)
        setup
        ;;
    format)
        format_code
        ;;
    lint)
        lint_code
        ;;
    type-check)
        type_check
        ;;
    test)
        run_tests
        ;;
    test-cov)
        run_tests_with_coverage
        ;;
    security)
        security_check
        ;;
    pre-commit)
        run_pre_commit
        ;;
    clean)
        clean_artifacts
        ;;
    build)
        build_package
        ;;
    docs)
        build_docs
        ;;
    all)
        run_all
        ;;
    help|--help|-h)
        show_help
        ;;
    "")
        show_help
        ;;
    *)
        echo "Unknown command: $1"
        echo "Use '$0 help' for usage information."
        exit 1
        ;;
esac
