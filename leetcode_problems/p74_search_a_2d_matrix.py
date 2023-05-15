# You are given an m x n integer matrix with the following two properties:
#   1) Each row is sorted in non-decreasing order.
#   2) The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# m == matrix.length  ,  n == matrix[i].length
# 1 <= m, n <= 100  ,  -104 <= matrix[i][j]  , target <= 104

# ! You must write a solution in O(log(m * n)) time complexity. !


def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    pass


test1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test1_target = 3
test1_out = True

test2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test2_target = 13
test2_out = False
