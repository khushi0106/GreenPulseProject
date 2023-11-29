import requests

def compile_and_execute_code(code):
    api_endpoint = 'https://api.jdoodle.com/v1/execute'
    client_id = '5576145851311c08f7442e057eccc666'
    client_secret = '23812612909fbf62e993cb041840a15bd9949586d42dc94b0aec5dfad04ac58c'

    payload = {
        'script': code,
        'language': 'python3',
        'versionIndex': '3',
        'clientId': client_id,
        'clientSecret': client_secret
    }

    response = requests.post(api_endpoint, json=payload)

    if response.status_code == 200:
        result = response.json()

        if 'error' in result:
            # Compilation or execution error
            return {'success': False, 'error_message': result['error']}
        else:
            # Compilation and execution successful
            return {'success': True, 'output': result['output']}
    else:
        # Handle HTTP errors
        return {'success': False, 'error_message': 'HTTP Error'}

# Example usage
code_snippet = "int a=5;"
result = compile_and_execute_code(code_snippet)
print(result)
