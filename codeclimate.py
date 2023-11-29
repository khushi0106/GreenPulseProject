import requests

# Set your Code Climate API token
api_token = '0cd42455fa3cef7f277f23a5f9a1abb3931c6ba6'

# Set the repository ID (replace with your repository ID)
repo_id = 'your_repository_id'

# Code Climate API base URL
base_url = 'https://api.codeclimate.com/v1'

# Function to get repository information
def get_repo_info(api_token, repo_id):
    headers = {'Authorization': f'Token {api_token}'}
    url = f'{base_url}/repos/{repo_id}'
    response = requests.get(url, headers=headers)
    return response.json()

# Function to analyze repository for issues
def analyze_repo(api_token, repo_id):
    headers = {'Authorization': f'Token {api_token}'}
    url = f'{base_url}/repos/{repo_id}/analyze'
    response = requests.post(url, headers=headers)
    return response.json()

# Example usage
try:
    # Get repository information
    repo_info = get_repo_info(api_token, repo_id)
    print('Repository Information:')
    print(repo_info)

    # Analyze repository for issues
    analysis_result = analyze_repo(api_token, repo_id)
    print('Analysis Result:')
    print(analysis_result)

except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
