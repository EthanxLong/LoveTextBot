import requests
from bs4 import BeautifulSoup

page = requests.get('https://weather.com/weather/today/l/455927f509a77fa8a9f21baf90efba1092b835f17ab4e454052afb57594c0c1d')
soup = BeautifulSoup(page.content, 'html.parser')

# weatherToday = soup.find_all(class_='CurrentConditions--tempValue--3KcTQ')
temperature = soup.select_one("span[data-testid='TemperatureValue']").text
description = soup.select_one("div[data-testid='wxPhrase']").text
# precipdesc = soup.select_one("div[data-testid='precipPhrase']").text


temp = int(temperature.strip("°"))