# Remove Nth Node From End of List (23-02-2026)  
LeetCode: [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## First idea: Two-pass (length-based) solution

- Complexity: 
      - Time: O(n)
      - Space: O(1)
- Algorithm:
      - Traverse the list once to compute its length.
      - Convert “n-th from end” into index from start: index = length - n
      - If index == 0, remove head.
      - Otherwise traverse again to the node before index.
      - Rewire pointers to skip the target node.
- Strengths:
      - Very readable and intuitive.
      - Easy to reason about correctness.
      - Clear separation of responsibilities (measure → compute → remove).
      - Good stepping stone toward pointer mastery.
- Weaknesses:
      - Requires two passes over the list.
      - Slightly less optimal than the one-pass solution.
      - Not as elegant in interview settings.

---

## Second (and better) idea: Two-pointer (fast/slow) solution

- Complexity:
      - Time: O(n)
      - Space: O(1)
- Algorithm:
      - Create a dummy node pointing to head.
      - Initialize two pointers (fast, slow) at dummy.
      - Move fast forward n steps.
      - Move both pointers forward together until fast reaches the last node.
      - slow now points to the node before the one to remove.
      - Rewire pointers.
      - Return dummy.next.
- Strengths:
      - Single pass.
      - Elegant and efficient.
      - Handles head removal cleanly with dummy node.
      - Interview-preferred approach.
- Weaknesses:
      - Slightly less intuitive at first glance.
      - Pointer offset logic requires careful reasoning.
 