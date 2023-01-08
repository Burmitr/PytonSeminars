import requests

# response = requests.get('https://mail.ru')
# print(response.headers)

# https://openweathermap.org

# API_key = '4321a3d417b53045aa1b6617c529c910'
# city_name = 'Бузулук'
#
# response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru")
# # print(response.headers)
# temp = response.json()
# temp1 = temp['main']
# print(temp1['temp'])

import requests
from bs4 import BeautifulSoup as bs

url = 'https://anekdoty.ru/'
response = requests.get(url).text
soup = bs(response, 'html.parser')
anekdot = soup.find('div', class_='holder-body')
print(anekdot.text)