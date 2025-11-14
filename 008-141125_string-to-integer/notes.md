# String to Integer (14-11-2025)  
LeetCode: [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

---

## First idea: Column-based

- Complexity:
  - Time: O(n), where n is the length of the string (single left-to-right pass)
  - Space: O(1), only a few scalar variables

- Algorithm:  
  - Initialise `i = 0`, `sign = 1`, `num = 0`.
  - Skip all leading spaces with a `while i < n and s[i] == ' '` loop.
  - If we consumed the whole string → return 0.
  - Read an optional sign:
    - If next char is `'-'`, set `sign = -1`, advance `i`.
    - Else if next char is `'+'`, just advance `i`.
  - Read digits and build the absolute value:
    - While `i < n` and `s[i].isdigit()`:
      - `digit = ord(s[i]) - ord('0')`
      - `num = num * 10 + digit`
      - `i += 1`
  - Compute `result = sign * num`.
  - Clamp the final result to 32-bit range:
    - If `result < INT_MIN` → return `INT_MIN`
    - If `result > INT_MAX` → return `INT_MAX`
    - Else return `result`.

- Strengths: 
  - Very straightforward and easy to read.
  - Uses one clean pass over the string.
  - Overflow handling is conceptually simple: “compute then clamp”.
  - Perfectly fine in Python where integers can grow arbitrarily large.

- Weaknesses: 
  - In a low-level / fixed-width integer language, building `num` first and clamping later can overflow before we even get to the clamp step.
  - Logic is correct only if the language guarantees safe big integers (like Python); not directly portable to C/C++/Java without extra care.
  - Overflow behaviour is “all at the end”, making it slightly harder to reason about boundary cases step by step.

---

## Second (and better) idea: Row-based with early overflow checks

- Complexity:
  - Time: O(n), still a single pass over the string
  - Space: O(1), same scalar variables as before

- Algorithm:
  - Same initial steps as in the first version:
    - Initialise `i`, `n`, `sign = 1`.
    - Skip leading spaces.
    - Early return 0 if we hit the end.
    - Read optional `'-'` or `'+'` and update `sign` + `i`.
  - Before the digit loop, define:
    - `INT_MIN = -2**31`
    - `INT_MAX = 2**31 - 1`
  - Read digits and build `num` **with pre-checks**:
    - While `i < n` and `s[i].isdigit()`:
      - `digit = ord(s[i]) - ord('0')`
      - If `sign == 1`:
        - If `num > INT_MAX // 10` **or**
          `num == INT_MAX // 10 and digit > INT_MAX % 10`  
          → we know the next step would overflow → return `INT_MAX`.
      - Else (`sign == -1`):
        - Use the mirrored check against `INT_MIN` (via `-INT_MIN` as positive bound);  
          if next step would go below `INT_MIN` → return `INT_MIN`.
      - If safe, update: `num = num * 10 + digit` and `i += 1`.
  - After the loop, just return `sign * num` (no extra clamp needed, it was already handled).

- Strengths:
  - Overflow is handled **during** number construction, before it actually happens.
  - Portable idea to languages with fixed-width ints (C/C++/Java), because we never let the intermediate `num` overflow.
  - Makes the boundary logic explicit and testable: we can see exactly when and why we return `INT_MAX` / `INT_MIN`.
  - Still O(n)/O(1), mutta semanttisesti “turvallisempi”.

- Weaknesses:
  - Slightly more complex to read and write because of the pre-check conditions.
  - Easy to make off-by-one mistakes in the comparison logic (`// 10`, `% 10`) if not careful.
  - Conceptually heavier: vaatii enemmän ymmärrystä siitä, miten 32-bittiset rajat toimivat numeron rakentamisen aikana.
