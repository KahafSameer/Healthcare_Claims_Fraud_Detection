import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
from streamlit_shap import st_shap
import matplotlib.pyplot as plt

# Load trained model and scaler
model = joblib.load(open('claims_fraud_detection.pkl', 'rb'))
scaler = joblib.load(open('scaler.pkl', 'rb'))

# Define Streamlit app
def app():

    st.markdown("""
        <style>
        .main-title {font-size:2.5rem; font-weight:bold; color:#2c3e50; text-align:center; margin-bottom:0;}
        .subtitle {font-size:1.2rem; color:#555; text-align:center; margin-bottom:2rem;}
        .stButton>button {background-color:#4CAF50; color:white; font-weight:bold; border-radius:8px;}
        .result-box {padding:1.5rem; border-radius:10px; margin-top:1.5rem;}
        </style>
    """, unsafe_allow_html=True)

    st.image("assets/fraud-alert.png", width=120)
    st.markdown('<div class="main-title">Healthcare Claims <span style="color:#e67e22;">Fraud Detection</span> App</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Predict whether a claim is <b>fraudulent</b> based on multiple features</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### <span style='color:#2980b9'>Enter the claim details below:</span>", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            Provider = st.number_input("Provider's Code", min_value=0.0, step=1e-2, format="%.2f", help="Unique identifier for the healthcare provider.")
            InscClaimAmtReimbursed = st.number_input("Insurance Claim Amount Reimbursed", min_value=0.0, step=1e-2, format="%.2f", help="Amount reimbursed by the insurance for the claim.")
            IPAnnualReimbursementAmt = st.number_input("Inpatient Annual Reimbursement Amount", min_value=0.0, step=1e-2, format="%.2f", help="Annual reimbursement amount for inpatient services.")
            IPAnnualDeductibleAmt = st.number_input("Inpatient Annual Deductible Amount", min_value=0.0, step=1e-2, format="%.2f", help="Annual deductible amount for inpatient services.")
            TotalReimbursement = st.number_input("Total Reimbursement", min_value=0.0, step=1e-2, format="%.2f", help="Total reimbursement amount, including inpatient and outpatient services.")
            RenalDiseaseIndicator = st.selectbox("Renal Disease Indicator", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has a renal disease.")
        with col2:
            ChronicCond_Alzheimer = st.selectbox("Alzheimer's Disease", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has Alzheimer's disease.")
            ChronicCond_Heartfailure = st.selectbox("Heart Failure", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has heart failure.")
            ChronicCond_KidneyDisease = st.selectbox("Kidney Disease", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has kidney disease.")
            ChronicCond_Cancer = st.selectbox("Cancer", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has cancer.")
            ChronicCond_ObstrPulmonary = st.selectbox("COPD", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has Chronic Obstructive Pulmonary Disease.")
            ChronicCond_Depression = st.selectbox("Depression", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has depression.")
            ChronicCond_Diabetes = st.selectbox("Diabetes", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has diabetes.")
            ChronicCond_IschemicHeart = st.selectbox("Ischemic Heart Disease", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has ischemic heart disease.")
            ChronicCond_Osteoporasis = st.selectbox("Osteoporosis", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has osteoporosis.")
            ChronicCond_rheumatoidarthritis = st.selectbox("Rheumatoid Arthritis", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has rheumatoid arthritis.")
            ChronicCond_stroke = st.selectbox("Stroke", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Indicates if the patient has had a stroke.")

    st.markdown("---")
    predict_clicked = st.button("🔍 Predict Claim Fraud", use_container_width=True)

    if predict_clicked:
        # Input validation
        missing_fields = []
        if Provider == 0.0:
            missing_fields.append("Provider's Code")
        if InscClaimAmtReimbursed == 0.0:
            missing_fields.append("Insurance Claim Amount Reimbursed")
        if IPAnnualReimbursementAmt == 0.0:
            missing_fields.append("Inpatient Annual Reimbursement Amount")
        if IPAnnualDeductibleAmt == 0.0:
            missing_fields.append("Inpatient Annual Deductible Amount")
        if TotalReimbursement == 0.0:
            missing_fields.append("Total Reimbursement")
        # Chronic/indicator fields are 0/1, so not required to check
        if missing_fields:
            st.warning(f"Please fill in: {', '.join(missing_fields)}")
        else:
            with st.spinner('Predicting...'):
                input_data = pd.DataFrame([[Provider, InscClaimAmtReimbursed, IPAnnualReimbursementAmt, IPAnnualDeductibleAmt, 
                                            TotalReimbursement, RenalDiseaseIndicator, ChronicCond_Alzheimer, 
                                            ChronicCond_Heartfailure, ChronicCond_KidneyDisease, ChronicCond_Cancer, 
                                            ChronicCond_ObstrPulmonary, ChronicCond_Depression, ChronicCond_Diabetes, 
                                            ChronicCond_IschemicHeart, ChronicCond_Osteoporasis, ChronicCond_rheumatoidarthritis, 
                                            ChronicCond_stroke]], 
                                        columns=['Provider', 'InscClaimAmtReimbursed', 'IPAnnualReimbursementAmt', 
                                                    'IPAnnualDeductibleAmt', 'TotalReimbursement', 'RenalDiseaseIndicator', 
                                                    'ChronicCond_Alzheimer', 'ChronicCond_Heartfailure', 
                                                    'ChronicCond_KidneyDisease', 'ChronicCond_Cancer', 
                                                    'ChronicCond_ObstrPulmonary', 'ChronicCond_Depression', 
                                                    'ChronicCond_Diabetes', 'ChronicCond_IschemicHeart', 
                                                    'ChronicCond_Osteoporasis', 'ChronicCond_rheumatoidarthritis', 
                                                    'ChronicCond_stroke'])

                input_data_scaled = scaler.transform(input_data)
                prediction = model.predict(input_data_scaled)
                proba = model.predict_proba(input_data_scaled)[0][1]

                if prediction[0] == 1:
                    st.markdown(f'<div class="result-box" style="background-color:#ffe6e6;"><h3 style="color:#c0392b;">🚨 This claim is likely <b>fraudulent</b>!</h3><p><b>Fraud Probability:</b> {proba:.2%}</p></div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="result-box" style="background-color:#e8f8f5;"><h3 style="color:#27ae60;">✅ This claim seems <b>legitimate</b>.</h3><p><b>Fraud Probability:</b> {proba:.2%}</p></div>', unsafe_allow_html=True)

                with st.expander("View Feature Importance"):
                    st.write("#### Local Feature Importance (for this specific claim)")
                    explainer = shap.TreeExplainer(model)
                    shap_values = explainer.shap_values(input_data_scaled)
                    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], input_data.iloc[0,:]))

                    st.markdown("---")
                    
                    st.write("#### Dynamic Prediction Breakdown (Waterfall Plot)")
                    st.write("This plot shows how each feature's value pushes the prediction from the baseline to the final output.")
                    
                    # Create a SHAP explanation object for the waterfall plot
                    expl = shap.Explanation(values=shap_values[0],
                                            base_values=explainer.expected_value,
                                            data=input_data.iloc[0].values,
                                            feature_names=input_data.columns.tolist())
                    
                    # Generate the waterfall plot
                    fig, ax = plt.subplots()
                    shap.waterfall_plot(expl, show=False)
                    st.pyplot(fig)



if __name__ == "__main__":
    app()

