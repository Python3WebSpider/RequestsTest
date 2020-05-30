import requests

r = requests.get('https://httpbin.org/get', timeout=1)
print(r.status_code)
