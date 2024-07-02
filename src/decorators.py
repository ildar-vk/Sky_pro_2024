def log(filename=None):
    """
    Декоратор log логирует вызовы функций в файл или в консоль.

    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"Function '{func.__name__}' ok \n")
                else:
                    with open(filename, "a") as file:
                        file.write(f"Function '{func.__name__}' ok \n")
                    return result
            except Exception as Err:
                if filename is None:
                    print(f"Function '{func.__name__}'  = {Err} of {args or kwargs}  \n")

                else:
                    with open(filename, "a") as file:
                        file.write(f"Function '{func.__name__}' = {Err} of {args or kwargs} \n")
                raise


        return wrapper

    return decorator


# @log("log.txt")
# def add(a, b):
#     return a / b
#
#
# print(add(2,0))