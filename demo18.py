import requests

r = requests.get('https://www.httpbin.org/get', timeout=1)
print(r.status_code)
