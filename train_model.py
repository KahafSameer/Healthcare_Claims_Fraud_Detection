import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_model(data_path='claims_cleaned_data.csv'):
    """
    Trains the fraud detection model.

    Args:
        data_path (str): The path to the cleaned claims data.
    """
    logging.info("Starting model training...")

    # Load data
    try:
        df = pd.read_csv(data_path)
        logging.info("Data loaded successfully.")
    except FileNotFoundError:
        logging.error(f"Data file not found at {data_path}. Please provide the correct path.")
        return

    # Define features and target
    top_features = ['Provider', 'InscClaimAmtReimbursed', 'IPAnnualReimbursementAmt',
                    'IPAnnualDeductibleAmt', 'TotalReimbursement', 'RenalDiseaseIndicator',
                    'ChronicCond_Alzheimer', 'ChronicCond_Heartfailure', 'ChronicCond_KidneyDisease',
                    'ChronicCond_Cancer', 'ChronicCond_ObstrPulmonary', 'ChronicCond_Depression',
                    'ChronicCond_Diabetes', 'ChronicCond_IschemicHeart', 'ChronicCond_Osteoporasis',
                    'ChronicCond_rheumatoidarthritis', 'ChronicCond_stroke']
    X = df[top_features]
    y = df['PotentialFraud']
    logging.info("Features and target defined.")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    logging.info("Data split into training and testing sets.")

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    logging.info("Features scaled.")

    # Define the parameter grid
    param_grid_gb = {
        'n_estimators': [100],
        'learning_rate': [0.1],
        'max_depth': [5],
        'min_samples_split': [10],
        'min_samples_leaf': [6]
    }
    logging.info("Parameter grid defined.")

    # Initialize and train the model with GridSearchCV
    gb = GradientBoostingClassifier(random_state=42)
    grid_search_gb = GridSearchCV(estimator=gb, param_grid=param_grid_gb, cv=5, n_jobs=-1, verbose=2, scoring='roc_auc')
    grid_search_gb.fit(X_train_scaled, y_train)
    logging.info("Model training with GridSearchCV completed.")

    # Save the model and scaler
    joblib.dump(grid_search_gb.best_estimator_, 'claims_fraud_detection.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    logging.info("Model and scaler saved successfully.")

if __name__ == '__main__':
    train_model()