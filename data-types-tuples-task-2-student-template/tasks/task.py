from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    result = []

    for i in range(len(lst)):
        if i + 1 < len(lst):
            tuple1 = lst[i], lst[i+1]
            result.append(tuple1)
    return result

if __name__ == '__main__':
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))
