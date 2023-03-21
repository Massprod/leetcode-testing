import sys

import numpy
import math


def get_sq_matrix(row_length: int) -> list[list[str]]:
    sq_matrix = [["_"] * row_length for _ in range(row_length)]
    return sq_matrix


def set_queen_pos(y: int, x: int, sq_matrix: list[list[str]]) -> list[list[str]]:
    sq_matrix[y][x] = "Q"
    return sq_matrix


def read_queen_position(queen_matrix: list[list[str]]) -> tuple:
    for _ in queen_matrix:
        try:
            queen_x_pos = _.index("Q")
            queen_y_pos = queen_matrix.index(_)
            queen_pos = (queen_y_pos, queen_x_pos)
            return queen_pos
        except ValueError:
            pass


def count_queen_moves(queen_matrix: list[list[str]], queen_pos: tuple):
    y = queen_pos[0]
    x = queen_pos[1]
    moves = {"x": [],
             "y": [],
             "xy": [],
             }
    max_y = len(queen_matrix)
    max_x = len(queen_matrix[0])
    for _ in range(max_x):
        if _ != x:
            moves["x"].append((y, _))
    for _ in range(max_y):
        if _ != y:
            moves["y"].append((_, x))
    #  (x-1 , y-1) (x-1, y+1) (x+1, y-1) (x+1, y+1)
    while y > 0 and x > 0:
        y -= 1
        x -= 1
        move = (y, x)
        moves["xy"].append(move)
    y = queen_pos[0]
    x = queen_pos[1]
    while y > 0 and x < max_x - 1:
        x += 1
        y -= 1
        move = (y, x)
        moves["xy"].append(move)
    y = queen_pos[0]
    x = queen_pos[1]
    while x > 0 and y < max_y - 1:
        x -= 1
        y += 1
        move = (y, x)
        moves["xy"].append(move)
    y = queen_pos[0]
    x = queen_pos[1]
    while x < max_x - 1 and y < max_y - 1:
        x += 1
        y += 1
        move = (y, x)
        moves["xy"].append(move)
    return moves


def test_populate(moves: dict, sq_matrix: list[list[str]]) -> list[list[str]]:
    for _ in moves["x"]:
        sq_matrix[_[0]][_[1]] = "X"
    for _ in moves["y"]:
        sq_matrix[_[0]][_[1]] = "X"
    for _ in moves["xy"]:
        sq_matrix[_[0]][_[1]] = "X"
    return sq_matrix


matrix = get_sq_matrix(8)
set = set_queen_pos(3, 5, matrix)
queen_pos = read_queen_position(set)
available_moves = count_queen_moves(set, queen_pos)
populated = test_populate(available_moves, set)
print(numpy.matrix(populated))
