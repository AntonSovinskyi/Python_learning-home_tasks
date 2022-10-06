"""Write a decorator that prints a function with arguments passed to it."""


from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        arguments = ', '.join(list(map(str, args)))
        print(f'{func.__doc__} {arguments}')
        return res
    return wrapper


@logger
def add(x, y):
    """add called with"""
    return x + y


@logger
def square_all(list_1):
    """return the squares of numbers in list"""
    return [x**2 for x in list_1]


add(4, 5)
square_all([1, 2, 3])
