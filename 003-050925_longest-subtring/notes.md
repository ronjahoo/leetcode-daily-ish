# Longest Substring Without Repeating Characters (05-09-2025)  
LeetCode: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## First idea: hash approach

- Complexity: 
  - Time complexity is worse than O(n) in practice, because the substring search restarts when a duplicate is found.  
  - Space complexity is O(min(n, Σ)), where Σ is the character set.

- Algorithm:  
  1. Iterate over the string character by character.  
  2. Keep a dictionary (`seen`) of characters currently in the substring.  
  3. If a duplicate character is encountered, update the maximum length found so far, reset the current length, and start a new substring from the duplicate.  
  4. Continue until the end of the string, then return the maximum length.  

- Strengths:
  - Simple to reason about.  
  - Directly implements the intuitive idea of “restart when a duplicate is found.”  

- Weaknesses:
  - Inefficient because it discards useful information when restarting.  
  - Fails to achieve the optimal O(n) time complexity.  
  - May mis-handle overlapping substrings.

---

## Second (and better) idea: dictionary with last seen indices

- Complexity: 
  - Time complexity: O(n), where n is the length of the string.  
  - Space complexity: O(min(n, Σ)) for storing the last seen index of each character.

- Algorithm: 
  1. Maintain two pointers (`left` and `i`) to represent the current window of unique characters.  
  2. Use a dictionary (`last_seen`) to store the last index of each character.  
  3. For each character at index `i`:  
     - If it has been seen inside the current window, move `left` to `last_seen[ch] + 1`.  
     - Update `last_seen[ch] = i`.  
     - Update the maximum length as `i - left + 1`.  
  4. Return the maximum length found.

- Strengths:
  - Efficient sliding-window approach.  
  - Never revisits characters unnecessarily.  
  - Guarantees linear time.  

- Weaknesses:
  - Slightly more complex to implement and reason about.  
  - Requires careful handling of indices to avoid off-by-one errors.  
