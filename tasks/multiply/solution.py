from functools import wraps


def multiply_by_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, *kwargs) * 2

    return wrapper


@multiply_by_2
def calculate1(n):
    return n + 1


def multiply_by_n(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, *kwargs) * n

        return wrapper

    return decorator


@multiply_by_n(4)
def calculate2(n):
    return n + 1


if __name__ == "__main__":
    assert calculate1(3) == 8
    assert calculate2(3) == 16
