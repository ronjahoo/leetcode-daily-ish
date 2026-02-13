# Longest Common Prefix (13-02-2026)  
LeetCode: [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

---

## First idea: Split the string and accumulate the prefix

- Complexity:
  - O(n*m) where n = number of strings and m = length of the shortest string
- Algorithm:  
  - Handle edge cases (empty list or empty string).
  - Compute the shortest string length.
  - For each index i up to that length:
    - Check if all strings have the same character at position i.
    - If yes → append to prefix.
    - If no → stop and return prefix.
  - Return accumulated prefix.
- Strengths: 
  - Straightforward logic.
  - Easy to reason about.
  - Stops immediately when mismatch occurs.
  - Works without sorting or modifying input.
- Weaknesses: 
  - Builds the prefix character by character (string concatenation can be slightly inefficient).
  - Slightly more verbose.
  - Requires two passes: one for min() and one for comparison.

---

## Second (and better) idea: Traverse the characters of the shortest string

- Complexity:
  - O(n*m) (same theoretical complexity, but often slightly cleaner in practice)
- Algorithm:
  - Handle edge cases.
  - Find the shortest string directly (min(strs, key=len)).
  - Iterate over its characters using enumerate.
  - For each index: If any string differs at that index → return prefix slice.
    - If no mismatch occurs → return shortest string.
- Strengths:
  - Cleaner and more Pythonic.
  - Avoids repeated string concatenation.
  - Uses slicing instead of incremental building.
  - Slightly more readable and elegant.
- Weaknesses:
  - Still compares all strings per character.
  - Requires scanning for shortest string first.
 