# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal,
#  switching the matrix's row and column indices.
# -------------------------
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10 ** 5
# -10 ** 9 <= matrix[i][j] <= 10 ** 9
from random import randint


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    # working_sol (91.30%, 81.62%) -> (66ms, 17.09mb)  time: O(m * n) | space: O(m * n)
    # # of columns == # of new rows.
    out: list[list[int]] = [[] for _ in matrix[0]]
    # Every value on the column == new values on the new rows.
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            out[col].append(matrix[row][col])
    return out


# Time complexity: O(m * n) <- m - length of input matrix `matrix`, n - height of input matrix `matrix`.
# Using every index of original input `matrix`.
# Auxiliary space: O(m * n).
# We're simply transpose matrix, it's still going to have the same size.
# Don't see how to do this in_place, if we have different row and col sizes.


test: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_out: list[list[int]] = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert test_out == transpose(test)

test = [[1, 2, 3], [4, 5, 6]]
test_out = [[1, 4], [2, 5], [3, 6]]
assert test_out == transpose(test)

test = [[randint(-10 ** 9, 10 ** 9) for _ in range(12)] for _ in range(99)]
print(test)
