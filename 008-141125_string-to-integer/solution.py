
def myAtoiFirst(s: str) -> int:
    i = 0
    n = len(s)
    sign = 1

    while i < n and s[i] == ' ':
        i += 1

    if i == n:
        return 0
        
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        i += 1

    num = 0
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')
        num = num * 10 + digit
        i += 1

    result = sign * num
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if (result < INT_MIN):
        return INT_MIN
    if (result > INT_MAX):
        return INT_MAX
    return result

def myAtoiSecond(s: str) -> int:
    i = 0
    n = len(s)
    sign = 1

    while i < n and s[i] == ' ':
        i += 1

    if i == n:
        return 0
        
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        i += 1

    num = 0
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')
        if sign == 1:
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX
        else:
            if num > (-INT_MIN) // 10 or (num == (-INT_MIN) // 10 and digit > (-INT_MIN) % 10):
                return INT_MIN
        num = num * 10 + digit
        i += 1

    return sign * num

if __name__ == "__main__":
    s = '22'
    print(myAtoiFirst(s))
    print(myAtoiSecond(s))
