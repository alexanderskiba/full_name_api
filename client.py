import requests


url = f'http://localhost:5000/validate_full_name/'
data = {"hello": "world"}
response = requests.post(url, json=data)
print(response.text)