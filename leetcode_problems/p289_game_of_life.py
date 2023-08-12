# According to Wikipedia's article:
# "The Game of Life, also known simply as Life, is a cellular automaton devised
#   by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state:
#   live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
#   using the following four rules (taken from the above Wikipedia article):
#  -Any live cell with fewer than two live neighbors dies as if caused by under-population.
#  -Any live cell with two or three live neighbors lives on to the next generation.
#  -Any live cell with more than three live neighbors dies, as if by over-population.
#  -Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state,
#   where births and deaths occur simultaneously.
# Given the current state of the m x n grid board, return the next state.
# ------------------
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
from random import randint


def game_of_life(board: list[list[int]]) -> None:
    # working_sol (99.30%, 62.72%) -> (30ms, 16.4mb)  time: O(m * n) | space: O(1)
    # -10 -> dead in next, alive in current.
    # +10 -> alive in next, dead in current.
    height: int = len(board)
    row_length: int = len(board[0])
    for y in range(height):
        for x in range(row_length):
            # Count every live neighbour and decide ->
            count_alive: int = 0
            if 0 <= (x - 1):
                if board[y][x - 1] == 1 or board[y][x - 1] == -10:
                    count_alive += 1
            if row_length > (x + 1):
                if board[y][x + 1] == 1 or board[y][x + 1] == -10:
                    count_alive += 1
            if 0 <= (y - 1):
                if board[y - 1][x] == 1 or board[y - 1][x] == -10:
                    count_alive += 1
            if height > (y + 1):
                if board[y + 1][x] == 1 or board[y + 1][x] == -10:
                    count_alive += 1
            if 0 <= (x - 1) and 0 <= (y - 1):
                if board[y - 1][x - 1] == 1 or board[y - 1][x - 1] == -10:
                    count_alive += 1
            if row_length > (x + 1) and 0 <= (y - 1):
                if board[y - 1][x + 1] == 1 or board[y - 1][x + 1] == -10:
                    count_alive += 1
            if 0 <= (x - 1) and height > (y + 1):
                if board[y + 1][x - 1] == 1 or board[y + 1][x - 1] == -10:
                    count_alive += 1
            if row_length > (x + 1) and height > (y + 1):
                if board[y + 1][x + 1] == 1 or board[y + 1][x + 1] == -10:
                    count_alive += 1
            # -> options provided in description.
            # All of them depends on alive only, so there's no reason
            # to check anything then alive_neighbours.
            if count_alive < 2 and board[y][x] == 1:
                board[y][x] = -10
            elif 2 <= count_alive <= 3 and board[y][x] == 1:
                board[y][x] = 1
            elif 3 < count_alive and board[y][x] == 1:
                board[y][x] = -10
            elif 3 == count_alive and board[y][x] == 0:
                board[y][x] = 10
    # Setting the next_state.
    for y_ in range(height):
        for x_ in range(row_length):
            if board[y_][x_] == 10:
                board[y_][x_] = 1
            elif board[y_][x_] == -10:
                board[y_][x_] = 0


# Time complexity: O(m * n) -> options checked for the edge_rows(top and down) == 2 * (2 * 3 + (n - 2) * 5) ->
# n - row length of input_matrix^^| -> options checked for edge_columns(left and right) == 2 * (2 * 3 + (m - 2) * 5) ->
# m - height of input_matrix^^|-> every other indexes are checking options == 8, all 8 neighbours ->
#                              -> O(4 * ((2 * (2 * 3 + (n - 2) * 5) + (2 * (2 * 3 + (m - 2) * 5)) + (m * n - 4) * 8) ->
#                              -> 2 rows and 2 columns always having 5 options to choose for sizes more than 2,
#                              for 2 it's only 3 options for every index -> don't think there's even a reason to calc,
#                              like this.
#                              Because we're still doing 8 checks for every index, so it's => O(m * n * 8) ->
#                              -> and if we drop constant => O(m * n).
#                              Oh and extra we're traversing once again to change to the next state => O(m * n).
#                              But this is dominated by previous part anyway.
#                              W.e sticking to the O(m * n).
# Auxiliary space: O(1) -> only 3 constant INTs used => O(1).
# ------------------
# Store new state as some distinct value and reuse it?
# Like dead in next turn but alive in this == -10, alive in next turn but dead in this == +10.


test: list[list[int]] = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
test_out: list[list[int]] = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
game_of_life(test)
assert test_out == test

test = [[1, 1], [1, 0]]
test_out = [[1, 1], [1, 1]]
game_of_life(test)
assert test_out == test

test = [[randint(0, 1) for _ in range(25)] for _ in range(25)]
# print(test)
