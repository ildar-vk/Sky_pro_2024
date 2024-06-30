# Sky\_pro\_2024


# Описание проекта


Мы создали модуль decorators , в котором будут располагаться декораторы. Написали декоратор log который принимает один необязательный аргумент filename ,который определяет путь к файлу, в который будут записываться логи.

## Функции:


1. `def log(filename):` - Это определение функции `log`, которая принимает имя файла в качестве аргумента.
2. `def decorator(func):` - Внутри функции `log` определяется ещё одна функция `decorator`, которая принимает другую функцию `func` в качестве аргумента.
3. `def wrapper(*args, **kwargs):` - Внутри функции `decorator` определяется функция `wrapper`, которая принимает любое количество позиционных и именованных аргументов. Эта функция выполняет действия до и после вызова функции `func`.

## Тесты


В этом ДЗ мы определили две функции-теста(test_log_file-creation, test_add_functionality).
Первая функция проверяет создание файла лога после вызова функции `add`, а вторая функция проверяет корректность работы функции `add`.
