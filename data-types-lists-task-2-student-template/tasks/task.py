from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    result = ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 ==0 else x for x in range(1, n + 1)]

    return result

if __name__ == '__main__':
    print(get_fizzbuzz_list(50))
