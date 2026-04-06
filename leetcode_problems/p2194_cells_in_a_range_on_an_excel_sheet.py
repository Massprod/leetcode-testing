# A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
#  - <col> denotes the column number c of the cell.
#    It is represented by alphabetical letters.
#    - For example, the 1st column is denoted by 'A',
#      the 2nd by 'B', the 3rd by 'C', and so on.
#  - <row> is the row number r of the cell. The rth row is represented by the integer r.
# You are given a string s in the format "<col1><row1>:<col2><row2>",
#  where <col1> represents the column c1, <row1> represents the row r1,
#  <col2> represents the column c2, and <row2> represents the row r2,
#  such that r1 <= r2 and c1 <= c2.
# Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2.
# The cells should be represented as strings in the format mentioned above
#  and be sorted in non-decreasing order first by columns and then by rows.
# --- --- --- ---
# s.length == 5
# 'A' <= s[0] <= s[3] <= 'Z'
# '1' <= s[1] <= s[4] <= '9'
# s consists of uppercase English letters, digits and ':'.
from string import ascii_uppercase


def cells_in_range(s: str) -> list[str]:
    # working_solution: (31.91%, 79.93%) -> (2ms, 19.28mb)  Time: O(s) Space: O(s)
    # Basically: columns with the rows order.
    first_row: int = int(s[1])
    last_row: int = int(s[4])
    first_col: str = s[0]
    last_col: str = s[3]
    # { char: index }
    char_indexes: dict[str, int] = {
        char: index for index, char in enumerate(ascii_uppercase)
    }
    first_col_index: int = char_indexes[first_col]
    last_col_index: int = char_indexes[last_col]
    out: list[str] = []
    for column in ascii_uppercase[first_col_index: last_col_index + 1]:
        for row in range(first_row, last_row + 1):
            record: str = f'{column}{row}'
            out.append(record)

    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = "K1:L2"
test_out: list[str] = ["K1", "K2", "L1", "L2"]
assert test_out == cells_in_range(test)

test = "A1:F1"
test_out = ["A1", "B1", "C1", "D1", "E1", "F1"]
assert test_out == cells_in_range(test)
