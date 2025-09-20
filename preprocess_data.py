import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def preprocess_data():
    """
    This function loads the raw data, merges the different files,
    and creates the final cleaned dataset.
    """
    # Load the datasets
    train_df = pd.read_csv('Train-1542865627584.csv')
    train_beneficiary_df = pd.read_csv('Train_Beneficiarydata-1542865627584.csv')
    train_inpatient_df = pd.read_csv('Train_Inpatientdata-1542865627584.csv')
    train_outpatient_df = pd.read_csv('Train_Outpatientdata-1542865627584.csv')

    # Merge inpatient and outpatient data
    train_io_df = pd.concat([train_inpatient_df, train_outpatient_df], axis=0)

    # Merge with beneficiary data
    train_full_df = pd.merge(train_io_df, train_beneficiary_df, on='BeneID', how='inner')

    # Merge with the main training data
    final_df = pd.merge(train_full_df, train_df, on='Provider', how='inner')

    # Feature Engineering and Cleaning (as described in README)
    # This is a simplified version of the cleaning process.
    # A more thorough implementation would handle missing values and categorical encoding more robustly.

    # Drop unnecessary columns
    final_df = final_df.drop(['BeneID', 'ClaimID', 'ClaimStartDt', 'ClaimEndDt', 'AttendingPhysician',
                               'OperatingPhysician', 'OtherPhysician', 'ClmDiagnosisCode_1', 'ClmDiagnosisCode_2',
                               'ClmDiagnosisCode_3', 'ClmDiagnosisCode_4', 'ClmDiagnosisCode_5',
                               'ClmDiagnosisCode_6', 'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8',
                               'ClmDiagnosisCode_9', 'ClmDiagnosisCode_10', 'ClmProcedureCode_1',
                               'ClmProcedureCode_2', 'ClmProcedureCode_3', 'ClmProcedureCode_4',
                               'ClmProcedureCode_5', 'ClmProcedureCode_6', 'DeductibleAmtPaid','DiagnosisGroupCode',
                               'DOB', 'DOD', 'State', 'County', 'Race'], axis=1, errors='ignore')

    # RenalDiseaseIndicator: covert Y to 1 and N to 0
    final_df['RenalDiseaseIndicator'] = final_df['RenalDiseaseIndicator'].apply(lambda x: 1 if x == 'Y' else 0)

    # Create TotalReimbursement
    final_df['TotalReimbursement'] = final_df['InscClaimAmtReimbursed'] + final_df['IPAnnualReimbursementAmt'] + final_df['OPAnnualReimbursementAmt']

    # One-hot encode chronic conditions
    for col in ['ChronicCond_Alzheimer', 'ChronicCond_Heartfailure',
                'ChronicCond_KidneyDisease', 'ChronicCond_Cancer',
                'ChronicCond_ObstrPulmonary', 'ChronicCond_Depression',
                'ChronicCond_Diabetes', 'ChronicCond_IschemicHeart',
                'ChronicCond_Osteoporasis', 'ChronicCond_rheumatoidarthritis',
                'ChronicCond_stroke']:
        final_df[col] = final_df[col].apply(lambda x: 1 if x == 1 else 0)


    final_df['PotentialFraud'] = final_df['PotentialFraud'].apply(lambda x: 1 if x == 'Yes' else 0)

    # Convert all feature columns to numeric, coercing errors
    for col in final_df.columns:
        if col != 'PotentialFraud':
            final_df[col] = pd.to_numeric(final_df[col], errors='coerce')

    # Fill missing values with 0 (a simple imputation strategy)
    final_df = final_df.fillna(0)

    # Label encode the 'Provider' column
    le = LabelEncoder()
    final_df['Provider'] = le.fit_transform(final_df['Provider'])

    # Save the cleaned data
    final_df.to_csv('claims_cleaned_data.csv', index=False)
    print("Pre-processing complete. Cleaned data saved to 'claims_cleaned_data.csv'")

if __name__ == '__main__':
    preprocess_data()