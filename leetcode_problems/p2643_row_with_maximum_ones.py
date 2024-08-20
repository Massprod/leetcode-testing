# Given a m x n binary matrix mat, find the 0-indexed position
#  of the row that contains the maximum count of ones, and the number of ones in that row.
# In case there are multiple rows that have the maximum count of ones,
#  the row with the smallest row number should be selected.
# Return an array containing the index of the row,
#  and the number of ones in it.
# ----------------------------
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.
from random import choice


def row_and_maximum_ones(mat: list[list[int]]) -> list[int]:
    # working_sol (74.71%, 80.08%) -> (736ms, 17.00mb)  time: O(n * m) | space: O(1)
    out_index: int = 0
    out_count: int = 0
    for row in range(len(mat)):
        cur_count: int = mat[row].count(1)
        if out_count < cur_count:
            out_index, out_count = row, cur_count
    return [out_index, out_count]


# Time complexity: O(n * m) <- n - height of the input matrix `mat`, m - length of the input matrix `mat`.
# Always traversing whole input matrix `mat`, once => O(n * m).
# ----------------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1).


test: list[list[int]] = [[0, 1], [1, 0]]
test_out: list[int] = [0, 1]
assert test_out == row_and_maximum_ones(test)

test = [[0, 0, 0], [0, 1, 1]]
test_out = [1, 2]
assert test_out == row_and_maximum_ones(test)

test = [[0, 0], [1, 1], [0, 0]]
test_out = [1, 2]
assert test_out == row_and_maximum_ones(test)

test = [[choice([0, 1]) for _ in range(100)] for _ in range(100)]
print(test)
