# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# -------------------
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2 ** 31 <= matrix[i][j] <= 2 ** 31 - 1
# -------------------
# Follow up:
#   A straightforward solution using O(mn) space is probably a bad idea.
#   A simple improvement uses O(m + n) space, but still not the best solution.
#   Could you devise a constant space solution?


def set_zeroes(matrix: list[list[int | str]]):
    # working_sol (49.4%, 95.13%) -> (118ms, 17.1mb)  time: O(m * n) | space: O(1)
    # Mark of zeroed cells.
    mark: str = '-'
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                # Nullify row.
                for zero_row in range(0, len(matrix)):
                    if matrix[zero_row][col] == 0:
                        continue
                    matrix[zero_row][col] = mark
                # Nullify column.
                for zero_col in range(0, len(matrix[0])):
                    if matrix[row][zero_col] == 0:
                        continue
                    matrix[row][zero_col] = mark
    # Set marked cells as 0.
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == mark:
                matrix[row][col] = 0


# Time complexity: O(m * n) -> fully traversing matrix, twice => O(2 * (m * n))
# m - height of input matrix^^|
# n - length of input matrix^^|
# Auxiliary space: O(1) -> only 1 constant INT, doesn't depend on input => O(1).


test: list[list[int]] = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
test_out: list[list[int]] = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
set_zeroes(test)
assert test == test_out

test = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
test_out = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
set_zeroes(test)
assert test == test_out

test = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
test_out = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
set_zeroes(test)
assert test == test_out

test = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
test_out = [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
set_zeroes(test)
assert test == test_out

test = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]
test_out = [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 3], [0, 0, 0, 0]]
set_zeroes(test)
assert test == test_out
