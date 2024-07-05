import json


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

