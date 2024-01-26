# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
# You are allowed to move the ball to one of the four adjacent cells in the grid
#  (possibly out of the grid crossing the grid boundary).
# You can apply at most maxMove moves to the ball.
# Given the five integers m, n, maxMove, startRow, startColumn,
#  return the number of paths to move the ball out of the grid boundary.
# Since the answer can be very large, return it modulo 10 ** 9 + 7.
# ---------------------
# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n
from functools import cache


def find_paths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    # working_sol (99.13%, 41.33%) -> (63ms, 22.23mb)  time: O(m * n * moves) | space: O(m * n * moves)
    # [(dy, dx)], y - row, x - column.
    # [top, right, bot, left]
    options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # (max row-index, max column-index)
    limits: tuple[int, int] = (m - 1, n - 1)

    @cache
    def dfs(row: int, col: int, moves: int) -> int:
        if not 0 <= row < m or not 0 <= col < n:
            return 1
        out: int = 0
        # We don't need to try if we already don't have enough moves to cross any border.
        # (row - 0) == moves we need to reach cell on top border, but not cross it.
        # (max column-index - current column) == moves we need to reach cell on right border.
        # (max row-index - current row) == moves we need to reach cell on bottom border.
        # (column - 0) == moves we need to reach cell on left border.
        # But we need extra move to cross it.
        if not moves > row and not moves > (limits[1] - col) and not moves > (limits[0] - row) and not moves > col:
            return 0
        for dy, dx in options:
            out += dfs(row + dy, col + dx, moves - 1)
        return out

    return dfs(startRow, startColumn, maxMove) % (10 ** 9 + 7)


# Time complexity: O(m * n * moves).
# Because we're using @cache on every cell we can reach, we can have all cells visited and all of them
#  will have different moves left to use.
# So, we're going to have (m * n * moves) states to memorise and calculate => O(m * n * moves).
# ---------------------
# Auxiliary space: O(m * n * moves).
# We're caching every state => O(m * n * moves).


test_m: int = 2
test_n: int = 2
test_maxMoves: int = 2
test_startRow: int = 0
test_startColumn: int = 0
test_out: int = 6
assert test_out == find_paths(test_m, test_n, test_maxMoves, test_startRow, test_startColumn)

test_m = 1
test_n = 3
test_maxMoves = 3
test_startRow = 0
test_startColumn = 1
test_out = 12
assert test_out == find_paths(test_m, test_n, test_maxMoves, test_startRow, test_startColumn)
