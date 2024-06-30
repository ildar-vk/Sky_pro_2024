def log(filename):
    """
    Это определение функции log,
    которая принимает имя файла в качестве аргумента.

    """

    def decorator(func):
        """
        Внутри функции log определяется ещё одна функция decorator,
        которая принимает другую функцию func в качестве аргумента.
        """

        def wrapper(*args, **kwargs):
            """
            Внутри функции decorator определяется функция wrapper,
            которая принимает любое количество позиционных и именованных аргументов.
            Эта функция выполняет действия до и после вызова функции func.
            """
            currency = "USD"  # В функции wrapper определяется переменная currency со значением "USD"
            result = func(
                *args, **kwargs
            )  # Вызывается функция func с переданными аргументами, и результат сохраняется в переменной result.
            with open(
                filename, "a"
            ) as file:  # Открывается файл с именем, переданным в функцию log, в режиме добавления ('a')
                file.write(
                    f"Function '{func.__name__}' was called. Result: {result}. Currency: {currency}\n"
                )  # Записывается информация о вызове функции в файл, включая имя вызванной функции,
                # результат выполнения и значение переменной currency.

            return result  # Возвращается результат выполнения функции func.

        return wrapper  # Функция decorator возвращает функцию wrapper.

    return decorator  # Функция log возвращает функцию decorator.


@log("log.txt")
def add(a, b):
    return a + b


print(add(2, 3))
