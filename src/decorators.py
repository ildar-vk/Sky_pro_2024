from functools import wraps
from typing import Callable, Any

def log(filename: str | None = None) -> Callable:

    def _log(msg: str) -> None:
        if filename is None:
            print(msg)
        else:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(msg + '\n')

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                msg = f"'{func.__name__}'error : {str(e)} Inputs:{args or kwargs}"
                _log(msg)
                raise
            else:
                msg = f"Function '{func.__name__}' ok"
                _log(msg)
                return result

        return wrapper

    return decorator



