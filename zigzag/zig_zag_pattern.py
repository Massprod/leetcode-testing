# The string "PAYPALISHIRING" is written in a zigzag pattern
# on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
from numpy import matrix


def convert(s: str, numRows: int) -> str:
    matr = [[""] for _ in range(numRows)]
    max_y = len(matr) - 1
    x = 0
    y = 0
    dx = 0
    dy = 1
    for _ in s:
        max_x = len(matr[0])
        matr[y][x] = _
        x += dx
        y += dy
        if y >= max_y and dx == 0:
            for _ in matr:
                _.append("")
            y = max_y
            x += 1
            dy = -1
            dx = 1
        elif y <= 0 and x == max_x:
            for _ in matr:
                _.append("")
            y = 0
            dy = 1
            dx = 0
        elif x == max_x:
            for _ in matr:
                _.append("")
    zig_zag = ""
    print(matrix(matr))
    for _ in matr:
        zig_zag += "".join(_)
    return zig_zag


test_string = "PAYPALISHIRING"

print(convert(test_string, 1))
print(convert("abcdefg", 100))


