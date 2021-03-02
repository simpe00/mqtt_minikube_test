import requests


response = requests.get('http://172.20.0.6:80/environment')
print(response)
print(response.text)
