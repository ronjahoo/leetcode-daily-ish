def romanToIntFirst(s: str) -> int:
    thousands_s, hundreds_s, tens_s, ones_s = "", "", "", ""

    i = 0
    n = len(s)

    while i < n and s[i] == "M":
        thousands_s += s[i]
        i += 1

    while i < n and s[i] in "CDM":
        hundreds_s += s[i]
        i += 1

    while i < n and s[i] in "XLC":
        tens_s += s[i]
        i += 1

    while i < n and s[i] in "IVX":
        ones_s += s[i]
        i += 1

    ones = {
    "": 0, "I": 1, "II": 2, "III": 3, "IV": 4,
    "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9
    }

    tens = {
        "": 0, "X": 10, "XX": 20, "XXX": 30, "XL": 40,
        "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90
    }

    hundreds = {
        "": 0, "C": 100, "CC": 200, "CCC": 300, "CD": 400,
        "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900
    }

    thousands = {
        "": 0, "M": 1000, "MM": 2000, "MMM": 3000
    }

    return (
        thousands[thousands_s] +
        hundreds[hundreds_s] +
        tens[tens_s] +
        ones[ones_s]
    )

def romanToIntSecond(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0

    for i in range(len(s)):
        current = values[s[i]]
        nextOne = values[s[i+1]] if i + 1 < len(s) else 0
        total += -current if current < nextOne else current

    return total


if __name__ == "__main__":
    s1 = "III"
    s2 = "LVIII"
    s3 = "MCMXCIV"

    print(romanToIntFirst(s1))
    print(romanToIntFirst(s2))
    print(romanToIntFirst(s3))

    print(romanToIntSecond(s1))
    print(romanToIntSecond(s2))
    print(romanToIntSecond(s3))


