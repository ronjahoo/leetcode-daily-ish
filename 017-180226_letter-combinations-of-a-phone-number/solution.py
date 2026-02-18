from typing import List

def letterCombinationsFirst(digits: str) -> List[str]:
    if not digits:
        return []
    digit_map = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    char_lists = []
    for ch in digits:
        num = int(ch)
        if num in digit_map:  
            char_lists.append(digit_map[num])

    result = []

    def backtrack(index, path):
        if index == len(char_lists):
            result.append("".join(path))
            return

        for letter in char_lists[index]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop() 

    backtrack(0, [])
    return result

def letterCombinationsSecond(digits: str) -> List[str]:
        if not digits:
            return []

        digit_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = [""]

        for digit in digits:
            temp = []
            for prefix in result:
                for letter in digit_map[digit]:
                    temp.append(prefix + letter)
            result = temp

        return result

if __name__ == "__main__":
    digits1 = "23"
    digits2 = "2"

    print(letterCombinationsFirst(digits1))
    print(letterCombinationsFirst(digits2))

    print(letterCombinationsSecond(digits1))
    print(letterCombinationsSecond(digits2))


