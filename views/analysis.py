import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define the main app function
def app():
    """
    This function defines the data analysis page of the Streamlit application.
    It loads the cleaned dataset and provides various visualizations.
    """
    # --- Page Title and Description ---
    st.markdown("""
        <style>
        .main-title {font-size:2.5rem; font-weight:bold; color:#2c3e50; text-align:center; margin-bottom:0;}
        .subtitle {font-size:1.2rem; color:#555; text-align:center; margin-bottom:2rem;}
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="main-title">Exploratory Data <span style="color:#e67e22;">Analysis</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Gain insights from the healthcare claims dataset</div>', unsafe_allow_html=True)
    st.markdown("---")

    # --- Load Data ---
    data_path = 'claims_cleaned_data.csv'
    if os.path.exists(data_path):
        with st.spinner('Loading data...'):
            try:
                df = pd.read_csv(data_path)

                # --- Section 1: Data Overview ---
                st.subheader("1. Dataset Overview")
                st.write("Here is a preview of the cleaned dataset:")
                st.dataframe(df.head())
                st.write(f"The dataset contains **{df.shape[0]}** rows and **{df.shape[1]}** columns.")
                
                # --- Section 2: Descriptive Statistics ---
                st.subheader("2. Descriptive Statistics")
                st.write("Summary statistics for the numerical features:")
                st.write(df.describe())

                # --- Section 3: Fraud Distribution ---
                st.subheader("3. Fraud vs. Legitimate Claims")
                fraud_counts = df['PotentialFraud'].value_counts()
                fraud_percentage = (fraud_counts / len(df)) * 100
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.write("Distribution of Claims:")
                    st.write(fraud_percentage.map('{:.2f}%'.format))
                with col2:
                    fig, ax = plt.subplots(figsize=(6, 4))
                    sns.barplot(x=fraud_counts.index, y=fraud_counts.values, hue=fraud_counts.index, ax=ax, palette="pastel", legend=False)
                    ax.set_title("Fraud Distribution", fontsize=16)
                    ax.set_xlabel("Claim Type (0: Legitimate, 1: Fraud)", fontsize=12)
                    ax.set_ylabel("Number of Claims", fontsize=12)
                    st.pyplot(fig)
                
                st.markdown("---")

                # --- Section 4: Numerical Feature Distribution ---
                st.subheader("4. Distribution of Key Numerical Features")
                numerical_features = ['InscClaimAmtReimbursed', 'IPAnnualReimbursementAmt', 'IPAnnualDeductibleAmt', 'TotalReimbursement']
                
                fig, axes = plt.subplots(2, 2, figsize=(14, 10))
                axes = axes.flatten()
                for i, feature in enumerate(numerical_features):
                    sns.histplot(df[feature], kde=True, ax=axes[i], color='skyblue', bins=50)
                    axes[i].set_title(f'Distribution of {feature}', fontsize=14)
                    axes[i].set_xlabel("")
                plt.tight_layout()
                st.pyplot(fig)
                
                st.markdown("---")
                
                # --- Section 5: Correlation Heatmap ---
                st.subheader("5. Feature Correlation Heatmap")
                st.write("This heatmap shows the correlation between different numerical features.")
                
                # Select only top features used in the model for clarity
                top_features = ['Provider', 'InscClaimAmtReimbursed', 'IPAnnualReimbursementAmt', 'IPAnnualDeductibleAmt', 
                                'TotalReimbursement', 'RenalDiseaseIndicator', 'ChronicCond_Alzheimer', 
                                'ChronicCond_Heartfailure', 'ChronicCond_KidneyDisease', 'ChronicCond_Cancer', 
                                'ChronicCond_ObstrPulmonary', 'ChronicCond_Depression', 'ChronicCond_Diabetes', 
                                'ChronicCond_IschemicHeart', 'ChronicCond_Osteoporasis', 'ChronicCond_rheumatoidarthritis', 
                                'ChronicCond_stroke', 'PotentialFraud']
                
                corr_matrix = df[top_features].corr()
                
                fig, ax = plt.subplots(figsize=(16, 12))
                sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax, annot_kws={"size": 8})
                ax.set_title('Correlation Matrix of Key Features', fontsize=16)
                st.pyplot(fig)

            except Exception as e:
                st.error(f"An error occurred while processing the data: {e}")
    else:
        st.error(f"Data file not found at '{data_path}'. Please run the pre-processing script first.")

# To run this page independently for testing
if __name__ == "__main__":
    app()