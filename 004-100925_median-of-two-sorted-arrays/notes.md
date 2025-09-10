# Median of Two Sorted Arrays (10-09-2025)  
LeetCode: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## First idea: merge lists until the median point

- Complexity:  
  - Time: O(m+n) (merge until reaching the median)  
  - Space: O(1) if only tracking the last two values, otherwise O(m+n) if storing the whole merged array  

- Algorithm:  
  1. Initialize two pointers (i, j) at the start of both arrays.  
  2. Move forward by always taking the smaller element, keeping track of the last two chosen values.  
  3. Stop once you’ve reached the median index.  
  4. If the total length is odd, the median is the last chosen value.  
  5. If the total length is even, the median is the average of the last two chosen values.  

- Strengths:  
  - Simple to understand and implement.   

- Weaknesses:  
  - Inefficient for long arrays (lots of unnecessary merging).  

---

## Second (and better) idea: binary search

- Complexity:  
  - Time: O(log min(m,n))  
  - Space: O(1)  

- Algorithm:  
  1. Always binary search on the smaller array.  
  2. Choose a partition index `i` in the smaller array; compute `j = (m+n+1)//2 − i` for the other array.  
  3. Check whether the maximum of the left halves ≤ the minimum of the right halves.  
  4. If so, the median is either `max(left)` (odd case) or `(max(left) + min(right)) / 2` (even case).  
  5. If not, adjust the binary search window left or right.  

- Strengths:  
  - No merging or extra memory allocation.  
  - Efficient even for large inputs.  

- Weaknesses:  
  - More complex to implement, prone to off-by-one and boundary errors.  
  - Requires careful handling of edge cases (e.g., using ±∞ for boundaries).  
