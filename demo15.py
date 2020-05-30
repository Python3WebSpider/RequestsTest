import requests

response = requests.get('https://static2.scrape.center/', verify=False)
print(response.status_code)