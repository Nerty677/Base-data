import sqlite3

# Создание базы данных и таблицы
conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute('''CREATE TABLE weather (date_time TEXT, temperature REAL)''')
conn.commit()
conn.close()

import requests
from bs4 import BeautifulSoup

# URL сайта с погодой
url = 'https://sinoptik.ua/soniachne'

# Отправка GET-запроса на сайт
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Поиск информации о температуре
temperature = soup.find('span', class_='temperature').text
print(f"Current temperature: {temperature}")

import datetime

# Получение текущей даты и времени
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Внесение данных в базу данных
conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", (current_datetime, temperature))
conn.commit()
conn.close()

import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime

# Создание базы данных и таблицы
conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute('''CREATE TABLE weather (date_time TEXT, temperature REAL)''')
conn.commit()
conn.close()

# URL сайта с погодой
url = 'https://sinoptik.ua/soniachne'

# Отправка GET-запроса на сайт
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Поиск информации о температуре
temperature = soup.find('span', class_='temperature').text
print(f"Current temperature: {temperature}")

# Получение текущей даты и времени
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Внесение данных в базу данных
conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", (current_datetime, temperature))
conn.commit()
conn.close()
