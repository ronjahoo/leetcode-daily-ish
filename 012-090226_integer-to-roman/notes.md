# Integer to Roman (09-02-2026)  
LeetCode: [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

---

## First idea: If-structure

- Complexity:
  - Time: O(1) (digits are at most 4 places: thousands → ones)
  - Space: O(1) (small dict + output string)
- Algorithm:  
  - Split the integer into digits by place (ones/tens/hundreds/thousands) using % 10 and // 10.
  - Iterate places from biggest to smallest.
  - For each place, build the Roman substring with if/elif rules:
    - handle 9 and 4 as special cases (CM/CD, XC/XL, IX/IV)
    - handle >=5 by starting with midpoint symbol (D, L, V) and adding repeats
    - handle <4 by repeating base symbol (C, X, I)
  - Append each part into the result string.
- Strengths: 
  - Derives the Roman rules directly (good for understanding).
  - Easy to extend/debug by stepping through each place.
  - Doesn’t require precomputed tables.
- Weaknesses: 
  - Lots of branching → verbose and easy to make small logic/edge mistakes.
  - Slightly “over-engineered” with the extra result dict + loop when digits can be computed directly.
  - Harder to read at a glance than a lookup-table solution.

---

## Second (and better) idea: Hash table

- Complexity:
  - Time: O(1) (constant number of lookups and concatenations)
  - Space: O(1) (fixed-size hash tables)
- Algorithm:
  - Predefine 4 hash tables (dicts) mapping digit 0..9 to the correct Roman string for that place
  - Extract digits with integer arithmetic
  - Return concatenation of the 4 looked-up strings.
- Strengths:
  - Very compact and readable: “digit → Roman chunk” becomes pure lookup.
  - Minimizes branching → fewer bugs.
  - Fast and clean; a strong interview-style solution.
- Weaknesses:
  - Requires writing/maintaining the lookup tables (more “data setup”).
  - Slightly less “conceptually derived” (it encodes rules as data rather than expressing them).
  - Needs careful tables to avoid typos (but once correct, it’s rock solid).
 