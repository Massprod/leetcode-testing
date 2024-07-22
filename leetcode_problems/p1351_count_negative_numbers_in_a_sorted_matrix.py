# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
#  return the number of negative numbers in grid.
# ---------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
# ---------------------
# Follow up: Could you find an O(n + m) solution?


def count_negatives(grid: list[list[int]]) -> int:
    # working_sol (72.53%, 89.04%) -> (100ms, 17.51mb)  time: O(n + m) | space: O(1)
    cur_row: int = len(grid) - 1
    cur_col: int = 0
    out: int = 0
    while cur_col < len(grid[0]) and 0 <= cur_row:
        if 0 > grid[cur_row][cur_col]:
            out += len(grid[0]) - cur_col
            cur_row -= 1
        else:
            cur_col += 1
    return out


# Time complexity: O(n + m) <- n - height of the input matrix `grid`, m - length of the input matrix `grid`.
# We're always using `rows` and `cols`, only once => O(n + m).
# ---------------------
# Auxiliary space: O(1).
# Only 3 constant INT's used, none of them depends on input => O(1).


test: list[list[int]] = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
test_out: int = 8
assert test_out == count_negatives(test)

test = [[3, 2], [1, 0]]
test_out = 0
assert test_out == count_negatives(test)
