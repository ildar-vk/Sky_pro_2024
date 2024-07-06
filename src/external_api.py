

import os
from dotenv import load_dotenv
import requests

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
github_token = os.getenv('GITHUB_TOKEN')

# Проверка наличия токена
if github_token:
    # Создание заголовка с токеном доступа API
    headers = {'Authorization': f'token {github_token}'}

    # Параметры запроса для API Layer
    params = {'to': 'USD', 'from': 'EUR', 'amount': 100}

    # Отправка GET-запроса к API Layer
    response = requests.get('https://api.apilayer.com/exchangerates_data/convert', headers=headers, params=params)

    # Проверка статуса запроса
    if response.status_code == 200:
        # Обработка ответа
        print(response.json())
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
else:
    print("Токен отсутствует")

# import requests
#
# url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount=5"
#
# payload = {}
# headers= {
#   "apikey": "HqXJ7DYFwwRu4tZVPIlLF7xfOFSnO0y9"
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text