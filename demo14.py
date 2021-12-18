import requests

response = requests.get('https://ssr2.scrape.center/')
print(response.status_code)