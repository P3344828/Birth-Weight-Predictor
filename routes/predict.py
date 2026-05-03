import pandas as pd
import pickle
import os
from flask import Blueprint, request, render_template, jsonify

predict_bp = Blueprint("predict",__name__)

# Lazy load the model to avoid hanging on startup
model = None

def get_model():
    global model
    if model is None:
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model.pkl")
        with open(path, 'rb') as obj:
            model = pickle.load(obj)
    return model

EXPECTED_COLUMNS = ["gestation","parity","age","height","weight","smoke"]

@predict_bp.route('/predict', methods=['POST'])
def get_prediction():
    is_api = request.is_json
    
    if is_api:
        baby_data_form = request.get_json()
    else:
        baby_data_form = request.form

    if not baby_data_form:
        if is_api:
            return jsonify({"error": "No input data provided"}), 400
        return render_template('index.html', error="No input data provided")
        
    # Check for missing columns
    for col in EXPECTED_COLUMNS:
        if col not in baby_data_form:
            if is_api:
                return jsonify({"error": f"Missing column: {col}"}), 400
            return render_template('index.html', error=f"Missing column: {col}")

    # convert into dataframe and ensure numeric types
    try:
        if is_api:
            baby_df = pd.DataFrame(baby_data_form)[EXPECTED_COLUMNS]
        else:
            # HTML form gives strings, need to parse to float
            cleaned_data = {col: [float(baby_data_form[col])] for col in EXPECTED_COLUMNS}
            baby_df = pd.DataFrame(cleaned_data)
    except Exception as e:
        if is_api:
            return jsonify({"error": "Invalid data format"}), 400
        return render_template('index.html', error="Invalid data format")

    # Make prediction on user data
    prediction = get_model().predict(baby_df)
    
    # Extract scalar if array
    try:
        pred_value = float(prediction[0])
    except (TypeError, IndexError):
        pred_value = float(prediction)

    prediction_rounded = round(pred_value, 2)

    # Return response
    if is_api:
        return jsonify({"Prediction": prediction_rounded}), 200
    else:
        return render_template('index.html', prediction=prediction_rounded)