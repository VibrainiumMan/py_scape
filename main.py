import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.seek.co.nz/?tracking=CLP-WEB-SeekLandingPage')

print(request)

parser = BeautifulSoup(request.content, 'html.parser')
print(parser.prettify())
