# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal
# and all the elements on the secondary diagonal that are not part of the primary diagonal.
# --------------------
# n == mat.length == mat[i].length
# 1 <= n <= 100  ,  1 <= mat[i][j] <= 100


def diagonal_sum(mat: list[list[int]]) -> int:
    pass


test1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
test1_out = 25

test2 = mat = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
test2_out = 8

test3 = [[5]]
test3_out = 5
