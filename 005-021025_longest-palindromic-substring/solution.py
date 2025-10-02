def palindromeFromHeads(s: str) -> str:
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    start, max_len = 0, 1
    
    for i in range(n):
        dp[i][i] = True
    
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start, max_len = i, 2
    
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_len:
                    start, max_len = i, length
    
    return s[start:start+max_len]

def palindromeFromCenter(s: str) -> str:
    start, end = 0, 0

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l+1, r-1

    for i in range(len(s)):
        l1, r1 = expand(i, i)      # odd length
        l2, r2 = expand(i, i+1)    # even length
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end+1]

if __name__ == "__main__":
    str = "cbbd"

    result_heads = palindromeFromHeads(str)
    result_center = palindromeFromCenter(str)

    print("Pointers from heads result:", result_heads)
    print("Pointers from center result:", result_center)
