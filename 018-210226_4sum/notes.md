# 4Sum (21-02-2026)  
LeetCode: [4Sum](https://leetcode.com/problems/4sum/)

---

## First idea: Sorting + Pointers (baseline)

- Complexity: 
      - Time: O(n³) — three nested loops (i, j, two-pointer scan)
      - Space: O(1) extra (excluding output)
- Algorithm:
      - Sort the array.
      - Loop i from 0 → n-4, skipping duplicates.
      - Loop j from i+1 → n-3, skipping duplicates.
      - Use two pointers (left = j+1, right = n-1) to find pairs that sum with nums[i] + nums[j] to reach the target.
      - Skip duplicates for left and right after finding a valid quadruplet.
- Strengths:
      - Simple, readable, easy to implement.
      - Handles duplicates correctly.
      - Works for any target (not just zero).
- Weaknesses:
      - Does not prune unnecessary iterations — checks all combinations.
      - Slightly slower for large arrays compared to an optimized approach.
      - Could do unnecessary work even when sums are obviously too large or too small.

---

## Second (and better) idea: Sorting + Pointers + Pruning (Optimized)

- Complexity:
      - Time: O(n³) — still three nested loops, but with pruning.
      - Space: O(1) extra (excluding output)
- Algorithm:
      - Sort the array.
      - Loop i from 0 → n-4, skipping duplicates. Apply early break/continue pruning based on minimum and maximum sums possible.
      - Loop j from i+1 → n-3, skipping duplicates. Apply similar pruning for j.
      - Use two pointers (left = j+1, right = n-1) to find pairs. Skip duplicates.
- Strengths:
      - Efficient: reduces unnecessary iterations via early pruning.
      - till readable and maintainable.
      - Handles duplicates correctly.
      - Especially faster when the array is large or contains extreme values.
- Weaknesses:
      - Slightly more complex code due to pruning conditions.
      - Gains are input-dependent; for small arrays, improvement is minimal.
 