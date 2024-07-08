import json
import unittest
from unittest.mock import patch

from src.external_api import convert_currency
from src.utils import process_transaction


def test_input_json():
    filename = "operation.json"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if "[" not in content and "]" not in content:
                print("Файл не содержит списков")
            else:
                with open(filename, encoding="utf-8") as f:
                    data = json.load(f)
                    print(data)
    except FileNotFoundError:
        print("Файл не найден")


class TestConvertCurrency(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_convert_currency(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {"result": 75.0}  # Пример вымышленного результата
        converted_amount = convert_currency(50, "USD")
        self.assertEqual(converted_amount, 75.0)


if __name__ == "__main__":
    unittest.main()


class TestProcessTransaction(unittest.TestCase):

    @patch("src.utils.convert_currency")
    def test_process_transaction(self, mock_convert_currency):
        file_json = {"amount": 100, "currency": "USD"}

        mock_convert_currency.return_value = 75

        result = process_transaction(file_json)

        self.assertEqual(result, 75)
