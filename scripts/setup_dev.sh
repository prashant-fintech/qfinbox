#!/bin/bash
# Setup script for qfinbox development environment

echo "Setting up qfinbox development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip setuptools wheel

# Install development dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Install package in development mode
echo "Installing qfinbox in development mode..."
pip install -e .

# Install pre-commit hooks
echo "Installing pre-commit hooks..."
pre-commit install

echo "✅ Development environment setup complete!"
echo "To activate the environment, run:"
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo "  venv\\Scripts\\activate"
else
    echo "  source venv/bin/activate"
fi
