import requests


response = requests.get('http://172.20.0.6:80/test1')
print(response)
print(response.text)
