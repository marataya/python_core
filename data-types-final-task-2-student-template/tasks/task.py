from typing import List


def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    result = [None] * (row_end - row_start + 1)
    for i in range(len(result)):
        result[i] = []
    for i in range(len(result)):
        for j in range(column_end - column_start + 1):
            result[i].append((row_start + i) * (column_start + j))
    return result


if __name__ == '__main__':
    print(check(2, 4, 3, 7))
