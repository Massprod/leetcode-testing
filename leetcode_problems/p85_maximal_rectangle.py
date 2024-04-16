# Given a rows x cols binary matrix filled with 0's and 1's,
#  find the largest rectangle containing only 1's and return its area.
# ---------------------------
# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
from random import choice


def maximal_rectangle(matrix: list[list[str | int]]) -> int:
    # working_sol (48.48%, 14.93%) -> (226ms, 18.02mb)  time: O(n * m) | space: O(m)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = int(matrix[row][col])
        matrix[row].append(0)

    def calc_row(row_num: int) -> int:
        max_rect: int = 0
        stack: list[int] = [-1]
        for _col in range(len(matrix[row_num])):
            while matrix[row_num][_col] < matrix[row_num][stack[-1]]:
                index: int = stack.pop()
                height: int = matrix[row_num][index]
                length: int = _col - stack[-1] - 1  # -1 for not including current element == `_col`
                max_rect = max(max_rect, height * length)
            stack.append(_col)
        return max_rect

    out: int = 0
    out = max(out, calc_row(0))
    for row in range(1, len(matrix)):
        for col in range(len(matrix[row])):
            if 0 != matrix[row][col]:
                matrix[row][col] += matrix[row - 1][col]
        out = max(out, calc_row(row))
    return out


# Time complexity: O(n * m) -> worst_case, traversing once through all indexes in a row => O(m)
# m - lengths of a row ^^      -> calling stack_calc() and traversing this row twice with a stack => O(2m) ->
# n - lengths of a matrix ^^   -> repeating for every row in a matrix => O(n * m)
# ---------------------------
# Space complexity: O(m) -> creating stack of matrix_row(hist) size => O(m) -> and max_area constant => O(1)
# ---------------------------
# Apparently changing whole matrix values to the integers, was faster than doing this on a move.
# Extra I can place stack_calc inside nested loop, but it's going to be uglier and less readable. At least for me.
# ---------------------------
# Changed______
#  Using this monstrosity with converting str -> int, cuz I don't want to make extra loop to change all cells to int.
#  It's going to be slower than this ^^. But it's very bad looking and error_prone.
#  Will change and see diff in speed after first correct commit.
# ---------------------------
# After failing with p84 and googling for a method, get a glimpse of STACK problems, and this is one of them.
# We can just assume that this matrix rows as histograms,
# and every bar will have a height of cells with 1 + any 1 above (base should be 1, can't place anything on empty spot).


test: list[list[str]] = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
test_out: int = 6
assert test_out == maximal_rectangle(test)

test = [["0"]]
test_out = 0
assert test_out == maximal_rectangle(test)

test = [["1"]]
test_out = 1
assert test_out == maximal_rectangle(test)

test = [[choice(['0', '1']) for _ in range(200)] for _ in range(200)]
print(test)
