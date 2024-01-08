import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Start of {func.__name__}')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'work time(sec) = {end - start}')
        return result

    return wrapper
