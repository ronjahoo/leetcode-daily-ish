# 3Sum (16-02-2026)  
LeetCode: [3Sum](https://leetcode.com/problems/3sum/)

---

## First idea: Sorting + Two Pointers (baseline)

- Complexity:
  - Time: O(n²)
  - Space: O(1) extra (excluding output)
- Algorithm:  
  - Sort the input array.
  - Iterate index i from 0 to n-3.
  - Skip duplicate values for i.
  - Use two pointers:
    - left = i + 1
    - right = n - 1
  - Compute total = nums[i] + nums[left] + nums[right]
    - If total == 0: append triplet and skip duplicate left and right
    - If total < 0: move left
    - If total > 0: move right
  - Continue until pointers meet.
- Strengths: 
  - Clean and readable.
  - Optimal time complexity for general case.
  - Correct duplicate handling
- Weaknesses: 
  - Always scans the full remaining range for each i.
  - Does not prune obviously impossible cases early.
  - Slightly higher constant factor than necessary.

---

## Second (and better) idea: Sorting + Two Pointers + Pruning (Optimized)

- Complexity:
  - Time: O(n²) worst case
  - Space: O(1) extra (excluding output)
- Algorithm:
  - Same as first approach, but with additional early stopping rules:
    - If nums[i] > 0, break (no possible zero-sum ahead).
    - If smallest possible triplet for this i is already > 0, break
    - If largest possible triplet for this i is still < 0, skip
    - Then run the same two-pointer search.
- Strengths:
  - Same theoretical complexity.
  - Faster in practice on many inputs.
  - Reduces unnecessary pointer scans.
  - Better constant-factor efficiency.
- Weaknesses:
  - Slightly more complex logic.
  - Gains only affect average performance, not worst-case.
 