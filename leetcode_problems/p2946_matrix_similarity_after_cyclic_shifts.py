# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.
# The following proccess happens k times:
# - Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
# - Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
# Return true if the final modified matrix after k steps is identical
#  to the original matrix, and false otherwise.
# --------------------
# 1 <= mat.length <= 25
# 1 <= mat[i].length <= 25
# 1 <= mat[i][j] <= 25
# 1 <= k <= 50
from pyperclip import copy

from random import randint


def are_similar(mat: list[list[int]], k: int) -> bool:
    # working_sol (75.69%, 69.27%) -> (1ms, 17.89mb)  time: O(n * m) | space: O(1)
    new_index: int
    shifts: int = k % len(mat[0])
    # Even rows -> to the left, 0 index == start from last index (or go negative)
    for even_row in range(0, len(mat), 2):
        for index in range(len(mat[even_row])):
            # We're python_bois == we can use negative indexing.
            # Or, we will just get a last index and take w.e left of shift there.
            # Like: len(mat[even_row] - 1) + (index - shifts) <- if it's negative.
            new_index = (index - shifts)
            if mat[even_row][index] != mat[even_row][new_index]:
                return False
    # Odd rows -> to the right, limit == start from 0
    for odd_row in range(1, len(mat), 2):
        for index in range(len(mat[odd_row])):
            new_index = (index + shifts) % len(mat[odd_row])
            # W.e the place we shifted, we still need to check with original
            if mat[odd_row][index] != mat[odd_row][new_index]:
                return False
    
    return True


# Time complexity: O(n * m) <- n - length of the input matrix `mat`,
#                              m - height of the input matrix `mat`.
# Always traversing whole input matrix `mat`, once => O(n * m).
# --------------------
# Auxiliary space: O(1)
# Only 2 constant  INTs used, none of them depends on input => O(1).


test: list[list[int]] = [[1,2,3],[4,5,6],[7,8,9]]
test_k: int = 4
test_out: bool = False
assert test_out == are_similar(test, test_k)

test = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
test_k = 2
test_out = True
assert test_out == are_similar(test, test_k)

test = [[2,2],[2,2]]
test_k = 3
test_out = True
assert test_out == are_similar(test, test_k)

test = [[randint(1, 25) for _ in range(25)] for _ in range(25)]
copy(test)
