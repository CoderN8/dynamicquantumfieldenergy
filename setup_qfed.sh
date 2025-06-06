#!/bin/bash

echo "Setting up QFED environment..."
python3 -m venv qfed_env
source qfed_env/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete. Activate with: source qfed_env/bin/activate"