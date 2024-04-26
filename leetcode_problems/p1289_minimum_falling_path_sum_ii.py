# Given an n x n integer matrix grid,
#  return the minimum sum of a falling path with non-zero shifts.
# A falling path with non-zero shifts is a choice of exactly one element from each row of grid
#  such that no two elements chosen in adjacent rows are in the same column.
# --------------------------
# n == grid.length == grid[i].length
# 1 <= n <= 200
# -99 <= grid[i][j] <= 99
from random import randint
from functools import cache


def min_falling_path_sum(grid: list[list[int]]) -> int:
    # working_sol (13.71%, 5.31%) -> (5995ms, 40.29mb)  time: O(m * n * m) | space: O(m * n)
    if 1 == len(grid):
        return min(grid[0])

    @cache
    def check(cur_row: int, cur_col: int) -> int:
        if len(grid) - 1 == cur_row:
            return grid[cur_row][cur_col]
        min_way = 99 * 200  # 200 rows with 99 max_value possible
        for column in range(len(grid[cur_row])):
            if column != cur_col:
                min_way = min(min_way, check(cur_row + 1, column))
        return grid[cur_row][cur_col] + min_way

    out: int = 99 * 200
    for col in range(len(grid[0])):
        out = min(out, check(0, col))
    return out


# Time complexity: O(m * n * m) <- m - length of input matrix `grid` , n - height of input matrix `grid`.
# We're using `cache` and only calculate each cell once, but for each cell we're looping every column except 1.
# O(m * n * (m -  1))
# --------------------------
# Auxiliary space: O(m * n)
# We store every result of calc for every cel => O(m * n).
# --------------------------
# Build correct top-down, by myself. But failed to pass the time Limit.
# And only because I was checking last ROW like (cur_row == len(grid): return 0)
# Which is correct, and store our last row values as intended, but it extra didn't pass the time Limit.
# Everything else was correct and surprisingly equal to editorial ;)
# Not using bot-up, like 50% of commits. Because it's too much to come up with it by myself.


test: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_out: int = 13
assert test_out == min_falling_path_sum(test)

test = [[7]]
test_out = 7
assert test_out == min_falling_path_sum(test)

test = [[randint(-99, 99) for _ in range(200)] for _ in range(200)]
print(test)
