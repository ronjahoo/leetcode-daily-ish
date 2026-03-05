# Valid Parentheses (05-03-2026)  
LeetCode: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
---
## First idea: Two-Pointer / Stack Simulation
- Complexity: 
      - O(n) time
      - O(n) space
- Algorithm: 
      - Iterate through the string. 
      - Push opening brackets onto a stack. 
      - When a closing bracket is encountered, check if the top of the stack holds its matching opener using a lookup dict (`{')': '(', ...}`). 
      - If it matches, pop the stack (collapsing the pair). 
      - If it doesn't match or the stack is empty, return `False`. 
      - After the loop, return `True` only if the stack is empty.
- Strengths: 
      - Intuitive, mirrors the mental model of "collapsing" matched pairs inward
      - Easy to reason about correctness
- Weaknesses: 
      - The lookup dict is queried on every closing bracket (at pop time), which is a minor extra step compared to the alternative

---
## Second (and better) idea: Optimal Stack Solution
- Complexity: 
      - O(n) time
      - O(n) space
- Algorithm: 
      - Iterate through the string. 
      - When an opening bracket is seen, push its *expected closing bracket* onto the stack using a lookup dict (`{'(': ')', ...}`). 
      - When a closing bracket is seen, check if it equals the top of the stack. 
      - If yes, pop; if no (or stack empty), return `False`. 
      - Return `True` if the stack is empty at the end.
- Strengths: 
      - Cleaner pop logic, no dict lookup needed at closing time, just a direct equality check
      - Slightly more elegant and idiomatic
- Weaknesses: 
      - The direction of the lookup (opener → closer instead of closer → opener) is slightly less intuitive at first glance, but quickly becomes natural