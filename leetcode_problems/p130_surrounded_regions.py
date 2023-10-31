# Given an m x n matrix board containing 'X' and 'O', capture all regions
#  that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# ------------------
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'
from collections import deque


def solve(board: list[list[str]]) -> None:
    # working_sol (22.36%, 15.83%) -> (153ms, 24.4mb)  time: O(m * n) | space: O(m * n)
    visited: set[tuple[int, int]] = set()
    to_flip: list[tuple[int, int]] = []
    # Essentially, all we care is if we hit border or not.
    # Otherwise, it's surrounded region.
    y_limits: set[int] = {0, len(board) - 1}
    x_limits: set[int] = {0, len(board[0]) - 1}
    max_y: int = len(board) - 1
    max_x: int = len(board[0]) - 1
    for y in range(len(board)):
        for x in range(len(board[0])):
            # Standard BFS from any 'O' we're not yet visited.
            if (y, x) not in visited and board[y][x] == 'O':
                que: deque[tuple[int, int]] = deque([(y, x)])
                region: list[tuple[int, int]] = [(y, x)]
                flipping: bool = True
                while que:
                    cell: tuple[int, int] = que.popleft()
                    region.append(cell)
                    _y: int = cell[0]
                    _x: int = cell[1]
                    # Border hit == not flipping, but still need to mark other 'O's of the region
                    #  as visited to skip later.
                    if flipping and (_y in y_limits or _x in x_limits):
                        flipping = False
                    if 0 <= (_y - 1) and (_y - 1, _x) not in visited and board[_y - 1][_x] == 'O':
                        que.append((_y - 1, _x))
                        visited.add((_y - 1, _x))
                    if max_y >= (_y + 1) and (_y + 1, _x) not in visited and board[_y + 1][_x] == 'O':
                        que.append((_y + 1, _x))
                        visited.add((_y + 1, _x))
                    if 0 <= (_x - 1) and (_y, _x - 1) not in visited and board[_y][_x - 1] == 'O':
                        que.append((_y, _x - 1))
                        visited.add((_y, _x - 1))
                    if max_x >= (_x + 1) and (_y, _x + 1) not in visited and board[_y][_x + 1] == 'O':
                        que.append((_y, _x + 1))
                        visited.add((_y, _x + 1))
                if flipping:
                    to_flip = to_flip + region
    for y, x in to_flip:
        board[y][x] = 'X'


# Time complexity: O(m * n) -> see 2 worst cases:
# m - height of input matrix 'board'^^| First: whole board is 'O' -> then we will check every cell => O(m * n).
# n - length of input matrix 'board'^^| Second: only borders are 'x' -> we will visit ((m - 2) * (n - 2)) cells,
#                                               and extra traverse to flip them => O(2 * ((m - 2) * (n - 2)).
#                             Still Linear, so it should be correct to say => O(m * n).
# Auxiliary space: O(m * n) -> second worst case -> set 'visited' will have ((m - 2) * (n - 2)) cells ->
#                              -> 'que' with the same size and 'to_flip' with the same size => O(3 * (m * n)).


test: list[list[str]] = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
test_out: list[list[str]] = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
solve(test)
assert test_out == test

test = [["X"]]
test_out = [["X"]]
solve(test)
assert test_out == test

test = [["O"]]
test_out = [["O"]]
solve(test)
assert test_out == test

test = [
    ["O", "O", "X", "O", "O", "O"],
    ["X", "O", "O", "O", "O", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "O", "O", "O", "X", "X"],
    ["X", "X", "X", "O", "O", "X"],
    ["X", "O", "O", "O", "X", "O"],
    ["O", "X", "X", "X", "O", "O"],
]
test_out = [
    ['O', 'O', 'X', 'O', 'O', 'O'],
    ['X', 'O', 'O', 'O', 'O', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'X', 'X', 'O', 'O'],
]
solve(test)
assert test_out == test

test = [
    ["O", "X", "X", "O", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"],
]
test_out = [
    ['O', 'X', 'X', 'O', 'X'],
    ['X', 'X', 'X', 'X', 'O'],
    ['X', 'X', 'X', 'O', 'X'],
    ['O', 'X', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'X', 'O'],
]
solve(test)
assert test_out == test
