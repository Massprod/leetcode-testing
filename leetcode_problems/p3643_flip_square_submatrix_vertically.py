# You are given an m x n integer matrix grid, and three integers x, y, and k.
# The integers x and y represent the row and column indices of the top-left corner
#  of a square submatrix and the integer k represents the size (side length) of the square submatrix.
# Your task is to flip the submatrix by reversing the order of its rows vertically.
# Return the updated matrix
# --- --- --- ---
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 100
# 0 <= x < m
# 0 <= y < n
# 1 <= k <= min(m - x, n - y)


def reverse_submatrix(grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
    # working_solution: (100%, 6.46%) -> (0ms, 18.24mb)  Time: O(n * m) Space: O(1)
    flip_rows: int = k
    # Nothing to flip.
    if 1 == flip_rows:
        return grid
    # 1 <= k <= min(m - x, n - y) <- we're always in boundaries.
    start_row: int = x
    start_col: int = y

    end_row: int = x + k - 1
    end_col: int = y + k  # we don't need to `-1`, because we ignore it in the loop
    while start_row < end_row:
        for column in range(start_col, end_col):
            grid[start_row][column], grid[end_row][column] = (
                grid[end_row][column], grid[start_row][column]
            )
        start_row += 1
        end_row -= 1

    return grid


# Time complexity: O(n * m) <- n - length of the input matrix `grid`,
#                              m - height of the input matrix `grid`.
# In the worst case, whole matrix is a submatrix.
# We will use every cell of the input matrix `grid`, once => O(n * m).
# --- --- --- ---
# Space complexity: O(1)


test_grid: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
test_x: int = 1
test_y: int = 0
test_k: int = 3
test_out: list[list[int]] = [
    [1, 2, 3, 4],
    [13, 14, 15, 8],
    [9, 10, 11, 12],
    [5, 6, 7, 16],
]
assert test_out == reverse_submatrix(test_grid, test_x, test_y, test_k)

test_grid = [
    [3, 4, 2, 3],
    [2, 3, 4, 2],
]
test_x = 0
test_y = 2
test_k = 2
test_out = [
    [3, 4, 4, 2],
    [2, 3, 2, 3],
]
assert test_out == reverse_submatrix(test_grid, test_x, test_y, test_k)
