import json

import src


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

def input_transaction(transaction):
    if transaction in ['USD', 'EUR']:
        # Вызов внешнего API для обработки транзакции
        amount = src.external_api(transaction)
        return amount
    else:
        return "Unsupported currency"
