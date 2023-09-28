# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
# -----------------
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


def rotate(matrix: list[list[int]]) -> None:
    # working_sol (99.49%, 100%) -> (28ms, 16.2mb)  time: O(n * n) | space: O(1)
    # Switching all rows once in clockwise for every square.
    # Example:
    # 0 row, y = 0, 0 column x = 0 <- start.
    # [0][max] - saved       _right_top
    # [0][0] -> [0][max]     _new_right_top
    # [max][max] - saved     _right_bot
    # [max][max] -> [0][max] _new_right_bot
    # [max][0] - saved       _left_bot
    # [max][0] -> [max][max] _new_left_bot
    # [0][0] -> [max][0]      _new_left_top
    # Repeating for every value on a row^^.
    # Repeat for (length // 2) times, for every 'square' we can run it through.
    length: int = len(matrix)
    for row in range(length // 2):
        for col in range(row, length - row - 1):
            first: int = matrix[col][length - row - 1]
            matrix[col][length - row - 1] = matrix[row][col]
            second: int = matrix[length - row - 1][length - col - 1]
            matrix[length - row - 1][length - col - 1] = first
            first: int = matrix[length - col - 1][row]
            matrix[length - col - 1][row] = second
            matrix[row][col] = first


# Time complexity: O(n * n) -> essentially traversing whole input matrix, using every cell only once => O(n * n).
# n - len of input square matrix^^|
# Auxiliary space: O(1) -> only 2 extra constant INTs used, none of them depends on input => O(1).
# -----------------
# Already worked with matrix_creating-appending-clock-counter_clock and all.
# But this one is new, and I just tried to brute force switching row into a column and this worked :)
# 0 row , y = 0, 0 column x = 0
# [0][max] - saved       _right_top
# [0][0] -> [0][max]     _new_right_top
# [max][max] - saved     _right_bot
# [max][max] -> [0][max] _new_right_bot
# [max][0] - saved       _left_bot
# [max][0] -> [max][max] _new_left_bot
# [0][0] -> [max][0]      _new_left_top
# repeating for (length // 2 times) . for every 'square' we can run it through


test: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_out: list[list[int]] = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
rotate(test)
assert test == test_out

test = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
test_out = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
rotate(test)
assert test == test_out
