from flask import Flask, request, jsonify
from flask_cors import CORS  
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app) 

# Load models and vectorizers
ar_model = joblib.load('ar_model.pkl')
en_model = joblib.load('en_model.pkl')
ar_vectorizer = joblib.load('ar_vectorizer.pkl')
en_vectorizer = joblib.load('en_vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Validate input
    if not data or 'language' not in data or 'textContent' not in data:
        return jsonify({'error': 'Missing language or textContent'}), 400

    language = data['language'].lower()
    text = data['textContent']

    try:
        if language == 'ar':
            # Use the loaded Arabic vectorizer
            text_vector = ar_vectorizer.transform([text])
            prediction = ar_model.predict(text_vector)[0]
            result = 'Fake' if prediction == 0 else 'Real'
        elif language == 'en':
            # Use the loaded English vectorizer
            text_vector = en_vectorizer.transform([text])
            prediction = en_model.predict(text_vector)[0]
            result = 'Fake' if prediction == 0 else 'Real'
        else:
            return jsonify({'error': 'Unsupported language'}), 400

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)