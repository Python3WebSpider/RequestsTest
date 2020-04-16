import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('https://httpbin.org/post', files=files)
print(r.text)
