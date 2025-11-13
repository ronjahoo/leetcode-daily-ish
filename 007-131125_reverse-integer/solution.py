
def reverse_first_version(x: int):
    sign = -1 if x < 0 else 1
    s = str(abs(x))[::-1].lstrip('0')
    if s == "":
        s = "0"
    
    if len(s) > 10:
        return 0
    if len(s) == 10:
        if sign == 1 and s > "2147483647":
            return 0
        if sign == -1 and s > "2147483648":
            return 0
    
    res = sign * int(s)
    return res

def reverse_second_version(x: int):
    lower_bound = -2**31
    upper_bound = 2**31-1

    sign = -1 if x < 0 else 1
    x = abs(x)

    rev = 0
    while x != 0:
        digit = x % 10
        x //= 10
        if rev > upper_bound // 10 or (rev == upper_bound // 10 and digit > 7):
            return 0
        rev = rev * 10 + digit
    rev *= sign
    return rev if lower_bound <= rev <= upper_bound else 0

if __name__ == "__main__":
    x = 123

    print("Result of the first version:", reverse_first_version(x))
    print("Result of the second version:", reverse_second_version(x))
