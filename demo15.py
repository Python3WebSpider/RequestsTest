import requests

response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)