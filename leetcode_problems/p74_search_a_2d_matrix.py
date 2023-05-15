# You are given an m x n integer matrix with the following two properties:
#   1) Each row is sorted in non-decreasing order.
#   2) The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# m == matrix.length  ,  n == matrix[i].length
# 1 <= m, n <= 100  ,  -104 <= matrix[i][j], target <= 104

# ! You must write a solution in O(log(m * n)) time complexity. !


def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    if matrix[0][0] > target:
        return False
    if matrix[-1][-1] < target:
        return False
    row_length: int = len(matrix[0])
    for y in range(len(matrix)):
        if row_length == 1:
            if matrix[y][0] == target:
                return True
        if matrix[y][0] <= target <= matrix[y][1]:
            return True
    return False

# All we need to check is first_column and last_column.
# But it's too easy and task is medium, tricky moments I know:
#   target > matrix[-1][-1] => target > max_value
#   target < matrix[0][0] => target < min_value
# ! The first integer of each row is greater than the last integer of the previous row. !
# But there's no info about, whole matrix, all values in ascending order or just in a particular row?
# Because if values only in ascending order in a row, and not whole matrix, than we can't skip any rows.


test1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test1_target = 3
test1_out = True
print(search_2d_matrix(test1, test1_target))

test2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test2_target = 13
test2_out = False
print(search_2d_matrix(test2, test2_target))

# test3 - failed - yep, tricky moments I didn't consider. Matrix can a 1 column or 1 row.
test3 = [[1]]
test3_target = 1
test3_out = True
print(search_2d_matrix(test3, test3_target))
