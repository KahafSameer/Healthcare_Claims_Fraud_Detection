import unittest
import joblib
import pandas as pd
import numpy as np

class TestModel(unittest.TestCase):

    def setUp(self):
        """Set up for the tests."""
        try:
            self.model = joblib.load('claims_fraud_detection.pkl')
            self.scaler = joblib.load('scaler.pkl')
        except FileNotFoundError:
            self.fail("Model or scaler not found. Please run train_model.py first.")

    def test_model_and_scaler_loading(self):
        """Test if the model and scaler objects are loaded correctly."""
        self.assertIsNotNone(self.model)
        self.assertIsNotNone(self.scaler)
    
    def test_prediction(self):
        """Test the model prediction with a sample input."""
        # Create a sample input DataFrame
        sample_input = {
            'Provider': [123], 'InscClaimAmtReimbursed': [1000], 'IPAnnualReimbursementAmt': [2000],
            'IPAnnualDeductibleAmt': [500], 'TotalReimbursement': [3000], 'RenalDiseaseIndicator': [1],
            'ChronicCond_Alzheimer': [1], 'ChronicCond_Heartfailure': [0], 'ChronicCond_KidneyDisease': [1],
            'ChronicCond_Cancer': [0], 'ChronicCond_ObstrPulmonary': [0], 'ChronicCond_Depression': [0],
            'ChronicCond_Diabetes': [1], 'ChronicCond_IschemicHeart': [0], 'ChronicCond_Osteoporasis': [0],
            'ChronicCond_rheumatoidarthritis': [0], 'ChronicCond_stroke': [0]
        }
        input_df = pd.DataFrame(sample_input)

        # Scale the input
        input_scaled = self.scaler.transform(input_df)

        # Make a prediction
        prediction = self.model.predict(input_scaled)

        # Check the output
        self.assertIn(prediction[0], [0, 1])

if __name__ == '__main__':
    unittest.main()