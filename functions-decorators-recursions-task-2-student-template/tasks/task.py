from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here
    """
    result = []
    for item in sequence:
        if isinstance(item, int):
            result.append(item)
        else:
            result += linear_seq(item)
    return result

if __name__ == '__main__':
    sequence = [1,2,3,[4,5, (6,7)]]
    print(linear_seq(sequence))
    # [1,2,3,4,5,6,7]
