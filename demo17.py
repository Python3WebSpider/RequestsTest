import logging
import requests

logging.captureWarnings(True)
response = requests.get('https://static2.scrape.center/', verify=False)
print(response.status_code)