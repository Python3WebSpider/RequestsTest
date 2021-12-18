import requests

r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
print(r.status_code)
