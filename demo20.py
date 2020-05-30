import requests

r = requests.get('https://static3.scrape.center/', auth=('admin', 'admin'))
print(r.status_code)
