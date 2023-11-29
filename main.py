from flask import Flask, render_template, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import re

app = Flask(__name__)

# Load pre-trained model and vectorizer
model_filename = 'optimized_model.joblib'
loaded_classifier = joblib.load(model_filename)
vectorizer_filename = 'vectorizer.joblib'
# Loading the trained TfidfVectorizer
loaded_vectorizer = joblib.load(vectorizer_filename)

def is_valid_code(code):
    # Define a simple regular expression for Python code
    pattern = re.compile(r'^\s*(import|from|def|class|if|else|for|while|try|except|print|int)\b')
    
    # Check if the code contains any valid keywords
    return bool(pattern.search(code))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        code_snippet = request.json['code']

         # Check if the code snippet is valid
        if not is_valid_code(code_snippet):
            print("Invalid code snippet")
            return jsonify({"error": "Invalid code snippet"})

        print("Valid code snippet")

        code_vec = loaded_vectorizer.transform([code_snippet])
        prediction = loaded_classifier.predict(code_vec)
        from test import json_metrics
        predicted_metrics = json_metrics[prediction[0]]

        # Return results as JSON
        result = {
            "optimized_rating": int(prediction[0]),
            "message": "Optimized" if prediction[0] == 1 else "Non-Optimized",
            "predicted_metrics": predicted_metrics
        }
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
