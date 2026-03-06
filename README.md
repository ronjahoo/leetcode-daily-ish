# 🧩 LeetCode Daily – My Solutions

A repository for my **daily practice** using [LeetCode](https://leetcode.com/) and python.  
I aim to solve one problem per day, and keep a clean log.

⚠️ Disclaimer: Only my solutions and notes are included. The problem statements belong to LeetCode.

---

## 📂 Structure
- Each folder `xxx-ddmmyy_problem-name/` contains:
  - `solution.py` – my implementation
  - `notes.md` – reflections (complexity, edge cases, what I learned)
  - `tests.py` – optional unit tests

---

## 📜 Daily Log

| Day | Problem | Link | Solution | Notes | Status |
|----:|---------|------|----------|-------|--------|
| 001 | Two Sum | [LeetCode #1](https://leetcode.com/problems/two-sum/) | [solution](001-220825_two-sum/solution.py) | Hash map O(n) and Pointers O(n log n) | ✅ |
| 002 | Add Two Numbers | [LeetCode #2](https://leetcode.com/problems/add-two-numbers/) | [solution](002-010925_add-two-numbers/solution.py) |O(n,m) | ✅ |
| 003 | Longest Substring Without Repeating Characters | [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [solution](003-050925_longest-subtring/solution.py) |O(n) | ✅ |
| 004 | Median of Two Sorted Arrays | [LeetCode #4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [solution](004-100925_median-of-two-sorted-arrays\solution.py) | O(log min(m,n)) | ✅ |
| 005 | Longest Palindromic Substring | [LeetCode #5](https://leetcode.com/problems/longest-palindromic-substring/) | [solution](005-021025_longest-palindromic-substring\solution.py) | O(n²) | ✅ |
| 006 | Zigzag Conversion | [LeetCode #6](https://leetcode.com/problems/zigzag-conversion/) | [solution](006-031025_zigzag-conversion\solution.py) | O(n) | ✅ |
| 007 | Reverse Integer | [LeetCode #7](https://leetcode.com/problems/reverse-integer/) | [solution](007-131125_reverse-integer\solution.py) | O(n) | ✅ |
| 008 | String to Integer | [LeetCode #8](https://leetcode.com/problems/string-to-integer-atoi/) | [solution](008-141125_string-to-integer\solution.py) | O(n) | ✅ |
| 009 | Palindrome Number | [LeetCode #9](https://leetcode.com/problems/palindrome-number/) | [solution](009-050226_palindrome-number\solution.py) | O(n) | ✅ |
| 010 | Regular Expression Matching | [LeetCode #10](https://leetcode.com/problems/regular-expression-matching/) | [solution](010-060226_regular-expression-matching) | O(n*m) | ✅ |
| 011 | Container With Most Water | [LeetCode #11](https://leetcode.com/problems/container-with-most-water/) | [solution](011-070226_container-with-most-water) | O(n) | ✅ |
| 012 | Integer to Roman | [LeetCode #12](https://leetcode.com/problems/integer-to-roman/) | [solution](012-090226_integer-to-roman) | O(1) | ✅ |
| 013 | Roman to Integer | [LeetCode #13](https://leetcode.com/problems/roman-to-integer/) | [solution](013-100226_roman-to-integer) | O(n) | ✅ |
| 014 | Longest Common Prefix | [LeetCode #14](https://leetcode.com/problems/longest-common-prefix/) | [solution](014-130226_longest-common-prefix) | O(n*m) | ✅ |
| 015 | 3Sum | [LeetCode #15](https://leetcode.com/problems/3sum/) | [solution](015-160226_3sum) | O(n²) | ✅ |
| 016 | 3Sum Closest | [LeetCode #16](https://leetcode.com/problems/3sum-closest/) | [solution](016-170226_3sum-closest) | O(n²) | ✅ |
| 017 | Letters Combinations of a Phone Number | [LeetCode #17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [solution](017-180226_letter-combinations-of-a-phone-number) |  O(4ⁿ) | ✅ |
| 018 | 4Sum | [LeetCode #18](https://leetcode.com/problems/4sum/) | [solution](018-210226_4sum) |  O(n³) | ✅ |
| 019 | Remove Nth Node From End of List | [LeetCode #19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [solution](019-230226_remove-nth-node-from-end-of-list) |  O(n) | ✅ |
| 020 | Valid Parantheses| [LeetCode #20](https://leetcode.com/problems/valid-parentheses/) | [solution](020-050326_valid-parantheses) |  O(n) | ✅ |
| 021 | Merge Two Sorted Arrays| [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/) | [solution](021-060326_merge-two-sorted-lists) |  O(n+m) | ✅ |

---

## ⚙️ Running locally

```bash
python solution.py
pytest tests.py    # if tests are provided
