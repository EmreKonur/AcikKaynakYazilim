import requests

URL = "https://api.imgbb.com/1/upload"
result = requests.get(URL)
data = result.json()
print(data)