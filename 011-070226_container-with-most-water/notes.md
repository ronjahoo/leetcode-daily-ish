# Container With Most Water (07-02-2026)  
LeetCode: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## First idea: Two pointers

- Complexity:
  - Time: O(n)
  - Space: O(1)
- Algorithm:  
  - Initialize two pointers: i = 0, j = n - 1.
  - While i < j:
    - Compute area: (j - i) * min(height[i], height[j]), update maxArea.
    - Move the pointer at the shorter height inward: if height[i] < height[j] → i += 1, else → j -= 1
  - Return maxArea.
- Strengths: 
  - Optimal asymptotic runtime (linear) and constant memory.
  - Very compact and readable; minimal moving parts.
  - Correctness intuition is clean: the shorter wall limits the area, so only replacing it can help.
- Weaknesses: 
  - Still checks every pointer position step-by-step (even if many heights are clearly “non-improving”).
  - Uses min() each iteration (tiny cost; not a real issue, but it exists).
  - Slightly less intuitive than brute force unless you internalize the “limiting height” argument.

---

## Second (and better) idea: Two pointers + skipping dominated heights

- Complexity:
  - Time: O(n) worst-case (each pointer only moves inward, and skips don’t revisit indices)
  - Space: O(1)
- Algorithm:
  - Same two-pointer core: i left, j right, compute current area each step.
  - After computing area:
    - If left < right, move i inward past all heights <= left (since width shrinks and min-height won’t improve, those can’t beat the current best with this right boundary).
    - Else, move j inward past all heights <= right for the symmetric reason.
    - This “jumping” prunes obviously hopeless candidates.
- Strengths:
  - Often faster in practice on inputs with long non-increasing runs / plateaus (fewer iterations).
  - Still simple, still O(1) memory, still O(n) time, but with less “busywork.”
  - Makes the key insight explicit: only a strictly taller replacement on the limiting side can compensate for reduced width.
- Weaknesses:
  - More logic → easier to introduce off-by-one mistakes if not careful.
  - In worst-case patterns (e.g., alternating up/down), skipping may not skip much, so it behaves like the baseline.
  - Slightly denser to read/debug than the first version.
 