#!/bin/bash

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .env

# Activate virtual environment
echo "Activating virtual environment..."
source .env/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

echo "Setup complete. Virtual environment is activated."