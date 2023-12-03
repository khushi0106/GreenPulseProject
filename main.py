from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
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
        jdoodle_response = jdoodle.compile_and_execute_code()
        print(jdoodle_response)
        
        if jdoodle_response == True:
            result = {
                'jdoodle_response': jdoodle_response
            }
            response= jsonify(result)
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
        else:
            result = {
                'jdoodle_response': jdoodle_response
            } 
            return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/button_clicked', methods=['GET', 'POST'])
def button_clicked():
    return render_template('dashboard.html')
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
        
    """  
            import pylint
            lint_response = pylint.run_pylint()
            print(lint_response)
            
            import psutillog
            util_cpu, util_cpucount, util_memory = psutillog.run_code_file()
            print(util_cpu, util_cpucount, util_memory)
    
    
    
    
    
    
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