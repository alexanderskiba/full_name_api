import requests


url = f'http://localhost:5000/validate_full_name/'
data = {"full_name": "Иванов Иван Иванович"}
response = requests.post(url, json=data)
print(response.json())