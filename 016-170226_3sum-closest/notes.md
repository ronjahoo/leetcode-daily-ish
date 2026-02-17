# 3Sum (17-02-2026)  
LeetCode: [3Sum Closest](https://leetcode.com/problems/3sum-closest/)

---

## First idea: Based directly on the previous 3Sum code

- Complexity:
  - Time: O(n²)
  - Space: O(1)
- Algorithm:  
  - Sort the input array.
  - Initialize closest as the sum of the first three elements (valid baseline).
  - Iterate with index i as an anchor.
  - Use two pointers: left = i + 1 and right = n - 1
  - Compute total = nums[i] + nums[left] + nums[right].
    - If total == target, return immediately (optimal).
    - If total < target, move left forward.
    - If total > target, move right backward.
  - Update closest whenever a smaller absolute difference is found.
- Strengths: 
  - Clear invariant: closest always stores the best sum seen so far.
  - Early return on exact match.
  - Efficient O(n²) time.
  - Easy to reason about and debug.
- Weaknesses: 
  - Recomputes abs(closest - target) repeatedly.
  - Slight redundancy in updating logic inside both branches.
  - Stores full sum rather than difference (less mathematically explicit).

---

## Second (and better) idea: invariant-driven solution

- Complexity:
  - Time: O(n²)
  - Space: O(1)
- Algorithm:
  - Sort the array.
  - Track deviation instead of raw sum: closest_diff = float("inf")
  - For each anchor i, apply two-pointer sweep.
  - Compute: diff = total - target
  - Update closest_diff if abs(diff) improves.
  - Move pointers based on the sign of diff.
  - Return target + closest_diff.
- Strengths:
  - Cleaner mathematical invariant solution
  - Avoids repeated subtraction of target
  - More explicit control over distance metric.
  - Slightly clearer reasoning about monotonic pointer movement.
- Weaknesses:
  - Slightly more abstract to read at first glance.
  - Same asymptotic complexity as first solution.
 