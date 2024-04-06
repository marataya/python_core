from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Add your code here or call it from here
    """
    result = []
    idx, prev_idx = 0, 0

    for i in range(len(indexes)):
        if indexes[i] < 0 or indexes[i] >= len(s) or (i > 0 and indexes[i] < indexes[i-1]):
            continue
        idx = indexes[i]
        result.append(s[prev_idx:idx])
        prev_idx = idx
    if idx < len(s) - 1:
        result.append(s[idx:])
    print(result)
    return result

if __name__ == '__main__':
    assert split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == ["python", "is", "cool", ",", "isn't", "it?"]
    assert split_by_index("no luck", [42]) == ["no luck"]
