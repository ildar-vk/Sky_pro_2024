
import json
import csv
import pandas as pd
from src.decorators import logger_utils
import re
@logger_utils
def input_data(file_path):
    """
    Эта функция принимает аргумент: file_path (файл с данными о финансовых транзакциях)
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        if file_path.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                logger_utils("Прочитан файл JSON")
                return data
        elif file_path.endswith(".csv"):
            data = []
            with open(file_path, newline="", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    data.append(row)
            logger_utils("Прочитан файл CSV")
            return data
        elif file_path.endswith(".xlsx"):
            data = pd.read_excel(file_path).to_dict(orient="records")
            logger_utils("Прочитан файл XLSX")
            return data
        else:
            logger_utils("Неподдерживаемый формат файла")
            return []
    except FileNotFoundError:
        logger_utils("Файл не найден")
        return []
    except json.JSONDecodeError:
        logger_utils("Ошибка декодирования JSON")
        return []
    except Exception as e:
        logger_utils(f"Произошла ошибка: {e}")
        raise

def filter_transactions_by_description(transactions, search_string):
    """Фильтрует транзакции по описанию."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction['description'])]

def count_operations_by_category(transactions, categories):
    """Считает количество операций по категориям."""
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        for category in categories:
            if category in transaction['description']:
                category_count[category] += 1
    return category_count

# Проверка работы функции с различными форматами файлов
json_data = input_data("C:\\Users\\Professional\\PycharmProjects\\Sky_pro_2024_1\\data\\operations.json")
print(json_data)

csv_data = input_data("C:\\Users\\Professional\\PycharmProjects\\Sky_pro_2024_1\\data\\data.transactions.csv")
print(csv_data)

xlsx_data = input_data("C:\\Users\\Professional\\PycharmProjects\\Sky_pro_2024_1\\data\\data.transactions_excel.xlsx")
print(xlsx_data)