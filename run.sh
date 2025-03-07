#!/bin/bash

# Function to activate virtual environment
activate_venv() {
    if [ -d ".env" ]; then
        echo "Activating virtual environment..."
        source .env/bin/activate
    else
        echo "Virtual environment does not exist. Please run setup.sh to create it."
        exit 1
    fi
}

# Check if virtual environment exists and activate it
activate_venv

# Execute Python script
python3 run.py

# Deactivate the virtual environment
deactivate