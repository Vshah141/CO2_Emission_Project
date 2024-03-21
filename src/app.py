from flask import Flask, request, jsonify, send_file
import pandas as pd
import numpy as np
from data_processing import Data_Ingestion, Data_Analysis, Data_Visualisation
from model_training import Model_training
import model_prediction

app = Flask(__name__)
trained_model = model_prediction.load_trained_model()

@app.route('/')
def index():
    return send_file(r"C:\vs code\ML\LinearRegression\CO2_Emission\templates\front.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    engine_size = data['engine_size']
    if engine_size < 1:
        return jsonify({'error': 'Invalid Engine Size'})
    else:
        df = Data_Ingestion("CO2_Emission/data/FuelConsumptionCo2.csv")
        Data_Analysis(df)
        new_df = Data_Visualisation(df)
        model_coefficient, model_intercept = trained_model.coef_, trained_model.intercept_
        pred = model_prediction.predict_emissions(engine_size, model_coefficient, model_intercept)
        return jsonify({'predicted_emission': pred[0][0]})

if __name__ == '__main__':
    app.run(debug=True)
