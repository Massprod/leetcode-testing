# Given an m x n binary matrix filled with 0's and 1's,
#  find the largest square containing only 1's and return its area.
# ------------------
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
from random import randint


def maximal_square(matrix: list[list[str | int]]) -> int:
    # working_sol (57.24%, 63.48%) -> (607ms, 19.26mb)  time: O(m * n) | space: O(1)
    max_side: int = 0
    # We start DP from 1 row and 1 col, cuz we only care about top, top-left, left cells.
    # So, we need extra check to see if we have 1x1 squares on 1 row, and column.
    if '1' in matrix[0]:
        max_side = 1
    if not max_side:
        for row in range(len(matrix)):
            if matrix[row][0] == '1':
                max_side = 1
                break
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][col] == '1':
                matrix[row][col] = 1 + min(
                    # All 3 are sides of maximum squares we can build on these cells.
                    # We can continue minimal square of these squares with our new '1' on matrix[row][col].
                    int(matrix[row - 1][col]),
                    int(matrix[row - 1][col - 1]),
                    int(matrix[row][col - 1]),
                )
                max_side = max(max_side, matrix[row][col])
    # sq_area = side * side
    return max_side ** 2


# Time complexity: O(m * n) < m - number of rows in `matrix`, n - number of columns in `matrix`.
# Traversing input matrix `matrix` indexes once.
# And for rows > 0, col > 0 we're doing constant min() operation => O(m * n).
# ------------------
# Auxiliary space: O(1).


test: list[list[str]] = [
    ["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]
]
test_out: int = 4
assert test_out == maximal_square(test)

test = [["0", "1"], ["1", "0"]]
test_out = 1
assert test_out == maximal_square(test)

test = [["0"]]
test_out = 0
assert test_out == maximal_square(test)

test = [[str(randint(0, 1)) for _ in range(300)] for _ in range(300)]
print(test)
