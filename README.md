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

---

## ⚙️ Running locally

```bash
python solution.py
pytest tests.py    # if tests are provided
