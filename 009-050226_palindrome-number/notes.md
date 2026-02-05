# Palindrome Number (05-02-2026)  
LeetCode: [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

## First idea: Reversing the Whole String

- Complexity:
  - Time: O(d), where d is the number of digits (creating the reverse and comparing).
  - Space: O(d) for the reversed string.
- Algorithm:  
  - Convert the integer n to a string s.
  - Create a reversed copy s[::-1].
  - Compare the original string and the reversed string.
    - If they are equal, return True, otherwise False.
- Strengths: 
  - Extremely simple and readable.
  - Minimal code, low chance of logical bugs.
  - Naturally handles odd, even, and single-digit numbers without extra logic.
  - Perfect baseline solution for correctness.
- Weaknesses: 
  - Uses extra memory for the reversed string.
  - Relies on string conversion, so it doesn’t demonstrate numeric manipulation skills.
  - Negative numbers return False only implicitly (because of the '-'), not via an explicit rule.
  - In interviews, this may be considered the “easy but not optimal” approach.

---

## Second idea: Two pointers Inward Comparison

- Complexity:
  - Time: O(d) (at most half the digits are compared).
  - Space: O(d) for the string representation.
- Algorithm:
  - If n is less than 0, return False
  - Convert n to string s.
  - Set two indices:
    - i at the beginning
    - j at the end
  - While i < j:
    - If s[i] != s[j] → return False.
    - Otherwise move both pointers inward.
  - If the loop finishes → return True.
- Strengths:
  - Still simple, but more algorithmic than full reversal.
  - Avoids creating a second full reversed string.
  - Works cleanly for odd and even lengths with no branching.
  . Early exit on mismatch, efficient in practice.
  - Shows clearer problem-solving intent in interviews.
- Weaknesses:
  - Still depends on string conversion instead of pure math.
  - Negative handling is implicit rather than explicit.
  - Not the most optimal theoretical solution compared to the numeric half-reversal method I checked out.
 
