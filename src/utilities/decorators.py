from time import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{end - start:.4f}s")

        return result

    return wrapper
