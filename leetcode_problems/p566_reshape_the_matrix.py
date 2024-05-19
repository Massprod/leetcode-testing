# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix
#  into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing
#  the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements
#  of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal,
#  output the new reshaped matrix; Otherwise, output the original matrix.
# -----------------------------------
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300
from random import randint
from collections import deque


def matrix_reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    # working_sol (97.28%, 6.34%) -> (64ms, 17.82mb)  time: O(m * n) | space: O(m * n)
    reshaped: list[list[int]] = [[0 for _ in range(c)] for _ in range(r)]
    all_values: deque[int] = deque([])
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            all_values.append(mat[row][col])
    # The trickiest part of the TASK is that we need to reshape in STRICTLY (r * c) matrix.
    # Not leaving anything empty, or extras.
    if (r * c) != len(all_values):
        return mat
    for row in range(r):
        for col in range(c):
            if all_values:
                reshaped[row][col] = all_values.popleft()
            else:
                break
    return reshaped


# Time complexity: O(m * n) <- m - rows of input matrix `mat`, n - columns of input matrix `mat`.
# We're always traversing the whole input matrix to get all the values from it => O(m * n).
# And because we need to create ONLY (r * c) matrix, we also use the same values again => O(2 * m * n).
# -----------------------------------
# Auxiliary space: O(m * n)
# `all_values` will store all values from the `mat` => O(m * n).
# `reshaped` is always of the size (r * c), but we only create new matrix if it can hold `all_values` => O(2 * m * n)


test: list[list[int]] = [[1, 2], [3, 4]]
test_r: int = 1
test_c: int = 4
test_out: list[list[int]] = [[1, 2, 3, 4]]
assert test_out == matrix_reshape(test, test_r, test_c)

test = [[1, 2], [3, 4]]
test_r = 2
test_c = 4
test_out = [[1, 2], [3, 4]]
assert test_out == matrix_reshape(test, test_r, test_c)

test = [[randint(-1000, 1000) for _ in range(100)] for _ in range(100)]
print(test)
