# Урок 25: Работа с интернетом и API (базово)

# 🔸 Цели урока:

# - Понять, что такое API и как через него получать данные с сайтов
# - Научиться использовать библиотеку requests
# - Научиться обрабатывать ответы от серверов
# - Попрактиковаться в работе с открытыми источниками: погода, курсы валют и др.

# 🔸 Что такое API

# API (Application Programming Interface) — это интерфейс, через который одна программа может «разговаривать» с другой.
# Веб-API позволяет получать данные от сайтов в формате JSON (чаще всего).

# Примеры открытых API:
# - Погода (OpenWeatherMap)
# - Курсы валют (exchangerate.host, НБРК и т.д.)
# - Новости, цитаты, мемы, факты и т.п.

# 🔸 Модуль requests

# Библиотека requests позволяет отправлять HTTP-запросы (GET, POST и др.) и получать ответы.

# 📦 Установка:
# pip install requests

# Пример базового запроса:

import requests

def basic_request():
    url = "https://api.example.com/data"
    response = requests.get(url)
    print("Status code:", response.status_code)  # 200
    print("Raw response:", response.text)        # сырой текст ответа
    print("Parsed response:", response.json())    # преобразует JSON в словарь

# 🔸 Важные методы requests

# HTTP методы:
# GET — метод для получения данных с сервера (чтение информации).
# POST — метод для отправки данных на сервер (например, для отправки формы).

# Метод           | Назначение
# ----------------|----------------------------------
# get(url)        | Отправка GET-запроса для получения данных с сервера.
# post(url, ...)  | Отправка POST-запроса для отправки данных на сервер.
# response.text   | Ответ в виде строки, полученный от сервера.
# response.json() | Ответ, преобразованный в Python-словарь.
# response.status_code | Код ответа (например, 200 — ОК, 404 — не найдено, и другие).

def get_data_from_api():
    url = "https://api.example.com/data"
    response = requests.get(url)
    return response.status_code, response.text

# 🔸 Пример метода GET

def fetch_weather(city):
    # Получаем погоду для указанного города
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    response = requests.get(url)
    return response.json()

# 🔸 Пример метода POST

def send_message(user_id, message):
    url = "https://api.example.com/messages"
    payload = {
        "user_id": user_id,
        "message": message
    }
    response = requests.post(url, data=payload)
    return response.json()

# 🔸 Обработка ошибок

def safe_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # вызовет ошибку, если статус не 2xx
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {e}"

# Пример обработки ошибки:
# response = safe_request("https://invalid-url.com")

# 🔸 Практика

def get_random_quote():
    url = "https://api.quotable.io/random"
    return safe_request(url)

def get_exchange_rate():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=KZT"
    return safe_request(url)

def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather?q=Almaty&appid=YOUR_API_KEY"
    return safe_request(url)

# 🔸 Этические правила и безопасность

# - Никогда не отправляй лишние запросы без необходимости (может быть блокировка)
# - Не храни API-ключи в открытом виде
# - Уважай ограничения (лимиты) на количество запросов

if __name__ == "__main__":
    # Пример использования
    print(get_random_quote())
    print(get_exchange_rate())
    print(get_weather())


