import joblib

def load_trained_model():
    return joblib.load('CO2_Emission/models/trained_model.pkl')

def predict_emissions(engineSize, coeff, intercept):
    prediction = engineSize * coeff + intercept
    return prediction