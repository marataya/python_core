from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here
    """
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += seq_sum(item)
        else:
            total += item
    return total


if __name__ == '__main__':
    sequence = [1, 2, 3, [4, 5, (6, 7)]]

    print(seq_sum(sequence))
