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
            _[x] = randint(1, 30)
    return matrix


def short_path(matrix: list[list[int]]) -> int:
    max_y = len(matrix)
    max_x = len(matrix[0])
    # sum horizontal
    for x in range(1, max_x):
        matrix[0][x] = matrix[0][x] + matrix[0][x - 1]
    # sum vertical
    for y in range(1, max_y):
        matrix[y][0] = matrix[y][0] + matrix[y - 1][0]
    # sum empty
    for y in range(1, max_y):
        for x in range(1, max_x):
            vert = matrix[y - 1][x]
            horiz = matrix[y][x - 1]
            matrix[y][x] = min(vert, horiz) + matrix[y][x]
    print(numpy.matrix(matrix))
    return matrix[max_y - 1][max_x - 1]


original = create_matrix(height=3, length=7)
print(numpy.matrix(original))
copy = copy.deepcopy(original)
my_short = short_path(original)
print(my_short)
