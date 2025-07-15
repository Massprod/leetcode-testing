# You are given a 2D binary array grid.
# Find a rectangle with horizontal and vertical sides with the smallest area,
#  such that all the 1's in grid lie inside this rectangle.
# Return the minimum possible area of the rectangle.
# -------------------------
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 0 or 1.
# The input is generated such that there is at least one 1 in grid.
from random import choice

from pyperclip import copy


def minimum_area(grid: list[list[int]]) -> int:
    # working_sol (30.13%, 49.36%) -> (2995ms, 47.65mb)  time: O(m * n) | space: O(1)
    first_row: int = len(grid)
    last_row: int = 0

    first_col: int = len(grid)
    last_col: int = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 1 != grid[row][col]:
                continue
            first_row = min(first_row, row)
            first_col = min(first_col, col)
            last_row = max(last_row, row)
            last_col = max(last_col, col)
    
    out: int = (1 + (last_row - first_row)) * (1 + (last_col - first_col))
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `grid`,
#                              n - height of the input matrix `grid`.
# Always traversing the whole input matrix `grid`, once => O(m * n).
# -------------------------
# Auxiliary space: O(1)


test: list[list[int]] = [[0, 1, 0], [1, 0, 1]]
test_out: int = 6
assert test_out == minimum_area(test)

test = [[1, 0], [0, 0]]
test_out = 1
assert test_out == minimum_area(test)

test = [[0], [1]]
test_out = 1
assert test_out == minimum_area(test)

test = [[choice([0, 1]) for _ in range(1000)] for _ in range(1000)]
copy(test)
