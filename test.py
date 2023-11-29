import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import json
import joblib
code_snippets = ["int x = 5;\nint y = 10;\nint sum = x + y;\nSystem.out.println('Sum: ' + sum);",
                 "int x = 5;\nint y = 10;\nString result = x + y;\nSystem.out.println('Result: ' + result);",
                 "int x = 5;\nint z = x + z;\nSystem.out.println('Z: ' + z);",
                 
                 #java examples
                  "public class HelloWorld {\n  public static void main(String[] args) {\n    System.out.println(\"Hello, World!\");\n  }\n}",
                  "int x = 5;\nint y = 10;\nint sum = x + y;\nSystem.out.println('Sum: ' + sum);",
                  "for (int i = 0; i < 5; i++) {\n  System.out.println(i);\n}",
    
    # Python examples
                  "def greet(name):\n  print('Hello, ' + name + '!')\n\ngreet('John')",
                  "x = 5\ny = 10\nresult = x + y\nprint('Result:', result)",
                  "for i in range(5):\n  print(i)",
    
    # C++ examples
                 "#include <iostream>\nusing namespace std;\nint main() {\n  cout << \"Hello, World!\" << endl;\n  return 0;\n}",
                 "int x = 5;\nint z = x + z;\ncout << 'Z: ' << z << endl;",
                 "for (int i = 0; i < 5; i++) {\n  cout << i << endl;\n}" 
                 ]

json_metrics = [
    {"lines_of_code": 4, "number_of_components": 1, "optimized_rating": 1, "syntax_errors": 0},
    {"lines_of_code": 4, "number_of_components": 1, "optimized_rating": 0, "syntax_errors": 1},
    {"lines_of_code": 3, "number_of_components": 1, "optimized_rating": 0, "syntax_errors": 1},
    
    {"lines_of_code": 3, "number_of_components": 2, "optimized_rating": 1, "syntax_errors": 0},
    {"lines_of_code": 4, "number_of_components": 1, "optimized_rating": 0, "syntax_errors": 1},
    {"lines_of_code": 2, "number_of_components": 1, "optimized_rating": 1, "syntax_errors": 0},
    
    {"lines_of_code": 3, "number_of_components": 1, "optimized_rating": 1, "syntax_errors": 0},
    {"lines_of_code": 4, "number_of_components": 1, "optimized_rating": 0, "syntax_errors": 1},
    {"lines_of_code": 2, "number_of_components": 1, "optimized_rating": 1, "syntax_errors": 0},
    
    {"lines_of_code": 5, "number_of_components": 1, "optimized_rating": 1, "syntax_errors": 0},
    {"lines_of_code": 3, "number_of_components": 1, "optimized_rating": 0, "syntax_errors": 1},
    {"lines_of_code": 2, "number_of_components": 1, "optimized_rating": 1, "syntax_errors": 0}   
]


labels = [1 if metric["optimized_rating"] == 1 else 0 for metric in json_metrics]

X_train, X_test, y_train, y_test = train_test_split(code_snippets, labels, test_size=0.2, random_state=42)


vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


classifier = MultinomialNB()
classifier.fit(X_train_vec, y_train)


model_filename = 'optimized_model.joblib'
joblib.dump(classifier, model_filename)
vectorizer_filename = 'vectorizer.joblib'
joblib.dump(vectorizer, vectorizer_filename)

print(f"Model saved to {model_filename}")
loaded_classifier = joblib.load(model_filename)
predictions = loaded_classifier.predict(X_test_vec)

accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy}")

new_code_snippet = ["int x = 5;\nint y = 10;\nint sum = x + y;\nSystem.out.println('Sum: ' + sum);"]
new_code_vec = vectorizer.transform(new_code_snippet)
new_prediction = loaded_classifier.predict(new_code_vec)

predicted_json_metrics = json_metrics[new_prediction[0]]
print(f"Predicted JSON Metrics: {json.dumps(predicted_json_metrics)}")

