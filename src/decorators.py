def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename is None:
                print(f"Function '{func.__name__}' was called. Result: {result}.")
            else:
                with open(filename, "a") as file:
                    file.write(f"Function '{func.__name__}' was called. Result: {result}.\n")
            return result
        return wrapper
    return decorator

@log("log.txt")
def add(a, b):
    return a + b


print(add(2, -8))
