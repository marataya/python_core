from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    result = {x:x**2 for x in range(1, num+1)}
    return result

if __name__ == '__main__':
    print(generate_squares(5))
