import streamlit as st
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from datetime import datetime

# Set page configuration for a wide, professional layout
st.set_page_config(
    page_title="AI-Powered Micro-Finance Platform",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a modern dark blue theme for inputs and outputs
st.markdown("""
    <style>
    /* General Styling */
    body {
        background-color: #f8f9fa;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    .main {background-color: #f8f9fa;}
    h1, h2, h3, h4 {color: #2c3e50; font-weight: 700;}

    /* Dark Blue Input Styling */
    .stTextInput>div>input,
    .stTextArea textarea,
    .stSelectbox>div>select,
    .stNumberInput>div>input {
        background-color: #003366;
        color: white;
        border-radius: 8px;
        border: 1px solid #ced4da;
        padding: 10px;
    }
    .stSlider>div {background-color: #e9ecef; border-radius: 8px;}

    /* Form Styling */
    .stForm {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    .stAlert {
        border-radius: 8px;
        padding: 15px;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }

    /* Dark Blue Output Styling: target pre elements often used for JSON/code outputs */
    pre {
        background-color: #003366 !important;
        color: white !important;
        padding: 10px;
        border-radius: 8px;
    }

    /* Custom Header */
    .header {
        padding: 10px 0;
        text-align: center;
        background-color: #007bff;
        color: white;
        margin-bottom: 20px;
    }
    .header h1 {
        margin: 0;
        font-size: 2.5rem;
    }

    /* Custom Elements */
    .section-header {
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .feature-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        padding: 20px;
        color: #6c757d;
        font-size: 14px;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="header"><h1>AI-Powered Micro-Finance Platform</h1></div>', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("Explore the platform's features below:")

# Updated pages list including admin operations
pages = [
    "Home", 
    "Creditworthiness Assessment", 
    "Compliance Verification", 
    "Behavioral Analysis",
    "ESG Tracking", 
    "Loan Recommendations", 
    "Dashboard",
    "Train Models",
    "Set Compliance Rule",
    "Enroll Biometric",
    "User Guide", 
    "About Us",
    "Contact Us", 
    "FAQ", 
    "Privacy Policy", 
    "Terms of Service", 
    "Blog", 
    "Support"
]
page = st.sidebar.selectbox("Go to", pages, index=0)

# Helper function for API calls
def api_call(endpoint, data):
    url = f"http://127.0.0.1:5000{endpoint}"
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Error: {response.json().get('error', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Connection Error: {str(e)}")
        return None

# Progress bar for loading simulation
def show_loading():
    with st.spinner("Processing your request..."):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        progress_bar.empty()

# Authentication Simulation (basic)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in and page not in ["Home", "About Us", "Contact Us", "FAQ", "Privacy Policy", "Terms of Service", "Blog", "User Guide"]:
    st.sidebar.subheader("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username == "user" and password == "pass":  # Dummy credentials
            st.session_state.logged_in = True
            st.sidebar.success("Logged in successfully!")
        else:
            st.sidebar.error("Invalid credentials")
    st.stop()

# Logout option
if st.session_state.logged_in:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.sidebar.success("Logged out successfully!")

# Page Definitions

## Home Page
if page == "Home":
    st.title("Welcome to the AI-Powered Micro-Finance Platform")
    st.markdown("Empowering financial inclusion with cutting-edge AI technology.")
    st.image("https://via.placeholder.com/1200x400.png?text=Revolutionizing+Micro-Finance", use_column_width=True)
    
    st.markdown("### Why Choose Us?")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="feature-card"><h3>AI-Driven Insights</h3><p>Leverage advanced analytics for smarter decisions.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="feature-card"><h3>Secure & Compliant</h3><p>Ensure compliance with decentralized KYC and AML.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="feature-card"><h3>Sustainable Finance</h3><p>Track ESG metrics for ethical investments.</p></div>', unsafe_allow_html=True)
    
    st.markdown("### Get Started")
    st.write("Navigate using the sidebar to explore our features and operations.")

## Creditworthiness Assessment Page
elif page == "Creditworthiness Assessment":
    st.title("Creditworthiness Assessment")
    st.markdown("Assess your credit profile with AI-powered precision.")
    
    with st.form("credit_form"):
        st.markdown('<h3 class="section-header">Input Your Financial Data</h3>', unsafe_allow_html=True)
        data = [st.number_input(f"Financial Feature {i+1}", value=0.0, step=0.1) for i in range(5)]
        use_social_data = st.checkbox("Include Social Network Data")
        if use_social_data:
            nodes = [st.number_input(f"Social Node {i+1}", value=0.0, step=0.1) for i in range(5)]
            connections = [[st.number_input(f"Connection {i+1}-{j+1}", value=0.0, step=0.1, key=f"conn_{i}_{j}") for j in range(5)] for i in range(5)]
            social_data = {'nodes': nodes, 'connections': connections}
        else:
            social_data = None
        submit = st.form_submit_button("Assess Now")
        
        if submit:
            show_loading()
            result = api_call("/assess_creditworthiness", {"data": data, "social_data": social_data})
            if result:
                st.success("Assessment Complete!")
                st.markdown("### Results")
                st.json(result)

## Compliance Verification Page
elif page == "Compliance Verification":
    st.title("Compliance Verification")
    st.markdown("Ensure regulatory compliance with automated verification.")
    
    with st.form("compliance_form"):
        st.markdown('<h3 class="section-header">Input Compliance Data</h3>', unsafe_allow_html=True)
        user_data = st.text_input("User Data / ID")
        document_text = st.text_area("Document Text", height=150)
        transaction_data = [st.number_input(f"Transaction Feature {i+1}", value=0.0, step=0.1) for i in range(5)]
        bio_data_str = st.text_input("Biometric Data (optional, comma-separated numbers)", value="")
        contract_id = st.text_input("Contract ID (optional)")
        conditions_str = st.text_area("Conditions (JSON format, optional)", value="{}", height=100)
        submit = st.form_submit_button("Verify Compliance")
        
        if submit:
            show_loading()
            bio_data = [float(x.strip()) for x in bio_data_str.split(",")] if bio_data_str else None
            try:
                conditions = json.loads(conditions_str) if conditions_str else None
            except json.JSONDecodeError:
                st.error("Invalid JSON format for conditions.")
                conditions = None
            data = {
                "user_data": user_data,
                "document_text": document_text,
                "transaction_data": transaction_data,
                "bio_data": bio_data,
                "contract_id": contract_id,
                "conditions": conditions
            }
            result = api_call("/verify_compliance", data)
            if result:
                st.success("Verification Complete!")
                st.markdown("### Results")
                st.json(result)

## Behavioral Analysis Page
elif page == "Behavioral Analysis":
    st.title("Behavioral Analysis")
    st.markdown("Gain insights into user behavior with AI-driven analysis.")
    
    with st.form("behavior_form"):
        st.markdown('<h3 class="section-header">Input Behavioral Features</h3>', unsafe_allow_html=True)
        features = [st.number_input(f"Behavioral Feature {i+1}", value=0.0, step=0.1) for i in range(3)]
        submit = st.form_submit_button("Analyze Behavior")
        
        if submit:
            show_loading()
            result = api_call("/analyze_behavior", {"features": features})
            if result:
                st.success("Analysis Complete!")
                st.markdown("### Results")
                st.json(result)

## ESG Tracking Page
elif page == "ESG Tracking":
    st.title("ESG Tracking & Scoring")
    st.markdown("Monitor and optimize your environmental, social, and governance impact.")
    
    with st.form("esg_form"):
        st.markdown('<h3 class="section-header">Input ESG Data</h3>', unsafe_allow_html=True)
        source_data = {
            "source1": [st.number_input(f"Source 1 Value {i+1}", value=0.0, step=0.1) for i in range(3)],
            "source2": [st.number_input(f"Source 2 Value {i+1}", value=0.0, step=0.1) for i in range(3)]
        }
        factors = [st.number_input(f"ESG Factor {i+1}", value=0.0, step=0.1) for i in range(3)]
        impact_data = [st.number_input(f"Impact Data {i+1}", value=0.0, step=0.1) for i in range(3)]
        risk = st.slider("Risk Level", 0.0, 1.0, 0.5, step=0.01)
        submit = st.form_submit_button("Track ESG")
        
        if submit:
            show_loading()
            data = {"source_data": source_data, "factors": factors, "impact_data": impact_data, "risk": risk}
            result = api_call("/track_esg", data)
            if result:
                st.success("ESG Tracking Complete!")
                st.markdown("### Results")
                st.json(result)
                if "visualization" in result:
                    df = pd.DataFrame(result["visualization"].items(), columns=["Source", "Value"])
                    st.bar_chart(df.set_index("Source"))

## Loan Recommendations Page
elif page == "Loan Recommendations":
    st.title("Loan Recommendations")
    st.markdown("Get personalized loan options and financial guidance.")
    
    with st.form("loan_form"):
        st.markdown('<h3 class="section-header">Input Loan Data</h3>', unsafe_allow_html=True)
        user_id = st.number_input("User ID", min_value=0, max_value=4, step=1)
        score = st.slider("Credit Score", 0.0, 1.0, 0.5, step=0.01)
        risk = st.slider("Risk Level", 0.0, 1.0, 0.5, step=0.01)
        query = st.text_input("Chatbot Query (optional)", value="")
        action = st.number_input("Game Action (optional)", value=0.0, step=0.1)
        transactions_str = st.text_area("Transactions (comma-separated, optional)", value="")
        submit = st.form_submit_button("Get Recommendations")
        
        if submit:
            show_loading()
            transactions = [item.strip() for item in transactions_str.split(",")] if transactions_str else None
            data = {
                "user_id": user_id,
                "score": score,
                "risk": risk,
                "query": query if query else None,
                "action": action if action else None,
                "transactions": transactions
            }
            result = api_call("/recommend_loans", data)
            if result:
                st.success("Recommendations Generated!")
                st.markdown("### Results")
                st.json(result)

## Dashboard Page
elif page == "Dashboard":
    st.title("User Dashboard")
    st.markdown("Your personalized overview of financial insights and recent activities.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Recent Activity")
        st.write("- Credit Assessment: 2023-10-15")
        st.write("- Compliance Check: 2023-10-14")
    with col2:
        st.subheader("Quick Stats")
        st.write("- Credit Score: 0.85")
        st.write("- ESG Score: 0.72")
    
    st.subheader("Performance Chart")
    df = pd.DataFrame({
        "Date": ["2023-10-01", "2023-10-08", "2023-10-15"],
        "Score": [0.7, 0.8, 0.85]
    })
    st.line_chart(df.set_index("Date"))

## Train Models Page (Admin Operation)
elif page == "Train Models":
    st.title("Train Models")
    st.markdown("Provide training data for the models.")
    
    with st.form("train_models_form"):
        st.markdown('<h3 class="section-header">Input Training Data (JSON format)</h3>', unsafe_allow_html=True)
        training_data_str = st.text_area("Training Data JSON", value='{"alt_data": [[1,2,3,4,5]], "targets": [0.8]}', height=200)
        submit = st.form_submit_button("Train Models")
        
        if submit:
            try:
                training_data = json.loads(training_data_str)
            except json.JSONDecodeError:
                st.error("Invalid JSON format.")
                training_data = None
            if training_data:
                show_loading()
                result = api_call("/train_models", {"training_data": training_data})
                if result:
                    st.success("Models trained successfully!")
                    st.json(result)

## Set Compliance Rule Page (Admin Operation)
elif page == "Set Compliance Rule":
    st.title("Set Compliance Rule")
    st.markdown("Define a compliance rule for a contract.")
    
    with st.form("set_compliance_rule_form"):
        st.markdown('<h3 class="section-header">Input Rule Details</h3>', unsafe_allow_html=True)
        contract_id = st.text_input("Contract ID")
        conditions_str = st.text_area("Conditions (JSON format)", value='{"min_age": 18}', height=150)
        submit = st.form_submit_button("Set Rule")
        
        if submit:
            try:
                conditions = json.loads(conditions_str)
            except json.JSONDecodeError:
                st.error("Invalid JSON format for conditions.")
                conditions = None
            if contract_id and conditions:
                show_loading()
                result = api_call("/set_compliance_rule", {"contract_id": contract_id, "conditions": conditions})
                if result:
                    st.success("Compliance rule set successfully!")
                    st.json(result)

## Enroll Biometric Page (Admin Operation)
elif page == "Enroll Biometric":
    st.title("Enroll Biometric Data")
    st.markdown("Enroll a user with biometric data for enhanced security.")
    
    with st.form("enroll_biometric_form"):
        st.markdown('<h3 class="section-header">Input Biometric Details</h3>', unsafe_allow_html=True)
        user_id = st.text_input("User ID")
        bio_data_str = st.text_area("Biometric Data (comma-separated numbers)", value="0.1, 0.2, 0.3", height=150)
        submit = st.form_submit_button("Enroll")
        
        if submit:
            try:
                bio_data = [float(x.strip()) for x in bio_data_str.split(",")]
            except ValueError:
                st.error("Invalid biometric data format.")
                bio_data = None
            if user_id and bio_data:
                show_loading()
                result = api_call("/enroll_biometric", {"user_id": user_id, "bio_data": bio_data})
                if result:
                    st.success("Biometric data enrolled successfully!")
                    st.json(result)

## User Guide Page
elif page == "User Guide":
    st.title("User Guide")
    st.markdown("Learn how to make the most of our platform.")
    
    st.markdown("""
    ### Getting Started
    1. **Login**: Use your credentials in the sidebar.
    2. **Navigate**: Use the sidebar to access features.
    3. **Input Data**: Fill out forms for each feature.
    
    ### Feature Overview
    - **Creditworthiness**: Assess your financial profile.
    - **Compliance**: Verify KYC, AML, and document authenticity.
    - **Behavioral Analysis**: Understand user behavior.
    - **ESG Tracking**: Monitor sustainability metrics.
    - **Loan Recommendations**: Find tailored loan options.
    - **Admin Operations**: Train models, set rules, and enroll biometric data.
    """)

## About Us Page
elif page == "About Us":
    st.title("About Us")
    st.markdown("Pioneering the future of micro-finance with AI.")
    
    st.markdown("""
    ### Our Mission
    To provide accessible, ethical, and efficient financial services using artificial intelligence.
    
    ### Our Team
    - **John Doe**: AI Specialist
    - **Jane Smith**: Finance Expert
    - **Alex Brown**: Blockchain Developer
    """)

## Contact Us Page
elif page == "Contact Us":
    st.title("Contact Us")
    st.markdown("We’re here to help!")
    
    with st.form("contact_form"):
        st.markdown('<h3 class="section-header">Get in Touch</h3>', unsafe_allow_html=True)
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message", height=150)
        submit = st.form_submit_button("Send Message")
        if submit:
            st.success(f"Thank you, {name}! Your message has been sent.")
    
    st.markdown("""
    - **Email**: mhatrevipul1518@gmail.com
    - **Phone**: +1-234-567-890
    - **Address**: 123 AI Finance St., Tech City, TC 12345
    """)

## FAQ Page
elif page == "FAQ":
    st.title("Frequently Asked Questions")
    st.markdown("Find answers to common questions.")
    
    st.markdown("""
    ### General
    **Q: What is this platform?**  
    A: An AI-driven micro-finance solution for credit, compliance, ESG, and loan recommendations.
    
    ### Technical
    **Q: How secure is my data?**  
    A: We use decentralized KYC, biometric enrollment, and ethical AI to safeguard your data.
    """)

## Privacy Policy Page
elif page == "Privacy Policy":
    st.title("Privacy Policy")
    st.markdown("Your trust is our priority. We ensure the utmost security of your data.")
    
    st.markdown("""
    ### Data Collection
    We collect only necessary data for our services, which is securely stored.
    
    ### Data Use
    Data is used solely to enhance your experience and comply with regulatory standards.
    """)

## Terms of Service Page
elif page == "Terms of Service":
    st.title("Terms of Service")
    st.markdown("Understand your rights and responsibilities while using our platform.")
    
    st.markdown("""
    ### Usage
    By using this platform, you agree to our terms and conditions.
    
    ### Liability
    We are not liable for losses arising from unforeseen technical issues.
    """)

## Blog Page
elif page == "Blog":
    st.title("Blog")
    st.markdown("Stay updated with insights and news about AI in micro-finance.")
    
    st.markdown("""
    ### Latest Posts
    - **AI in Finance: The Future is Now** (2023-10-10)
    - **Understanding ESG Metrics** (2023-10-05)
    """)

## Support Page
elif page == "Support":
    st.title("Support Center")
    st.markdown("Need help? Contact our support team or explore our resources.")
    
    st.markdown("""
    ### Contact Support
    Submit a ticket via the Contact Us page or email us directly.
    
    ### Resources
    - [User Guide](#user-guide)
    - [FAQ](#faq)
    """)

# Footer
st.markdown(f"""
<div class="footer">
    © {datetime.now().year} AI Micro-Finance Platform. All rights reserved. | 
    <a href="#privacy-policy">Privacy Policy</a> | 
    <a href="#terms-of-service">Terms of Service</a>
</div>
""", unsafe_allow_html=True)
