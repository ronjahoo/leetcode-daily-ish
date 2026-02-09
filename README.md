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
| 005 | Longest Palindromic Substring | [LeetCode #5](https://leetcode.com/problems/longest-palindromic-substring/) | [solution](005-021025_longest-palindromic-substring\solution.py) | O(n^2) | ✅ |
| 006 | Zigzag Conversion | [LeetCode #6](https://leetcode.com/problems/zigzag-conversion/) | [solution](006-031025_zigzag-conversion\solution.py) | O(n) | ✅ |
| 007 | Reverse Integer | [LeetCode #7](https://leetcode.com/problems/reverse-integer/) | [solution](007-131125_reverse-integer\solution.py) | O(n) | ✅ |
| 008 | String to Integer | [LeetCode #8](https://leetcode.com/problems/string-to-integer-atoi/) | [solution](008-141125_string-to-integer\solution.py) | O(n) | ✅ |
| 009 | Palindrome Number | [LeetCode #9](https://leetcode.com/problems/palindrome-number/) | [solution](009-050226_palindrome-number\solution.py) | O(n) | ✅ |
| 010 | Regular Expression Matching | [LeetCode #10](https://leetcode.com/problems/regular-expression-matching/) | [solution](010-060226_regular-expression-matching) | O(n*m) | ✅ |
| 011 | Container With Most Water | [LeetCode #11](https://leetcode.com/problems/container-with-most-water/) | [solution](011-070226_container-with-most-water) | O(n) | ✅ |
| 012 | Integer to Roman | [LeetCode #12](https://leetcode.com/problems/integer-to-roman/) | [solution](012-090226_integer-to-roman) | O(1) | ✅ |
---

## ⚙️ Running locally

```bash
python solution.py
pytest tests.py    # if tests are provided
