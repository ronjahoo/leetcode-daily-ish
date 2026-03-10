# Merge k Sorted Lists (10-03-2026)  
LeetCode: [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
---
## First idea: Collect the values, sort, and make a linked list
- Complexity: 
      - Time O(N log N)
      - Space O(N) 
- Algorithm: 
      - Traverse every list and dump all values into a single array
      - Sort the list
      - Rebuild a linked list from scratch based on the sorted new list
- Strengths: 
      - Simple to implement and reason about
      - Sorting handles everything without thinking about inter-list ordering
- Weaknesses: 
      - Throws away the fact that each input list is already sorted — that property is completely ignored, making the sort redundant work
      - Also allocates O(N) extra space for the values array plus the new nodes

---

## Second (and better) idea: Always pick the smallest current node across all lists using min-heap
- Complexity: 
      - Time O(N log k)
      - Space O(k)
- Algorithm: 
      - Push the head node of each list into a min-heap
      - Repeatedly pop the smallest node, append it to the result, and push that node's next onto the heap, so the heap always holds exactly one candidate per list
- Strengths: 
      - Exploits the fact that each list is pre-sorted; only k elements live in the heap at any time, so both time and space are much tighter
      - The log k factor vs log N is a meaningful win when k << N
- Weaknesses: 
      - Slightly more involved to implement; requires either a comparable wrapper or a tie-breaking index in the heap tuple (since ListNode objects aren't directly comparable in Python)