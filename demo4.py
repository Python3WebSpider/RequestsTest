import requests

data = {'name': 'germey', 'age': '25'}
r = requests.post("https://httpbin.org/post", data=data)
print(r.text)
