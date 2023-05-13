# Given an m x n grid filled with non-negative numbers,
# find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
from random import randint
import numpy


def create_matrix(height: int, length: int):
    matrix = [[0] * length for _ in range(height)]
    for _ in matrix:
        for x in range(0, len(_)):
            _[x] = randint(1, 3)
    return matrix


def short_path(matrix: list[list[int]], start_x: int = 0, start_y: int = 0) -> int:
    # working_sol (29.77%, 15.36%) -> (108ms, 18mb)  time: O( ) | space: O( )
    max_y: int = len(matrix)
    max_x: int = len(matrix[0])
    if not 0 <= start_y < max_y or not 0 <= start_x < max_x:
        raise ValueError("Starting coordinates: start_y, start_x out of bounds.")
    # sum first_row
    for x in range(start_x + 1, max_x):
        matrix[start_y][x] = matrix[start_y][x] + matrix[start_y][x - 1]
    # sum first_column
    for y in range(start_y + 1, max_y):
        matrix[y][start_x] = matrix[y][start_x] + matrix[y - 1][start_x]
    # sum everything_else with less resistance way
    for y in range(start_y + 1, max_y):
        for x in range(start_x + 1, max_x):
            vert: int = matrix[y - 1][x]
            horiz: int = matrix[y][x - 1]
            # diag = matrix[y-1][x-1] - for ‾\ move option, if we're moving from top_left to bot_right
            matrix[y][x] = min(vert, horiz) + matrix[y][x]
    shortest_sum = matrix[max_y - 1][max_x - 1]
    return shortest_sum


# Time complexity: O(n * m) -> looping once through whole input of m * n size -> first_row_loop => O(max_x) ->
# max_y - height ^^            -> first_column_loop => O(max_y)
# max_x - length ^^            -> nested loop for 1 <= y <= (max_y - 1) and 1 <= x <= (max_x - 1)
#                                 depends on size of input_matrix (max_y * max_y) => O(max_y * max_x)
#                              -> O(n * m) - where: max_y = n, max_x = m (for better look)
# ! Before revisit, I was making tasks in different style and there's -> start_x, start_y
#   which give us a starting cell to count from -> we can count from any start_cell and find shortest_sum
#   worst case will be same => O(n * m),
#   but the best case => Ω(log(n * m)) <- cuz we're skipping some part of the matrix !
# ------------------------------
# Space complexity: O(1) -> only 3 extra constants: max_y, max_x, shortest_sum(can be changed to return [-1][-1]).
# ------------------------------

test1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
test1_out = 7
assert short_path(test1) == test1_out

test2 = [[1, 2, 3], [4, 5, 6]]
test2_out = 12
assert short_path(test2) == test2_out

original = create_matrix(height=18, length=15)
print(numpy.matrix(original))
my_short = short_path(original)
print(numpy.matrix(original))
print(my_short)
