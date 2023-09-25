# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#   P   A   H   N
#   A P L S I I G
#   Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#   string convert(string s, int numRows);
# ------------------
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


def convert(s: str, numRows: int) -> str:
    # working_sol (75.6%, 51.16%) -> (56ms, 16.4mb)  time: O(n) | space: O(n)
    # 1 row => zigzag will be a 1 line.
    # len(s) < rows => one column, which is also 1 line.
    if numRows == 1 or numRows >= len(s):
        return s
    # Only one column first, we don't know how many we need.
    # When we need more columns we add them, cuz we only know about rows.
    matrix: list[list[str]] = [[''] for _ in range(numRows)]
    max_row: int = len(matrix) - 1
    row: int = 0
    row_shift: int = 1
    for sym in s:
        matrix[row].append(sym)
        # First row. We go down.
        if row == 0:
            row_shift = 1
        # Last row. We go up.
        elif row == max_row:
            row_shift = -1
        row += row_shift
    # Recreate row by row.
    zig_zag: str = ''
    for row_ in matrix:
        zig_zag += ''.join(row_)
    return zig_zag


# Time complexity: O(n) -> traversing whole input string to record all symbols in zig_zag order => O(n) ->
# n - len of input string^^| -> extra traversing created matrix with same # of indexes => O(n).
# Auxiliary space: O(n) -> matrix with all symbols of input string => O(n).


test: str = "PAYPALISHIRING"
test_rows: int = 3
test_out: str = "PAHNAPLSIIGYIR"
assert test_out == convert(test, test_rows)

test = "PAYPALISHIRING"
test_rows = 4
test_out = "PINALSIGYAHRPI"
assert test_out == convert(test, test_rows)

test = "A"
test_rows = 1
test_out = "A"
assert test_out == convert(test, test_rows)

test = "AB"
test_rows = 1
test_out = "AB"
assert test_out == convert(test, test_rows)

test = "ABCD"
test_rows = 1
test_out = "ABCD"
assert test_out == convert(test, test_rows)
