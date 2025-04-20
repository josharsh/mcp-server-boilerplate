#!/bin/bash

# Development setup script for MCP server

# Check if Python 3.11+ is installed
python_version=$(python --version 2>&1 | awk '{print $2}')
python_major=$(echo $python_version | cut -d. -f1)
python_minor=$(echo $python_version | cut -d. -f2)

if [ "$python_major" -lt 3 ] || [ "$python_major" -eq 3 -a "$python_minor" -lt 11 ]; then
  echo "Error: Python 3.11 or higher is required. Found Python $python_version"
  exit 1
fi

echo "✅ Python version check passed: $python_version"

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
  echo "Installing uv package manager..."
  pip install uv
else
  echo "✅ uv is already installed"
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
  echo "Creating .env file from example..."
  cp .env.example .env
  echo "⚠️ Please update the .env file with your actual credentials"
else
  echo "✅ .env file already exists"
fi

# Create app directory if it doesn't exist
if [ ! -d app ]; then
  echo "Creating app directory..."
  mkdir -p app
fi

# Create __init__.py if it doesn't exist
if [ ! -f app/__init__.py ]; then
  echo "Creating app/__init__.py..."
  echo '# Makes the app directory a proper Python package' > app/__init__.py
  echo '__version__ = "0.1.0"' >> app/__init__.py
fi

# Install dependencies using uv
echo "Installing dependencies with uv..."
uv pip install -r requirements.txt
uv pip install mcp[cli]>=1.6.0

echo "✅ Setup complete! You can now run the application with:"
echo "python main.py" 