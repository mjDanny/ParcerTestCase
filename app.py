import requests
from bs4 import BeautifulSoup
import json

# URL сайта
base_url = "https://quotes.toscrape.com/page/{}/"

# Список для хранения данных
data = []

# Цикл по страницам (от 1 до 10)
for page in range(1, 11):
    url = base_url.format(page)
    print(f"Сбор данных с {url}")

    # Отправка запроса
    response = requests.get(url)
    response.raise_for_status()  # Проверка на ошибки

    # Парсинг HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлечение данных о цитатах
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        author_link = quote.find('a')['href']
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        # Добавление данных в список
        data.append({
            'text': text,
            'author': author,
            'author_link': author_link,
            'tags': tags
        })

# Сохранение данных в JSON-файл
with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Сбор данных завершен. Результат сохранен в quotes.json")