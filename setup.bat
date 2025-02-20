@echo off
echo Setting up Nityartha Loan Analysis Project

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Train models
python app.py

echo Project setup complete!
echo To run the frontend, use: streamlit run frontend.py
