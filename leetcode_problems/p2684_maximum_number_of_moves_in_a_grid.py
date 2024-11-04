# You are given a 0-indexed m x n matrix grid consisting of positive integers.
# You can start at any cell in the first column of the matrix, and traverse the grid in the following way:
#  - From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1)
#   and (row + 1, col + 1) such that the value of the cell you move to,
#   should be strictly bigger than the value of the current cell.
# Return the maximum number of moves that you can perform.
# --------------------------
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 10 ** 5
# 1 <= grid[i][j] <= 10 ** 6
from random import randint
from functools import cache


def max_moves(grid: list[list[int]]) -> int:
    # working_sol (48.48%, 5.30%) -> (170ms, 43.12mb)  time: O(n * m) | space: O(n * m)
    # [ asc_diag, row, desc_diag]
    options: list[tuple[int, int]] = [
        (-1, 1), (0, 1), (1, 1)
    ]

    @cache
    def dfs(row: int, col: int) -> int:
        if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
            return 0
        out: int = 0
        for dy, dx in options:
            new_row: int = row + dy
            new_col: int = col + dx
            if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]))\
                    and grid[new_row][new_col] > grid[row][col]:
                out = max(out, 1 + dfs(new_row, new_col))
        return out

    _out: int = 0
    for _row in range(len(grid)):
        _out = max(_out, dfs(_row, 0))
    return _out


# Time complexity: O(m * n) <- n - length of the input matrix `grid`, m - height of the input matrix `grid`.
# Always traversing whole input array `grid`, once => O(m * n).
# We memorize every cell, we visit == every cell will be used once.
# --------------------------
# Auxiliary space: O(m * n)
# Every cell we visit is cached with `cache` => O(m * n).


test: list[list[int]] = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
test_out: int = 3
assert test_out == max_moves(test)

test = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
test_out = 0
assert test_out == max_moves(test)

test = [[randint(1, 10 ** 6) for _ in range(444)] for _ in range(222)]
print(test)
