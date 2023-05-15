# You are given an m x n integer matrix with the following two properties:
#   1) Each row is sorted in non-decreasing order.
#   2) The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# m == matrix.length  ,  n == matrix[i].length
# 1 <= m, n <= 100  ,  -104 <= matrix[i][j], target <= 104

# ! You must write a solution in O(log(m * n)) time complexity. !


def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    # working_sol (33.54%, 15.5%) -> (53ms, 16.9mb)  time: O(m + n) | space: O(1)
    if target > matrix[-1][-1]:
        return False
    if target < matrix[0][0]:
        return False
    row_length: int = len(matrix[0])
    for y in range(len(matrix)):
        if row_length == 1:
            if matrix[y][0] == target:
                return True
        if matrix[y][0] <= target <= matrix[y][-1]:
            for x in range(row_length):
                if matrix[y][x] == target:
                    return True
            return False

# Time complexity: O(m + n) -> worst case, looping whole height of input_matrix => O(m) ->
#                                   -> looping once through row of input_matrix length => O(n) ->
#                                   -> O(m + n)
#                  ! Not sure about this ^^, cuz it's nested loop, but it's triggering once and returning after it,
#                    totally need to learn how to calculate it with formulas. !
#                  -----------
#                  Ω(m) or Ω(n) -> best case, 1row or 1 column and looping once through.
#                  -----------
#                  Θ(log(m + n)) -> median case, looping only part of height => Θ(log(m) ->
#                                   -> and part of a row with size of input_matrix length == n => Θ(log(n)) ->
#                                   -> Θ(log(m + n)
# Space complexity: O(1) -> no extras and 1 constant.

# Brain-lag, I was thinking that we need to return value in range(row(first_index), row(last_index)).
# But I need to find particular number, not just being in range.
# --------------------------------
# Tricky moments I know:
#   target > matrix[-1][-1] => target > max_value
#   target < matrix[0][0] => target < min_value
#   matrix is one row, or column
# ! The first integer of each row is greater than the last integer of the previous row. !
# Totally need to take a breaks, before rushing solution, cuz there's definition ^^ of ascending matrix.
# every [y][0] < [y][-1] and [y][-1] < [y + 1][0] <- it's in a description...


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

test4 = [[1, 2, 3]]
test4_target = 3
test4_out = True
print(search_2d_matrix(test4, test4_target))
