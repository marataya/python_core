import math
from typing import Union

NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  result = None
  # add your code here
  result = round((12 * a + 25 * b) / (1 + a**(2**b)),2)
  # return f'{result:.2}'
  return result

if __name__ == '__main__':
    print(some_expression_with_rounding(1.4, 2.55))
    print(some_expression_with_rounding(13.222, 3.533))
    print(some_expression_with_rounding(6.147, 0.2))
    print(some_expression_with_rounding(14.222, 4.66))
