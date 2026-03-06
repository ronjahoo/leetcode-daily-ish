# Merge Two Sorted Lists (06-03-2026)  
LeetCode: [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
---
## First idea: Two-Pointer with Array Buffer
- Complexity: 
      - Time O(n+m)
      - Space O(n+m) — extra array of size n+m allocated for results
- Algorithm: 
      - Walk both lists and collect values into two arrays. 
      - Use two index pointers (i, j) and a write pointer (k) into a pre-allocated result array. 
      - At each step, copy the smaller value into result[k] and advance that pointer. 
      - Drain any remaining elements. 
      - Rebuild a linked list from the result array.
- Strengths: 
      - Easy to reason about — familiar two-pointer array merge pattern. 
      - Straightforward to debug since all values are visible in a flat array.
- Weaknesses: 
      - Allocates O(n+m) extra memory unnecessarily. 
      - Creates brand new ListNode objects instead of reusing the existing ones. 
      - More code and more steps than needed.

---
## Second (and better) idea: Optimal In-Place Splice (Merge Sort style)
- Complexity: 
      - Time O(n+m)
      - Space O(1) — only a dummy head node is allocated
- Algorithm: 
      - Create a dummy sentinel node as the result head. Use a cursor pointer starting there. 
      - At each step, compare the values at p1 and p2, wire cursor.next directly to the smaller node (no copying), advance that list's pointer and the cursor. 
      - After the loop, attach the non-exhausted tail in a single assignment since it is already sorted.
- Strengths: 
      - O(1) space — splices existing nodes in-place with no allocation. 
      - Minimal code. 
      - The dummy node elegantly eliminates the null-head edge case, making the loop uniform for all inputs including empty lists.
- Weaknesses: 
      - Mutates the input lists (nodes get their .next pointers rewired), so the originals cannot be reused after the call. 
      - Slightly less intuitive than the array version for beginners since you are manipulating pointers rather than values.