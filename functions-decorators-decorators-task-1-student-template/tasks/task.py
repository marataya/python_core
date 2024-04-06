from typing import Dict
from time import time, sleep

execution_time: Dict[str, float] = {}

def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        execution_time[fn.__name__] = end - start
        return result
    return wrapper

@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b


if __name__ == '__main__':
    func_add(10, 20)
    # 30
    print(execution_time['func_add'])
    # 0.212341254
