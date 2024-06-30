import src.decorators


def test_add_functionality():
    result = src.decorators.add(2, -8)
    if result == -6:
        print("Test Passed: Add functionality test")
    else:
        print("Test Failed: Add functionality test")


def test_add_log_file():
    with open("log.txt", "r") as file:
        logs = file.readlines()
        last_log = logs[-1].strip()
        expected_log = "Function 'add' was called. Result: -6."
        assert last_log == expected_log
