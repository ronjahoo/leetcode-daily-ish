# Longest Palindromic Substring (02-10-2025)  
LeetCode: [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

---

## First idea: Dynamic Programming

- Complexity:
  - Time: O(n²)  
  - Space: O(n²)  

- Algorithm:  
  - Build a table `dp[i][j]` indicating whether `s[i:j+1]` is a palindrome
  - Base cases: single characters (always palindromes) and two-character substrings  
  - For longer substrings: it's a palindrome if `s[i] == s[j]` and the inner substring `dp[i+1][j-1]` is also true 
  - Update the longest palindrome whenever a longer one is found

- Strengths: 
  - Straightforward and systematic: explores all possibilities
  - Easy to reason about correctness

- Weaknesses: 
  - High memory usage (O(n²) table) 
  - Less practical: slower and more memory-intensive for large strings 

---

## Second (and better) idea: Expand Around Center

- Complexity:
  - Time: O(n²) (worst case, since each center can expand up to the length of the string)  
  - Space: O(1)  

- Algorithm:
  - Every palindrome can be defined around a "center"
  - Iterate through each index as a potential center
  - Expand outward for both odd- and even-length palindromes
  - Track the longest palindrome found

- Strengths:
  - Much lighter than DP (memory and implementation) 
  - Faster in practice on LeetCode  
  - Very intuitive: directly matches the definition of a palindrome

- Weaknesses:
  - Only finds the longest palindrome, not all palindromic substrings
  - Theoretical time complexity is still O(n²), even though it performs better in practice
