from typing import List

def product(nums):
    if not nums:
        return 1
    return nums[0] * product(nums[1:])

def foo(nums: List[int]) -> List[int]:
    product1 = product(nums)
    result = []
    for el in nums:
        result.append(int(product1 / el))
    return result

if __name__ == '__main__':
    print(foo([1, 2, 3, 4, 5]))
    print(foo([1, 2, 3]))
