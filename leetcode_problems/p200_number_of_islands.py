# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
#  return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
# ---------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
from collections import deque
from random import choice


def num_of_islands(grid: list[list[str]]) -> int:
    # working_sol (99.68%, 88.1%) -> (242ms, 18.78mb)  time: O(m * n) | space: O(log(m * n))
    # Standard BFS approach.
    que: deque[tuple[int, int]] = deque()
    row_len: int = len(grid[0])
    col_len: int = len(grid)
    islands: int = 0
    # Check all cells.
    for y in range(col_len):
        for x in range(row_len):
            if grid[y][x] == '1':
                que.append((y, x))
                grid[y][x] = '3'
                while que:
                    cell: tuple[int, int] = que.popleft()
                    col: int = cell[0]
                    row: int = cell[1]
                    # If cell coordinate is correct and cell is not visited => check it.
                    if 0 <= col - 1 < col_len and grid[col - 1][row] == '1':
                        que.append((col - 1, row))
                        grid[col - 1][row] = '3'
                    if 0 <= col + 1 < col_len and grid[col + 1][row] == '1':
                        que.append((col + 1, row))
                        grid[col + 1][row] = '3'
                    if 0 <= row - 1 < row_len and grid[col][row - 1] == '1':
                        que.append((col, row - 1))
                        grid[col][row - 1] = '3'
                    if 0 <= row + 1 < row_len and grid[col][row + 1] == '1':
                        que.append((col, row + 1))
                        grid[col][row + 1] = '3'
                islands += 1
    return islands


# Time complexity: O(m * n) -> worst case, every cell in matrix is '1' -> traversing whole matrix once => O(m * n).
# m - height of input_matrix^^| Actually no matter the case, we're still traversing whole matrix, once.
# n - length of input_matrix^^|
# Auxiliary space: O(log(m * n)) -> doing BFS on every cell with '1', for every cell check we will
#                              add 4 neighbours at max, and because we're removing them to check later ->
#                              -> our que will have only part of the matrix, so it should be correct => O(log(m * n)).
# ---------------------
# BFS with changing of '1's to any other to skip later? Yep, correctly working.


test: list[list[str]] = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
test_out: int = 1
assert test_out == num_of_islands(test)

test = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
test_out = 3
assert test_out == num_of_islands(test)

test = [[choice(['1', '0']) for _ in range(300)] for _ in range(300)]
print(test)
