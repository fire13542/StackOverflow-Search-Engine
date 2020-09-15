import requests
from bs4 import BeautifulSoup

start_url = 'https://stackoverflow.com/questions/'

links = requests.get(start_url)
content = BeautifulSoup(links.text, 'lxml')
print(content)
