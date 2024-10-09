# app.py (Flask app)
from flask import Flask, request, jsonify
import pandas as pd
import joblib
import requests

app = Flask(__name__)

# Load the trained model
model = joblib.load('reg_fetch_california_housing.joblib')

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    columns = data['features']
    prediction = model.predict(pd.DataFrame([features], columns=columns))
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')  # Start the Flask app



