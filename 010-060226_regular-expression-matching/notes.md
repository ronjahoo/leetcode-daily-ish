# Regular Expression Matching (06-02-2026)  
LeetCode: [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

---

## First idea: Basic Loop-Matcher

- Complexity:
  - Worst-case time: exponential ≈O(2^(m+n)) in pathological cases with many '∗'
    - Closer to O(m·n) in practice, but not guaranteed
  - Space: O(m + n) for recursion/stack or O(states) for iterative backtracking with memo-set
- Algorithm:  
  - Traverse string and pattern using indices.
  - When encountering x*, branch into:
    - Skip the x* (zero occurrences)
    - Consume one matching character and stay on the same pattern position
  - Use iterative backtracking with a stack of (si, pi) states.
    - Normalize repeated a*a*a* → a*
    - Remember failed states in a seen set to avoid recomputation.
- Strengths: 
  - Intuitive, follows the natural reading of regex.
  - Uses only basic loops and indices (no DP table).
  - Easy stepping stone toward understanding recursion/DP.
- Weaknesses: 
  - Exponential worst case → can cause Time Limit Exceeded.
  - Correctness relies on subtle state management and pruning.
  - Harder to reason about formally.
  - Not the canonical interview solution.

---

## Second (and better) idea: Dynamic Programming

- Complexity:
  - Time: O(m · n)
  - Space: O(m · n)
- Algorithm:
  - Define subproblem: dp[i][j] = does s[i:] match p[j:]
  - Base case: empty string matches empty pattern → dp[m][n] = True.
  - Fill table backwards because each state depends on future states.
  - Transition rules:
    - If next pattern char is * : skip x* → dp[i][j+2] or consume one char if matching → first_match and dp[i+1][j]
    - Otherwise: first_match and dp[i+1][j+1].
  - Final answer: dp[0][0].
- Strengths:
  - Provably polynomial time → never TLE.
  - Clean mathematical structure; easy to verify correctness.
  - Standard textbook / interview solution.
- Weaknesses:
  - Uses O(m·n) memory.
  - Less intuitive at first glance than backtracking.
  - Requires understanding subproblem decomposition.
 