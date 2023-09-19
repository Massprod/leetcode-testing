# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
# If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
#  to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#   - All the visited cells of the path are 0.
#   - All the adjacent cells of the path are 8-directionally connected
#     (i.e., they are different, and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
# ------------------
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
from collections import deque


def shortest_path_bm(grid: list[list[int]]) -> int:
    # working_sol (94.97%, 97.86%) -> (462ms, 16.5mb)  time: O(n * n) | space: O(n * n)
    row_len: int = len(grid[0])
    col_len: int = len(grid)
    # Start and end already taken by '1' no correct path.
    if grid[0][0] or grid[row_len - 1][col_len - 1]:
        return -1
    path: int = 1
    # Unique case.
    if row_len == 1 and col_len == 1:
        return path
    # Standard BFS with delimiter.
    # (row, col) <- coordinates of the cell.
    que: deque[tuple[int, int] | None] = deque([(0, 0), None])
    # Any mark, except 0.
    mark: int = 3
    grid[0][0] = mark
    # All 8 directions to shift cell coordinates.
    shifts: list[tuple[int, int]] = [
        (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
    ]
    while que:
        cur_cell: tuple[int, int] | None = que.popleft()
        # Hit delimiter == all cells in all 8 directions processed.
        # So, we made 1 step on the path.
        if cur_cell is None:
            if que:
                que.append(None)
            path += 1
            continue
        for row_shift, col_shift in shifts:
            s_row: int = row_shift + cur_cell[0]
            s_col: int = col_shift + cur_cell[1]
            if 0 <= s_row < row_len and 0 <= s_col < col_len:
                if not grid[s_row][s_col]:
                    # Better to break when last cell added.
                    # Then we don't need to check what's left in a que.
                    # There's 3 neighbours for last cell in the worst case, we need only 1.
                    if (s_row == row_len - 1) and (s_col == col_len - 1):
                        path += 1
                        return path
                    que.append((s_row, s_col))
                    grid[s_row][s_col] = mark
    return -1


# Time complexity: O(n * n) -> worst case == all cells checked => O(n * n).
# Auxiliary space: O(n * n) -> all cells added into que => O(n * n).
# ------------------
# BFS with delimiter, but with 8 options not just 4 neighboring?
# Should be correct.


test: list[list[int]] = [[0, 1], [1, 0]]
test_out: int = 2
assert test_out == shortest_path_bm(test)

test = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
test_out = 4
assert test_out == shortest_path_bm(test)

test = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
test_out = -1
assert test_out == shortest_path_bm(test)

test = [[0]]
test_out = 1
assert test_out == shortest_path_bm(test)
