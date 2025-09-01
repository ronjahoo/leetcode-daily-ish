# Add two numbers (01-09-2025)  
LeetCode: [Add two numbers](https://leetcode.com/problems/add-two-numbers/)

---

## First idea: Loop through both linked lists  

- Complexity: 
  - Time: O(max(m, n)), where m and n are the lengths of the two linked lists
  - Space: O(max(m, n)) for the new linked lis

- Algorithm:  
  1. Initialize a dummy head and a carry variable
  2. Traverse both lists at the same time
  3. At each step, take node values (or 0 if list ended)  
  4. Compute sum of node values and carry variable
  5. Split the sum to under ten as a result and rest in the carry
  6. Append digit to the new list 
  7. Move to next nodes
  8. If a carry remains after traversal, append it as a new node  

- Strengths:
  - Straightforward and easy to implement 
  - Very efficient in both time and space (optimal for the problem)  
  - Easy to debug and reason about

- Weaknesses: 
  - Slightly more verbose — requires explicit dummy node and while-loop handling  
  - Repetitive checks  

---

## Second (and better) idea: One recursive loop  

- Complexity: 
  - Time: O(max(m, n)) (same as the loop) 
  - Space: O(max(m, n)) because of recursion stack + new list

- Algorithm:  
  1. Base case: if `l1`, `l2`, and `carry` are all empty/zero, return `None`  
  2. Otherwise, compute sum of node values and carry varaiable 
  4. Split sum into carry and digit  
  5. Create a new node with the digit 
  6. Set next node to point to recursive call of next nodes with this function 
  7. Return the node

- Strengths: 
  - Elegant, compact, and mathematically neat
  - Avoids dummy-head boilerplate code 
  - Natural fit for recursive thinkers — closely mirrors the problem definition  

- Weaknesses:  
  - Consumes extra stack frames, so there's a risk of hitting recursion depth limit in Python for very long inputs  
  - Slightly harder to debug compared to the iterative approach  
  - Not as idiomatic in Python, where loops are usually preferred  
