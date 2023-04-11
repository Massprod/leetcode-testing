# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
from numpy import matrix as mt


def rotate(matrix: list[list[int]]) -> None | list[list[int]]:
    # working 96.73% 19.38%
    length = len(matrix)
    for y in range(int(length / 2)):
        for x in range(y, length - y - 1):
            temp = matrix[x][length - y - 1]
            matrix[x][length - y - 1] = matrix[y][x]
            temp2 = matrix[length - y - 1][length - x - 1]
            matrix[length - y - 1][length - x - 1] = temp
            temp = matrix[length - x - 1][y]
            matrix[length - x - 1][y] = temp2
            matrix[y][x] = temp
    return matrix


# Already worked with matrix_creating-appending-clock-counter_clock and all.
# But this one is new, and I just tried to brute force switching row into a column and this worked :)
# 0 row , y = 0, 0 index x = 0
# [0][max] - saved       _right_top
# [0][0] -> [0][max]     _new_right_top
# [max][max] - saved     _right_bot
# [max][max] -> [0][max] _new_right_bot
# [max][0] - saved       _left_bot
# [max][0] -> [max][max] _new_left_bot
# [0][0] -> [max][0]      _new_left_top
# repeating for length / 2 times . for every 'square' we can run it through


test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test1_out = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
test2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
test2_out = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
# print(mt(test1))
print(mt(test2))
# print(mt(rotate(test1)))
print(mt(rotate(test2)))
# print(rotate(test1))
assert rotate(test1) == test1_out
assert rotate(test2) == test2_out
