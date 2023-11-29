import requests

# Replace 'YOUR_API_KEY' and 'INSIGHTS_QUERY_ENDPOINT' with your actual API key and endpoint
api_key = 'eu01xx3f87ec4e9e098056b6e34f1cffFFFFNRAL'  #license key 
endpoint = 'https://metric-api.eu.newrelic.com/metric/v1'

code_snippet = """
    def hello():
        print('Hello, World!')
"""

data={  
        "name":"cpu", 
        "type":"gauge", 
        "value":2.3, 
        "attributes":{"host.name":"dev.server.com"} 
    }

headers = {
    'Api-Key': api_key,
    'Content-Type': 'application/json',
}

response = requests.post(endpoint, json=data, headers=headers)

result = requests.get(endpoint, headers=headers)

if response.status_code == 202:
    data = result.json()
    # Process the data as needed
    print(data)
else:
    print(f"Error: {response.status_code}, {response.text}")
