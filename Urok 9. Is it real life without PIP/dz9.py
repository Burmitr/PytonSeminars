import requests
from bs4 import BeautifulSoup as bs

url = 'https://anekdoty.ru/'
response = requests.get(url).text
soup = bs(response, 'html.parser')
anekdot = soup.find('div', class_='holder-body')
print(anekdot.text)