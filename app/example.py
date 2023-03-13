import requests

url = 'http://localhost:5000/chat'
url_fastapi= 'http://localhost:8000/chat'
data = {"message": "Hello, ChatGPT!, who are you"}
response = requests.post(url, json=data)

print(response.json())