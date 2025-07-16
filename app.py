from flask import Flask, request, jsonify
from flask_cors import CORS  
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app) 

# Load models only
ar_model = joblib.load('ar_model.pkl')
en_model = joblib.load('en_model.pkl')

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
            # Arabic stopwords
            arabic_stopwords = [
                "في", "من", "على", "إلى", "و", "عن", "أن", "إن", "كان", "هذه", "هذا", "ما", "لا", "لم", "لن", "قد",
                "هل", "هو", "هي", "ثم", "ذلك", "كل", "أو", "أي", "أين", "كيف", "لماذا", "متى", "ب", "ل", "حتى", "كما"
            ]
            vectorizer = TfidfVectorizer(stop_words=arabic_stopwords)
            text_vector = vectorizer.fit_transform([text])  # transform to numeric
            prediction = ar_model.predict(text_vector)[0]
        elif language == 'en':
            vectorizer = TfidfVectorizer(stop_words='english')
            text_vector = vectorizer.fit_transform([text])  # transform to numeric
            prediction = en_model.predict(text_vector)[0]
        else:
            return jsonify({'error': 'Unsupported language'}), 400

        result = 'Fake' if prediction == 1 else 'Real'
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)