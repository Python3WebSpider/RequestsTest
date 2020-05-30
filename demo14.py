import requests

response = requests.get('https://static2.scrape.center/')
print(response.status_code)