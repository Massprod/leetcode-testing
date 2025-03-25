# You are given an m x n integer matrix grid.
# Return the maximum sum of the elements of an hourglass.
# Note that an hourglass cannot be rotated
#  and must be entirely contained within the matrix.
# ----------------------
# m == grid.length
# n == grid[i].length
# 3 <= m, n <= 150
# 0 <= grid[i][j] <= 10 ** 6
from random import randint

from pyperclip import copy


def max_sum(grid: list[list[int]]) -> int:
    # working_sol (87.63%, 21.21%) -> (29ms, 20.30mb)  time: O(m * n) | space: O(m * n + n)
    # Prefix sums and use them to get a diff.
    prefixes: list[list[int]] = [[0] for _ in range(len(grid))]

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            prefixes[row].append(
                grid[row][column] + prefixes[row][-1]
            )
    
    out: int = 0
    start_row: int = 0
    end_row: int = len(grid) - 2
    end_col: int = 2
    for row in range(start_row, end_row):
        for column in range(end_col, len(grid[row])):
            cur_sum: int = 0
            start_col: int = column - 2
            cur_row: int = row
            # `column + 1` <- because we're using prefix sum.
            # First glass row.
            cur_sum += prefixes[cur_row][column + 1] - prefixes[cur_row][start_col]
            # Second glass row.
            cur_row += 1
            cur_sum += grid[cur_row][column - 1]
            # Third glass row.
            cur_row += 1
            cur_sum += prefixes[cur_row][column + 1] - prefixes[cur_row][start_col]
            out = max(out, cur_sum)
    
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `grid`,
#                              n - height of the input matrix `grid`.
# Always traversing whole input matrix `grid` to get prefixes, once => O(m * n).
# Extra traversing all `hourGlass` options, essentially whole matrix without 2 rows =>
# => O(2 * m * n) <- linear anyway.
# ----------------------
# Auxiliary space: O(m * n + n)
# `prefixes` <- allocates space for each index of the `grid`,
# and extra +1 for each row => O(n * m + n).


test: list[list[int]] = [[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]
test_out: int = 30
assert test_out == max_sum(test)

test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_out = 35
assert test_out == max_sum(test)

test = [
    [randint(0, 10 ** 6) for _ in range(150)] for _ in range(150)
]
copy(test)
