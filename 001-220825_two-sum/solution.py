# solution.py

from typing import List

def twoSumPointers(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    arr = sorted((val, i) for i, val in enumerate(nums))  
    
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l][0] + arr[r][0]
        if s == target:
            i1, i2 = arr[l][1], arr[r][1]
            return [i1, i2]  
        if s < target:
            l += 1
        else:
            r -= 1
    return []

def twoSumHash(nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []

if __name__ == "__main__":
    example = [5, 7, 10]
    target = 15
    print(twoSumPointers(example, target))
    print(twoSumHash(example, target))
