# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
from random import randint
import numpy
import copy


def create_matrix(height: int, length: int):
    matrix = [[0] * length for _ in range(height)]
    for _ in matrix:
        for x in range(0, len(_)):
            _[x] = randint(1, 3)
    return matrix


def short_path(matrix: list[list[int]], start_x: int = 0, start_y: int = 0) -> int:
    max_y = len(matrix)
    max_x = len(matrix[0])
    if not 0 <= start_y < max_y or not 0 <= start_x < max_x:
        raise ValueError("Starting coordinates: start_y, start_x out of bounds.")
    # sum horizontal
    for x in range(start_x + 1, max_x):
        matrix[start_y][x] = matrix[start_y][x] + matrix[start_y][x - 1]
    # sum vertical
    for y in range(start_y + 1, max_y):
        matrix[y][start_x] = matrix[y][start_x] + matrix[y - 1][start_x]
    # sum empty
    for y in range(start_y + 1, max_y):
        for x in range(start_x + 1, max_x):
            vert = matrix[y - 1][x]
            horiz = matrix[y][x - 1]
            # diag = matrix[y-1][x-1] - for ‾\ move option, if we're moving from top_left to bot_right
            matrix[y][x] = min(vert, horiz) + matrix[y][x]
    shortest_sum = matrix[max_y - 1][max_x - 1]
    print(numpy.matrix(matrix))
    return shortest_sum


original = create_matrix(height=18, length=15)
test = copy.deepcopy(original)
print(numpy.matrix(original))
my_short = short_path(test)
print(my_short)