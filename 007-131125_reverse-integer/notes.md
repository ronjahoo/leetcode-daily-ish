# Reverse Integer (13-11-2025)  
LeetCode: [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

---

## First idea: Column-based (“full → tapering columns”)

- Complexity:
  - Time: O(n), where n is the number of digits (at most 10)
  - Space: O(n), due to string slicing, reversing, trimming, and possible string comparison

- Algorithm:  
  1. Extract the sign (positive/negative).
  2. Convert the absolute value of the integer into a string.
  3. Reverse that string and strip leading zeros on the reversed form.
  4. Handle the edge case where stripping zeros yields an empty string (e.g., input 0).
  5. Check the length of the reversed string:
    - If it is more than 10 digits → definitely outside 32-bit signed range.
    - If exactly 10 digits → compare lexicographically against the 32-bit boundaries
("2147483647" for positive, "2147483648" for negative).
  6. If within boundaries, convert back to int and reapply the original sign.
  7. Return the final value.

- Strengths: 
  - Very simple, intuitive, and easy to reason about.
  - Operates at the string level, so it avoids any accidental intermediate integer overflow.
  - Lexicographic comparison is elegant when length is fixed.
  - Great for validating the logic or building quick prototypes.

- Weaknesses: 
  - Requires multiple string allocations and manipulations (slower and less memory-efficient).
  - Edge cases such as 0, negative numbers, or leading zeros require dedicated handling.
  - The boundary checks must be manually implemented using string logic — somewhat brittle.
  - Not the “intended” CPU-like solution: does not model real arithmetic overflow prevention.

---

## Second (and better) idea: Row-based with direction flag

- Complexity:
  - Time: O(n), with n ≤ 10 (number of digits)
  - Space: O(1), constant space — uses only a few integer variables

- Algorithm:
  1. Store the 32-bit signed integer limits
  2. Extract the sign and reduce x to its absolute value.
  3. Initialize rev = 0.
  4. While x still contains digits:
    - Extract the last digit using digit = x % 10.
    - Remove that last digit using x //= 10.
    - Before constructing the next number, check whether
      - rev * 10 + digit would overflow the 32-bit boundary:
        - If rev > INT_MAX // 10 → certain overflow.
        - If rev == INT_MAX // 10 and digit > 7 → overflow by final digit.
      - If safe, perform rev = rev * 10 + digit.
  5. Reapply the sign.
  6. Return the resulting reversed value or 0 if overflow was detected.

- Strengths:
  - Uses true arithmetic and mirrors how a 32-bit CPU would guard against overflow.
  - Safe and efficient: O(1) space, simple integer operations.
  - Overflow is prevented before it happens — exactly what the problem demands
  - Handles all edge cases naturally through arithmetic, not string manipulation.

- Weaknesses:
  - Requires the programmer to manually reason about overflow thresholds — subtle logic.
  - Less intuitive to beginners compared to the straightforward “reverse a string” idea.
  - The overflow guard conditions need to be carefully crafted and remembered.
