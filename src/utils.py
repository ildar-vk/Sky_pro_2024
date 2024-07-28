import json


from src.decorators import logger_utils


@logger_utils
def input_json(file_json):
    """
    Это определение функции input_json,
    которая принимает аргумент: file_json (файл с данными о финансовых транзакциях)
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.
    """
    try:
        if file_path.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                logger_utils.info("Прочитан файл JSON")
                return data
        elif file_path.endswith(".csv"):
            data = []
            with open(file_path, newline="", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    data.append(row)
            logger_utils.info("Прочитан файл CSV")
            return data
        elif file_path.endswith(".xlsx"):
            data = pd.read_excel(file_path).to_dict(orient="records")
            logger_utils.info("Прочитан файл XLSX")
            return data
        else:
            logger_utils.error("Неподдерживаемый формат файла")
            return []
    except FileNotFoundError:
        logger_utils.error("Файл не найден")
        empty_list = []
        return empty_list
    except json.JSONDecodeError:
        logger_utils.error("Ошибка декодирования JSON")
        return []
    except Exception as e:
        # Здесь можно добавить дополнительные действия, если это необходимо
        logger_utils.error(f"Произошла ошибка: {e}")
        raise
