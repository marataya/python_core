from typing import Tuple
import time
import random

def get_tuple(num: int) -> Tuple[int]:
    begin = time.time()
    result = (int(d) for d in str(num))
    end = time.time()
    print(f'{end - begin} sec')
    return tuple(result)

if __name__ == '__main__':
    n = 5000
    number = int(''.join([str(random.randint(0, 9)) for _ in range(4300)]))
    print(get_tuple(number))
