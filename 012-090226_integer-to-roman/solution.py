def intToRomanFirst(num: int) -> str:
    places = ["ones", "tens", "hundreds", "thousands"]
    result = {}

    i = 0
    while num > 0 and i < len(places):
        result[places[i]] = num % 10
        num //= 10
        i += 1

    s = ""
    order = ["thousands", "hundreds", "tens", "ones"]

    for place in order:
        if place not in result:
            continue

        digit = result[place]

        if place == "thousands":
            s += "M" * digit

        elif place == "hundreds":
            if digit == 9:
                s += "CM"
            elif digit == 4:
                s += "CD"
            elif digit >= 5:
                s += "D" + ("C" * (digit - 5))
            else:
                s += "C" * digit

        elif place == "tens":
            if digit == 9:
                s += "XC"
            elif digit == 4:
                s += "XL"
            elif digit >= 5:
                s += "L" + ("X" * (digit - 5))
            else:
                s += "X" * digit

        elif place == "ones":
            if digit == 9:
                s += "IX"
            elif digit == 4:
                s += "IV"
            elif digit >= 5:
                s += "V" + ("I" * (digit - 5))
            else:
                s += "I" * digit

    return s

def intToRomanSecond(num: int) -> str:
    ones = {
        0: "", 1: "I", 2: "II", 3: "III", 4: "IV",
        5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"
    }
    tens = {
        0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL",
        5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"
    }
    hundreds = {
        0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD",
        5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"
    }
    thousands = {
        0: "", 1: "M", 2: "MM", 3: "MMM"
    }

    return (
        thousands[num // 1000] +
        hundreds[(num // 100) % 10] +
        tens[(num // 10) % 10] +
        ones[num % 10]
    )


if __name__ == "__main__":
    num1 = 3749
    num2 = 58
    num3 = 1994

    print(intToRomanFirst(num1))
    print(intToRomanFirst(num2))
    print(intToRomanFirst(num3))

    print(intToRomanSecond(num1))
    print(intToRomanSecond(num2))
    print(intToRomanSecond(num3))
