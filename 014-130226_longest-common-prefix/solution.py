from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    longestPrefix = ""

    if not strs:
        return longestPrefix

    if any(word == "" for word in strs):
        return longestPrefix
    
    shortestLen = min(len(word) for word in strs)

    for i in range(shortestLen):
        if all(word[i] == strs[0][i] for word in strs):
            longestPrefix += strs[0][i]
        else:
            return longestPrefix
        
    return longestPrefix

def longestCommonPrefixSecond(strs: List[str]) -> str:
    if not strs:
        return ""
    
    if any(word == "" for word in strs):
        return ""

    shortest = min(strs, key=len)

    for i, char in enumerate(shortest):
        if any(word[i] != char for word in strs):
            return shortest[:i]

    return shortest


if __name__ == "__main__":
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]

    print(longestCommonPrefix(strs1))
    print(longestCommonPrefix(strs2))

    print(longestCommonPrefixSecond(strs1))
    print(longestCommonPrefixSecond(strs2))


