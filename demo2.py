import requests

r = requests.get('https://www.httpbin.org/get')
r = requests.post('https://www.httpbin.org/post')
r = requests.put('https://www.httpbin.org/put')
r = requests.delete('https://www.httpbin.org/delete')
r = requests.patch('https://www.httpbin.org/patch')
