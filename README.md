# Nityartha Loan Analysis AI Agent 

## Overview
This project provides a comprehensive analysis of Nityartha loan data using machine learning techniques. The application includes a Streamlit-based frontend for interactive exploration and prediction.

## Features
- Loan Funding Probability Predictor
- Data Overview Visualization
- Loan Distribution Analysis
- Machine Learning Models:
  - Random Forest Classifier
  - Ensemble Model

## Prerequisites
- Python 3.8+
- pip

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
1. Train the models:
```bash
python app.py
```

2. Launch the Streamlit frontend:
```bash
streamlit run frontend.py
```

## Project Structure
- `app.py`: Model training script
- `frontend.py`: Streamlit web application
- `data/`: Contains input datasets
- `models/`: Saved machine learning models
- `requirements.txt`: Project dependencies

## Machine Learning Approach
- Preprocessed Kiva loans dataset
- Created binary classification model for loan funding prediction
- Used Random Forest and Ensemble learning techniques

## Visualizations
- Loan amount distribution
- Sector-wise loan distribution
- Country-level loan analysis

## Contributing
Contributions are welcome! Please submit pull requests or open issues.
