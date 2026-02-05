
def palindromeNumberFirst(n: int) -> bool:
    s = str(n)
    sRev = s[::-1]
    if (s == sRev):
        return True
    else:
        return False

def palindromeNumberSecond(n: int) -> bool:
    if n < 0:
        return False
    
    s = str(n)
    i = 0
    j = len(s) - 1

    while i < j:
        if (s[j] == s[i]):
            i += 1
            j -= 1
        else:
            return False
    
    return True

        

if __name__ == "__main__":
    n1 = 121
    n2 = -121
    n3 = 10

    print(palindromeNumberFirst(n1))
    print(palindromeNumberFirst(n2))
    print(palindromeNumberFirst(n3))

    print(palindromeNumberSecond(n1))
    print(palindromeNumberSecond(n2))
    print(palindromeNumberSecond(n3))
