from typing import List
import math

def mergeUntilMedian(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)
    total = m + n
    stop = total // 2  
    i = j = 0
    prev = curr = 0

    for _ in range(stop + 1):
        prev = curr
        if i < m and (j >= n or nums1[i] <= nums2[j]):
            curr = nums1[i]; i += 1
        else:
            curr = nums2[j]; j += 1

    if total % 2 == 1:
        return float(curr)
    else:
        return (prev + curr) / 2.0


def BinarySearchSolution(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    m, n = len(A), len(B)

    if m > n:
        A, B, m, n = B, A, n, m

    left_total = (m + n + 1) // 2
    lo, hi = 0, m

    INF = math.inf

    while lo <= hi:
        i = (lo + hi) // 2
        j = left_total - i

        A_left  = -INF if i == 0 else A[i - 1]
        A_right =  INF if i == m else A[i]
        B_left  = -INF if j == 0 else B[j - 1]
        B_right =  INF if j == n else B[j]

        if A_left <= B_right and B_left <= A_right:
            if (m + n) % 2 == 1:
                return float(max(A_left, B_left))
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
        elif A_left > B_right:
            hi = i - 1
        else:
            lo = i + 1

    raise ValueError("Should not reach here")


if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2] 

    result_merge = mergeUntilMedian(nums1, nums2)
    result_binary = BinarySearchSolution(nums1, nums2)

    print("Merge result:", result_merge)
    print("Binary search result:", result_binary)
