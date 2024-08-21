# A square matrix is said to be an X-Matrix if both of the following conditions hold:
#  - All the elements in the diagonals of the matrix are non-zero.
#  - All other elements are 0.
# Given a 2D integer array grid of size n x n representing a square matrix,
#  return true if grid is an X-Matrix. Otherwise, return false.
# ------------------------
# n == grid.length == grid[i].length
# 3 <= n <= 100
# 0 <= grid[i][j] <= 10 ** 5


def check_x_matrix(grid: list[list[int]]) -> bool:
    # working_sol (82.26%, 23.95%) -> (210ms, 17.61mb)  time: O(m * n) | space: O(1)
    desc_diag_val: int = 0
    asc_diag_val: int = len(grid) - 1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if desc_diag_val == (row - col):
                if grid[row][col]:
                    continue
                else:
                    return False
            if asc_diag_val == (row + col):
                if grid[row][col]:
                    continue
                else:
                    return False
            if grid[row][col]:
                return False
    return True


# Time complexity: O(m * n) <- m - length of the input matrix `grid`, n - height of the input matrix `grid`.
# Always traversing whole input matrix `grid`, once => O(m * n).
# ------------------------
# Auxiliary space: O(1).
# Only 2 constant INTs used, none of them depends on input => O(1).


test: list[list[int]] = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]
test_out: bool = True
assert test_out == check_x_matrix(test)

test = [[5, 7, 0], [0, 3, 1], [0, 5, 0]]
test_out = False
assert test_out == check_x_matrix(test)
