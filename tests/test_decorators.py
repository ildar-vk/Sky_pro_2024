import src.decorators


def test_log_file_creation():
    with open("log.txt", "w") as file:
        file.write("Initial content")  # Создаем начальное содержимое файла
    src.decorators.add(2, 3)  # Вызываем функцию add
    with open("log.txt", "r") as file:
        content = file.read()
        if "Function 'add' was called." in content:
            print("Test Passed: Log file creation test")
        else:
            print("Test Failed: Log file creation test")


def test_add_functionality():
    result = src.decorators.add(2, 3)
    if result == 5:
        print("Test Passed: Add functionality test")
    else:
        print("Test Failed: Add functionality test")
