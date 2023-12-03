from flask import Flask, render_template, request, jsonify
import pylint
import psutillog

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    samplecode_path = 'samplecode.py'
    with open(samplecode_path, 'w') as file:
        file.write('')
    
    if 'file' not in request.files:
        return "No file attached."
    
    file = request.files['file']
    
    if file.filename == '':
        return "no selected file."
    
    content = file.read().decode('utf-8')
    
    with open(samplecode_path, 'w') as f:
        f.write(content)
    
    return render_template('result.html')

@app.route('/call_pylint', methods=['GET', 'POST'])
def call_pylint():
    pylint_output = pylint.run_pylint()
    return jsonify(pylint_output=pylint_output)

@app.route('/call_psutil', methods=['GET', 'POST'])
def call_psutil():
    cpu_percent, cpu_threads, memory = psutillog.run_code_file()
    return jsonify(cpu_percent=cpu_percent, cpu_threads=cpu_threads, memory=memory)

@app.route('/call_jdoodle')
def call_jdoodle():
    import jdoodle
    response = jdoodle.compile_and_execute_code()
    return jsonify(response=response)   

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
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