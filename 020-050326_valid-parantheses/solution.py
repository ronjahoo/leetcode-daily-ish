def validParanthesesFirst(s: str) -> bool:
    matching = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop() 

    return len(stack) == 0


def validParanthesesSecond(s: str) -> bool:
    stack = []
    pair = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in pair:
            stack.append(pair[char])
        else:
            if not stack or stack[-1] != char:
                return False
            stack.pop()

    return len(stack) == 0

if __name__ == "__main__":
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([])"
    s5 = "([)]"

    print(validParanthesesFirst(s1))
    print(validParanthesesFirst(s2))
    print(validParanthesesFirst(s3))
    print(validParanthesesFirst(s4))
    print(validParanthesesFirst(s5))

    print(validParanthesesSecond(s1))
    print(validParanthesesSecond(s2))
    print(validParanthesesSecond(s3))
    print(validParanthesesSecond(s4))
    print(validParanthesesSecond(s5))