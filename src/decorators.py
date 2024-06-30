def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            currency = "USD"
            result = func(*args, **kwargs)
            with open(filename, "a") as file:
                file.write(f"Function '{func.__name__}' was called. Result: {result}. Currency: {currency}\n")
            return result

        return wrapper

    return decorator


@log("log.txt")
def add(a, b):
    return a + b


print(add(2, 3))
