# Given an m x n matrix board containing 'X' and 'O', capture all regions
#   that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# m == board.length  ,  n == board[i].length
# 1 <= m, n <= 200  ,  board[i][j] is 'X' or 'O'.


def solve(board: list[list[str]]) -> None:
    pass


test1 = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
test1_out = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

test2 = [["X"]]
test2_out = [["X"]]

test3 = [["O"]]
test3_out = [["O"]]
