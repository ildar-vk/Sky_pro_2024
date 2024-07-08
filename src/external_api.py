import os

import requests


def convert_currency(amount, currency):
    api_key = os.getenv("API_KEY")
    base_currency = "USD" if currency == "USD" else "EUR"
    url = (f'https://api.apilayer.com/exchangerates_data-api/convert?access_key={api_key}'
           f'&from={currency}&to=RUB&amount={amount}')

    response = requests.get(url)
    data = response.json()

    return data["result"]
