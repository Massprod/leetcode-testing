# You are given an m x n integer matrix matrix with the following two properties:
#   - Each row is sorted in non-decreasing order.
#   - The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# ----------------------
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10 ** 4 <= matrix[i][j], target <= 10 ** 4
from random import randint


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # working_sol (89.25%, 40.17%) -> (48ms, 16.82mb)  time: O(log(m * n)) | space: O(1)
    # O(log(m * n)):
    # (log m) <- to find row
    # (log n) <- to find inside the row
    # O(log m + log n) == O(log(m * n)).
    # First find the correct row with BinarySearch.
    left: int = 0
    right: int = len(matrix) - 1
    while left < right:
        middle: int = (left + right) // 2 + 1
        # We need higher.
        if matrix[middle][0] <= target:
            left = middle
        # We need lower.
        else:
            right = middle - 1
    # Try to find 'target' on this row.
    row: int = left
    left = 0
    right = len(matrix[row]) - 1
    while left < right:
        middle = (left + right) // 2 + 1
        if matrix[row][middle] <= target:
            left = middle
        else:
            right = middle - 1
    return matrix[row][left] == target


# Time complexity: O(log(m * n) <- n - length of input matrix 'matrix', m - height of input matrix 'matrix'.
# (log m) <- BS to find row
# (log n) <- BS to find inside the row
# O(log m + log n) == O(log (m * n)).
# Auxiliary space: O(1).
# Standard BS with only 2 constant INTS, none of them depends on input.


test: list[list[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test_target: int = 3
test_out: bool = True
assert test_out == search_matrix(test, test_target)

test = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test_target = 13
test_out = False
assert test_out == search_matrix(test, test_target)

test = sorted([[randint(-10 ** 4, 10 ** 4)] for _ in range(100)])
for row_ in range(len(test) - 1):
    test[row_] += sorted([randint(test[row_][0], test[row_ + 1][0] - 1) for _ in range(99)])
test[-1] += sorted([randint(test[-1][0], 10 ** 4) for _ in range(99)])
print(test)
