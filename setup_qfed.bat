@echo off
echo Setting up QFED environment...

python -m venv qfed_env
call qfed_env\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete. To activate later, run:
echo call qfed_env\Scripts\activate.bat