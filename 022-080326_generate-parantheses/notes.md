# Generate Parantheses (08-03-2026)  
LeetCode: [Generate Parantheses](https://leetcode.com/problems/generate-parentheses/)
---
## First idea: Basic Recursive Backtracking
- Complexity: 
      - O(4ⁿ / √n) time
      - O(n) space per recursive call stack frame
- Algorithm: 
      - Recursive backtracking. 
            - Build the string character by character, passing open/close counters.
            - Add `(` if `open < n`, add `)` if `close < open`. 
            - When `len(string) == 2n`, append to results.
- Strengths: 
      - Very readable and intuitive, the constraints map directly to the two `if` conditions. 
      - Easy to reason about correctness at a glance.
- Weaknesses: 
      - Creates a new string object on every recursive call (strings are immutable in Python), so there's hidden allocation overhead. 
      - Also uses the call stack, which adds function call overhead and has a stack depth of `2n`.

---
## Second (and better) idea: Iterative BFS with Deque + Tuple State
- Complexity:
      - O(4ⁿ / √n) time
      - O(4ⁿ / √n) space
- Algorithm: 
      - Iterative BFS using a deque. 
      - Each queue entry is a tuple of `(current_string, open_count, close_count)`. 
      - Pop from the front, apply the same two validity rules (`open < n`, `close < open`), and push new states. 
      - When `len(string) == 2n`, save to results.
- Strengths: 
      - Eliminates recursion and the call stack entirely, no risk of stack overflow for large inputs. 
      - The iterative structure is easier to debug (you can inspect the queue at any point)
      - Processes combinations in a natural breadth-first order.
- Weaknesses: 
      - Holds all in-flight partial strings in memory at once, making peak memory usage significantly higher than the recursive approach. 
      - Still creates a new string on every state expansion
      - The deque of tuples also adds overhead compared to the buffer backtracking approach.