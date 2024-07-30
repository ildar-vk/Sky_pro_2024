import logging
from functools import wraps
"""
from functools import wraps: Импортирует функцию wraps из модуля functools.
wraps используется для копирования метаданных
(например, имени функции) из одной функции в другую.
from typing import Callable, Any: Импортирует типы Callable и Any из модуля typing.
Callable используется для определения типа функции, а Any — для указания на любой тип данных.

"""


def log(filename: str | None = None):

    def _log(msg: str) -> None:
        """Объявляет вспомогательную функцию _log, которая принимает строку msg и не возвращает ничего (None).
        Эта функция отвечает за логирование сообщений.
        """
        if filename is None:
            print(msg)
        else:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(msg + "\n")

    def decorator(func):
        """
            Декоратор @wraps(func)
        используется для обновления метаданных обернутой функции wrapper с метаданными функции func.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Функция wrapper возвращает результат выполнения функции func.
            """
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                msg = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                _log(msg)  # Передает эту строку в функцию _log для записи в журнал или обработки.
                raise
            else:
                msg = f"{func.__name__} ok"
                _log(msg)  # Передает эту строку в функцию _log для записи в журнал или обработки.
                return result

        return wrapper

    return decorator


def logger_masks(func):
    """
    Функция декорированая  которая принимает другую функцию в качестве аргумента.
    С реализацие записи логовв определенном формате в файл
    с последующпй перезаписью логов при вызове функции вновь
    """
    logging.basicConfig(
        filename="C:\\Users\\Professional\\PycharmProjects\\Sky_pro_2024_1\\logs\\masks.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filemode="w",  # при каждом запуске функции журнал будет перезаписан.
    )
    logger = logging.getLogger("masks")

    def wrapper(*args, **kwargs):
        logger.info(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} returned: {result}")
        return result

    return wrapper


import logging


def logger_utils(func):
    # Настройка логирования
    logging.basicConfig(
        filename="C:\\Users\\Professional\\PycharmProjects\\Sky_pro_2024_1\\logs\\utils.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Получаем логгер
    logger = logging.getLogger("utils")

    # Отключаем вывод логов в консоль
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    def wrapper(*args, **kwargs):
        logger.info(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} returned: {result}")
        return result

    return wrapper


