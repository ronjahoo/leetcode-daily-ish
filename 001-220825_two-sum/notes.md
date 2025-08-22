# Two Sum (22-08-2025)
LeetCode: [Two sum](https://leetcode.com/problems/two-sum/)

## First idea: Pointers

- Complexity of O(nlogn)
- Algorithm:
    1. Combine values and indexes as pairs
    2. Sort the structure
    3. Use two pointers: left and right
    4. If sum of the two values is less than target, move the left pointer
    5. If the sum of the two values is more than target, move the right pointer
    6. If the sum of the two values is same as target, return the indexes
- Strengths:
    - Clear
    - Two-pointer pattern is old and familiar
- Weaknesses:
    - Sorting brings complexity up to O(nlogn)
    - Indexes may return in the "wrong" order

## Second (and better) idea: Hashmap

- Complexity of O(n)
- Algorithm:
    1. Idea is to go through the list only once
    2. Calculate complement need = target - x for each value
    3. If need is already saved, the pair of indexes is found
    4. Otherwise, save x to the dictionary and continue the list
- Strengths:
    - No need for sorting, so this one is fast
- Weaknesses:
    - This takes O(n) extra space