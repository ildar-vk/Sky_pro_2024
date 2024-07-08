import json

import src
from src.external_api import convert_currency


def input_json(file_json):
    try:
        with open(file_json, "r", encoding="utf-8") as file:
            content = file.read()
            if "[" not in content and "]" not in content:
                print("Файл не содержит списков")
                empty_list = []
                return empty_list
            else:
                with open(file_json,encoding="utf-8") as f:
                    data = json.load(f)
                    print("Файл со списками")
                return data
    except FileNotFoundError:
         empty_list = []
         print("Файл не найден")
         return empty_list

def process_transaction(file_json):
    amount = file_json['amount']
    currency = file_json['currency']

    if currency in ['USD', 'EUR']:
        amount_rub = convert_currency(amount, currency)
    else:
        amount_rub = amount

    return amount_rub


