def zigzagFirst(s: str, numRows: int):
    if numRows == 1 or numRows >= len(s):
        return s

    cols = []     
    col = 0
    row = 0
    down = True  

    for ch in s:
        if col == len(cols):
            cols.append({})
        cols[col][row] = ch

        if down:
            if row == numRows - 1:
                down = False
                row -= 1
                col += 1
            else:
                row += 1     
        else:
            if row == 0:
                down = True
                row += 1
                col += 1
            else:
                row -= 1
                col += 1            

    out = []
    for r in range(numRows):
        for c in range(len(cols)):
            if r in cols[c]:
                out.append(cols[c][r])
    return "".join(out)

def zigzagSecond(s: str, numRows: int):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        r = 0           
        direction = 1   

        for ch in s:
            rows[r] += ch
            if r == 0:
                direction = 1
            elif r == numRows - 1:
                direction = -1
            r += direction

        return "".join(rows)

if __name__ == "__main__":
    str = "PAYPALISHIRING"
    nr = 3

    result_first = zigzagFirst(str, nr)
    result_second = zigzagSecond(str, nr)

    print("Result of the first verion:", result_first)
    print("Result of the seconf version:", result_second)
