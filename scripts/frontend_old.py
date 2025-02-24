import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import joblib  

def load_model(model_path):
    """Load machine learning model with robust error handling"""
    try:
        try:
            model_data = joblib.load(model_path)
        except Exception:
            with open(model_path, 'rb') as f:
                model_data = pickle.load(f)
        
        if isinstance(model_data, dict):
            if 'rf_model' in model_data:
                required_keys = ['rf_model', 'gb_model', 'meta_model', 'scaler']
                if all(key in model_data for key in required_keys):
                    return model_data
            elif 'model' in model_data and 'scaler' in model_data:
                return model_data
        
        return {'model': model_data, 'scaler': None}
    
    except Exception as e:
        st.error(f"Error loading model from {model_path}: {e}")
        st.error("Possible causes:\n"
                 "- Incompatible Python versions\n"
                 "- Corrupted model file\n"
                 "- Insufficient memory")
        return None

def predict_loan_funding(model_data, loan_amount, term_in_months, lender_count):
    """Predict loan funding probability with enhanced error handling"""
    if not model_data:
        st.error("Invalid model data")
        return None
    
    try:
        if 'rf_model' in model_data and 'gb_model' in model_data and 'meta_model' in model_data:
            rf_model = model_data['rf_model']
            gb_model = model_data['gb_model']
            meta_model = model_data['meta_model']
            scaler = model_data.get('scaler')
            
            input_data = np.array([[loan_amount, term_in_months, lender_count]])
            
            if scaler is not None:
                input_scaled = scaler.transform(input_data)
            else:
                input_scaled = input_data
            
            rf_prob = rf_model.predict_proba(input_scaled)[0][1]
            gb_prob = gb_model.predict_proba(input_scaled)[0][1]
            
            meta_features = np.array([[rf_prob, gb_prob]])
            ensemble_prob = meta_model.predict_proba(meta_features)[0][1]
            
            return ensemble_prob
        
        model = model_data.get('model') or model_data
        scaler = model_data.get('scaler')
        
        input_data = np.array([[loan_amount, term_in_months, lender_count]])
        
        if scaler is not None:
            input_scaled = scaler.transform(input_data)
        else:
            input_scaled = input_data
        
        prob_funded = model.predict_proba(input_scaled)[0][1]
        return prob_funded
    
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

def load_kiva_data():
    """Load Nityartha loans dataset"""
    try:
        df = pd.read_csv('data/kiva_loans.csv', low_memory=False)
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None

def main():
    st.set_page_config(page_title="Nityartha Loan Analysis", page_icon=":bank:", layout="wide")
    
    st.sidebar.title("Nityartha Loan Analysis")
    page = st.sidebar.radio("Navigate", 
        ["Loan Funding Predictor", "Data Overview", "Loan Distribution", "About"])
    
    try:
        rf_model = load_model('models/saved_models/kiva_rf_model.pkl')
        ensemble_model = load_model('models/saved_models/kiva_ensemble_model.pkl')
    except Exception as e:
        st.error(f"Error loading models: {e}")
        rf_model = None
        ensemble_model = None
    
    if page == "Loan Funding Predictor":
        st.title("Loan Funding Probability Predictor")
        
        if rf_model and ensemble_model:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=1000, step=100)
            with col2:
                term_in_months = st.number_input("Loan Term (Months)", min_value=1, value=12, step=1)
            with col3:
                lender_count = st.number_input("Number of Potential Lenders", min_value=0, value=10, step=1)
            
            if st.button("Predict Funding Probability"):
                rf_prob = predict_loan_funding(rf_model, loan_amount, term_in_months, lender_count)
                ensemble_prob = predict_loan_funding(ensemble_model, loan_amount, term_in_months, lender_count)
                
                if rf_prob is not None and ensemble_prob is not None:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("Random Forest Model", 
                                  f"{rf_prob*100:.2f}%")
                    with col2:
                        st.metric("Ensemble Model", 
                                  f"{ensemble_prob*100:.2f}%", 
                                  delta_color="inverse")
                    
                    st.write("### Interpretation")
                    if rf_prob > 0.7:
                        st.success("High probability of loan funding. Looks promising!")
                    elif rf_prob > 0.4:
                        st.warning("Moderate probability of loan funding. Some uncertainty.")
                    else:
                        st.error("Low probability of loan funding. High risk.")
                else:
                    st.error("Unable to predict loan funding probability.")
        else:
            st.error("Models not loaded. Please check model files.")
    
    elif page == "Data Overview":
        st.title("Nityartha Loans Data Overview")
        
        df = load_kiva_data()
        
        if df is not None:
            st.write("### Dataset Information")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Total Loans", len(df))
                st.metric("Number of Unique Countries", df['country'].nunique())
            
            with col2:
                st.metric("Average Loan Amount", f"${df['loan_amount'].mean():,.2f}")
                st.metric("Median Loan Amount", f"${df['loan_amount'].median():,.2f}")
            
            st.write("### Loan Distribution by Sector")
            sector_counts = df['sector'].value_counts()
            
            fig, ax = plt.subplots(figsize=(10, 6))
            sector_counts.plot(kind='bar', ax=ax)
            plt.title("Loan Distribution by Sector")
            plt.xlabel("Sector")
            plt.ylabel("Number of Loans")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
    
    elif page == "Loan Distribution":
        st.title("Loan Distribution Analysis")
        
        df = load_kiva_data()
        
        if df is not None:
            st.write("### Loan Amount Distribution")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(df['loan_amount'], kde=True, ax=ax)
            plt.title("Distribution of Loan Amounts")
            plt.xlabel("Loan Amount")
            plt.ylabel("Frequency")
            plt.tight_layout()
            st.pyplot(fig)
            
            st.write("### Loan Amounts by Top 10 Countries")
            top_countries = df['country'].value_counts().head(10).index
            country_loans = df[df['country'].isin(top_countries)]
            
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.boxplot(x='country', y='loan_amount', data=country_loans, ax=ax)
            plt.title("Loan Amounts by Top 10 Countries")
            plt.xlabel("Country")
            plt.ylabel("Loan Amount")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
    
    elif page == "About":
        st.title("About Nityartha Loan Analysis")
        
        st.markdown("""
        ### Nityartha Loan Analysis Project
        
        #### Project Overview
        This application provides insights into Nityartha loan data using machine learning models.
        
        #### Features
        - Loan Funding Probability Predictor
        - Data Overview
        - Loan Distribution Analysis
        
        #### Machine Learning Models
        - Random Forest Classifier
        - Ensemble Model
        
        #### Data Source
        Nityartha Loans Dataset
        
        #### Created by
        Nityartha Team
        """)

if __name__ == "__main__":
    main()