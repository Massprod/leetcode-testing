# You are given an m x n binary matrix grid.
# A row or column is considered palindromic if its values
#  read the same forward and backward.
# You can flip any number of cells in grid from 0 to 1, or from 1 to 0.
# Return the minimum number of cells that need to be flipped
#  to make either all rows palindromic or all columns palindromic.
# --------------------
# m == grid.length
# n == grid[i].length
# 1 <= m * n <= 2 * 10 ** 5
# 0 <= grid[i][j] <= 1


def min_flips(grid: list[list[int]]) -> int:
    # working_sol (79.62%, 57.31%) -> (139ms, 58.22mb)  time: O(m * n) | space: O(1)
    rows_count: int = 0
    # Rows check.
    for row in range(len(grid)):
        row_flips: int = 0
        left_p: int = 0
        right_p: int = len(grid[row]) - 1
        while left_p < right_p:
            left_v: int =  grid[row][left_p]
            right_v: int = grid[row][right_p]
            row_flips += 1 if left_v != right_v else 0
            left_p += 1
            right_p -= 1

        rows_count += row_flips
    # Cols check
    col_count: int = 0
    for column in range(len(grid[0])):
        col_flips: int = 0
        top_p: int = 0
        bot_p: int = len(grid) - 1
        while top_p < bot_p:
            top_v: int = grid[top_p][column]
            bot_v: int = grid[bot_p][column]
            col_flips += 1 if top_v != bot_v else 0
            top_p += 1
            bot_p -= 1
        
        col_count += col_flips

    return min(rows_count,  col_count)


# Time complexity: O(m * n) < - m - length of the input matrix `grid`,
#                               n - height of the input matrix `grid`.
# Always traversing whole input matrix `grid`, twice => O(m * n).
# --------------------
# Auxiliary space: O(1)


test: list[list[int]] = [[1, 0, 0], [0, 0 ,0], [0, 0, 1]]
test_out: int = 2
assert test_out == min_flips(test)

test = [[0, 1], [0, 1], [0, 0]]
test_out = 1
assert test_out == min_flips(test)

test = [[1], [0]]
test_out = 0
assert test_out == min_flips(test)
