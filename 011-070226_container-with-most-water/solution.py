import math
from typing import List

def maxAreaFirst(height: List[int]) -> int:
    maxArea = 0
    currentArea = 0
    j = len(height) - 1
    i = 0

    while i < j:
        currentArea = (j-i) * min(height[i], height[j])
        if (currentArea > maxArea):
            maxArea = currentArea
        if (height[i] < height[j]):
            i += 1
        else:
            j -= 1
    
    return maxArea

def maxAreaSecond(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    maxArea = 0

    while i < j:
        left, right = height[i], height[j]
        h = left if left < right else right
        currentArea = (j - i) * h
        if currentArea > maxArea:
            maxArea = currentArea
        if left < right:
            prev = left
            i += 1
            while i < j and height[i] <= prev:
                i += 1
        else:
            prev = right
            j -= 1
            while i < j and height[j] <= prev:
                j -= 1

    return maxArea

if __name__ == "__main__":
    height1 = [1,8,6,2,5,4,8,3,7]
    height2 = [1,1]

    print(maxAreaFirst(height1))
    print(maxAreaFirst(height2))
    print(maxAreaSecond(height1))
    print(maxAreaSecond(height2))

