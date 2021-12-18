import requests

r = requests.get('https://www.httpbin.org/get')
print(r.text)


import requests  

data = {  
    'name': 'germey',  
    'age': 25
}  
r = requests.get('https://httpbin.org/get', params=data)  
print(r.text)