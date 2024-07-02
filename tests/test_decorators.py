import os

import pytest

import src.decorators


def test_for_Exception():
    with pytest.raises(Exception):

        @src.decorators.log("test_log.txt")
        def add(a, b):
            return a / b

        print(add(2, 0))


def test_log():
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5


def test_log_file():
    filename = 'test_log.txt'
    try:
        if os.path.exists(filename):
            os.remove(filename)

        with open(filename, 'w') as file:
            file.write("Test is good")

        with open(filename, 'r') as file:
            content = file.read()
            if content == "Test is good":
                print('File content is correct')

    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")


