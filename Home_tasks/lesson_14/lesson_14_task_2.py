"""Write a decorator that takes a list of c
and replaces them with * inside the decorated function

"""


def stop_words(words: list):
    def stop_decorator(func):
        def wrapper(*args, **kwargs):
            slogan = func(*args, **kwargs).split()
            for i in range(len(slogan)):
                if slogan[i] in words:
                    slogan[i] = '*'
            return ' '.join(slogan)
        return wrapper
    return stop_decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW !"


assert create_slogan("Steve") == "Steve drinks * in his brand new * !"
