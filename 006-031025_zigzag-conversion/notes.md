# Zigzag Conversion (03-10-2025)  
LeetCode: [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)

---

## First idea: Column-based (“full → tapering columns”)

- Complexity:
  - Time: O(n⋅k), where n = length of string, k = number of rows (because we explicitly build column structures and then transpose)
  - Space: O(n), stored in a 2D-like structure

- Algorithm:  
  - Construct columns with a repeating cycle of heights: numRows, numRows-1, …, 1, numRows, …
  - Place characters top-down in each column up to that height
  - Read the result row by row to form the output string

- Strengths: 
  - Intuitive and easy to visualize
  - Directly implements the initial “tapering columns” idea
  - Useful for learning and debugging since the matrix is explicit

- Weaknesses: 
  - Wastes time and space building an explicit 2D structure
  - More complicated logic than necessary

---

## Second (and better) idea: Row-based with direction flag

- Complexity:
  - Time: O(n), single pass over the string
  - Space: O(n), store characters row by row

- Algorithm:
  - Keep a list of strings (one for each row)
  - Iterate through the input string while moving a row pointer r downwards and upwards alternately
  - Append each character to the current row
  - Concatenate rows at the end

- Strengths:
  - Simple, clean, and efficient
  - Easy to test and reason about

- Weaknesses:
  - Does not build a visible 2D matrix (harder to visualize if debugging)
  - Slightly more abstract compared to the column-based “manual matrix” version
