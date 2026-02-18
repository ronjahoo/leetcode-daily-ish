# Letters Combinations of a Phone Number (18-02-2026)  
LeetCode: [Letters Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

---

## First idea: Basic Backtracking Template

- Complexity: 
  - Time: O(4ⁿ) (worst case each digit has 4 letters)
  - Space: O(4ⁿ) for storing results + O(n) recursion stack
  - Since n ≤ 4, this is effectively constant time in practice.
- Algorithm:
  - Build a dictionary mapping digits (2–9) to their corresponding letters.
  - Convert the input string into a list of letter lists (char_lists).
  - Use backtracking (DFS):
    - Build combinations character by character.
    - When the current path length equals number of digits, append to result.
    - Backtrack by removing last added character.
- Strengths:
  - Very clear recursive structure.
  - Easy to reason about.
  - Classic backtracking template (useful in interviews).
  - Easy to extend for similar problems.
- Weaknesses:
  - Slightly more verbose.
  - Builds an intermediate char_lists structure (extra memory).
  - Uses int() conversion unnecessarily.
  - Recursion overhead (though small here).

---

## Second (and better) idea:  Iterative Cartesian Product

- Complexity:
  - Time: O(4ⁿ)
  - Space: O(4ⁿ) for result storage
  - No recursion stack.
- Algorithm:
  - Store digit → letters mapping using string keys.
  - Start with result = [""].
  - For each digit:
    - Create a temporary list.
    - Append every possible letter to every existing prefix.
  - Replace result with the new list each iteration.
  - This is essentially computing a Cartesian product iteratively.
- Strengths:
  - No recursion.
  - Cleaner and shorter.
  - No unnecessary conversions.
  - More Pythonic.
  - Slightly better memory usage.
- Weaknesses:
  - Slightly less intuitive if unfamiliar with iterative combination building.
  - Still exponential (cannot be avoided).
 