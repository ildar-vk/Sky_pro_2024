import json

from unittest.mock import Mock, patch
from src.utils import process_transaction

def test_input_json():
    filename = "operation.json"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if "[" not in content and "]" not in content:
                print("Файл не содержит списков")
            else:
                with open(filename,encoding="utf-8") as f:
                    data = json.load(f)
                    print(data)
    except FileNotFoundError:
        print("Файл не найден")



def test_process_transaction():
    # Создание мок-объекта для convert_currency
    mock_convert_currency = Mock(return_value=85)  # Замените 85 на ожидаемое значение

    # Патчим convert_currency в модуле your_module
    with patch('src.utils.convert_currency', mock_convert_currency):
        # Тестирование для случая с USD
        file_json_usd = {'amount': 100, 'currency': 'USD'}
        result_usd = process_transaction(file_json_usd)
        assert result_usd == 85, "Ошибка: Ожидается 85"

