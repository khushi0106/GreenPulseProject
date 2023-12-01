from flask import Flask, render_template, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import re, os
import json

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
        samplecode_path = 'samplecode.py'
        with open(samplecode_path, 'w') as file:
            file.write('')
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file found'})
            
        file = request.files['file']
           
        if file.filename=='':
            return jsonify({'error': 'No selected file'})
        
        file_contents = file.read()
            
        #code_snippet = request.files['file']
        #print(code_snippet)
        
        with open(samplecode_path, 'w') as f:
            f.write(file_contents.decode('utf-8'))
            
        import jdoodle
        response = jdoodle.compile_and_execute_code()
        print(response)
        
        if response == True:
            import pylint
            lint_response = pylint.run_pylint()
            print(lint_response)
            
            import psutillog
            util_cpu, util_cpucount, util_memory = psutillog.run_code_file()
            print(util_cpu, util_cpucount, util_memory)
            
            result = {
                "jdoodle_response": "Compiled" if response==True else "Not Compiled",
                "lint_response": lint_response,
                "util_cpu": util_cpu,
                "util_cpucount": util_cpucount,
                "util_memory": util_memory 
            }
            return jsonify(result)
            
      #  else:
       #     return jsonify({'Failure': 'File is not compilable. Return with compilable file'})    

    except Exception as e:
        return jsonify({'error': str(e)})
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)

        
    """  
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
"""