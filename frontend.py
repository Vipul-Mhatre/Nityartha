import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

def load_model(model_path):
    """Load the saved model and scaler"""
    with open(model_path, 'rb') as f:
        model_data = pickle.load(f)
    return model_data

def predict_loan_funding(model_data, loan_amount, term_in_months, lender_count):
    """Predict loan funding probability"""
    scaler = model_data['scaler']
    model = model_data['model']
    
    # Prepare input data
    input_data = np.array([[loan_amount, term_in_months, lender_count]])
    input_scaled = scaler.transform(input_data)
    
    # Predict probability
    prob_funded = model.predict_proba(input_scaled)[0][1]
    return prob_funded

def load_kiva_data():
    """Load Nityartha loans dataset"""
    try:
        df = pd.read_csv('data/kiva_loans.csv', low_memory=False)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    st.set_page_config(page_title="Nityartha Loan Analysis", page_icon=":bank:", layout="wide")
    
    # Sidebar for navigation
    st.sidebar.title("Nityartha Loan Analysis")
    page = st.sidebar.radio("Navigate", 
        ["Loan Funding Predictor", "Dataset Overview", "Loan Distribution", "About"])
    
    # Load models
    try:
        rf_model = load_model('models/saved_models/kiva_rf_model.pkl')
        ensemble_model = load_model('models/saved_models/kiva_ensemble_model.pkl')
    except Exception as e:
        st.error(f"Error loading models: {e}")
        rf_model = None
        ensemble_model = None
    
    if page == "Loan Funding Predictor":
        st.title("Loan Funding Probability Predictor")
        
        if rf_model:
            # Input features
            col1, col2, col3 = st.columns(3)
            
            with col1:
                loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=1000, step=100)
            
            with col2:
                term_in_months = st.number_input("Loan Term (Months)", min_value=1, value=12, step=1)
            
            with col3:
                lender_count = st.number_input("Number of Potential Lenders", min_value=0, value=10, step=1)
            
            if st.button("Predict Funding Probability"):
                rf_prob = predict_loan_funding(rf_model, loan_amount, term_in_months, lender_count)
                
                ensemble_prob = None
                if ensemble_model:
                    ensemble_prob = predict_loan_funding(ensemble_model, loan_amount, term_in_months, lender_count)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Random Forest Model", 
                              f"{rf_prob*100:.2f}%", 
                              delta_color="inverse")
                
                if ensemble_prob is not None:
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
            st.error("Models not loaded. Please check model files.")
    
    elif page == "Dataset Overview":
        st.title("Nityartha Loans Dataset Overview")
        
        df = load_kiva_data()
        
        if df is not None:
            st.write("### Dataset Information")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Total Loans", len(df))
                st.metric("Total Loan Amount", f"${df['loan_amount'].sum():,.2f}")
            
            with col2:
                st.metric("Average Loan Amount", f"${df['loan_amount'].mean():,.2f}")
                st.metric("Median Loan Amount", f"${df['loan_amount'].median():,.2f}")
            
            st.write("### Loan Distribution by Sector")
            sector_counts = df['sector'].value_counts()
            
            fig, ax = plt.subplots(figsize=(10, 6))
            sector_counts.plot(kind='bar', ax=ax)
            plt.title("Number of Loans by Sector")
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
            plt.xlabel("Loan Amount ($)")
            plt.ylabel("Frequency")
            plt.tight_layout()
            st.pyplot(fig)
            
            st.write("### Loan Amounts by Top 10 Countries")
            top_countries = df['country'].value_counts().head(10).index
            country_loans = df[df['country'].isin(top_countries)]
            
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.boxplot(x='country', y='loan_amount', data=country_loans, ax=ax)
            plt.title("Loan Amounts by Country")
            plt.xlabel("Country")
            plt.ylabel("Loan Amount ($)")
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
        - Dataset Overview
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
