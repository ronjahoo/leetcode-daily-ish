# Roman to Integer (10-02-2026)  
LeetCode: [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

---

## First idea: Split the string

- Complexity:
  - Time: O(n) (each character is consumed once across the four while-loops)
  - Space: O(1) (fixed-size strings + dictionaries)
- Algorithm:  
  - Scan the string left-to-right and split it into four place-value chunks: thousands (M*), hundreds (C/D/M), tens (X/L/C), ones (I/V/X).
  - Convert each chunk via a lookup table and sum the results.
- Strengths: 
  - Very readable if you think in decimal place values (thousands/hundreds/tens/ones).
  - Easy to debug because you can print the four chunks and see what went where.
  - Naturally supports subtractive forms because they’re included as explicit keys (IV, CM, etc.).
- Weaknesses: 
  - Easy to introduce table typos (your "XXX": 33 bug is the classic example).
  - Assumes the Roman numeral is in standard canonical form; odd/non-canonical strings may split in surprising ways.
  - More verbose than necessary; maintains multiple lookup dictionaries.

---

## Second (and better) idea: Traverse the characters

- Complexity:
  - Time: O(n) (single pass)
  - Space: O(1) (one value map + a few integers)
- Algorithm:
  - Traverse characters left-to-right.
  - Let current = value[s[i]], and next = value[s[i+1]] (or 0 at end).
  - If current < next, subtract current; else add it.
  - Return the accumulated sum.
- Strengths:
  - Short, elegant, and hard to break with a typo.
  - Handles all standard subtractive cases implicitly (no need to list IV, IX, CM, etc.).
  - The most common interview/LeetCode approach.
- Weaknesses:
  - By itself, it doesn’t enforce Roman numeral validity rules (e.g., it would compute a number for non-canonical inputs like "IL" even though that’s not a valid Roman numeral for 49).
  - Slightly less “place-value intuitive” at first glance than the chunking approach.
 