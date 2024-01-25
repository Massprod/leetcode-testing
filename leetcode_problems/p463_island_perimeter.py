# You are given row x col grid representing a map where grid[i][j] = 1 represents land
#  and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water,
#  and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water
#  around the island.
# One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.
# -------------------------
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
from collections import deque


def island_perimeter(grid: list[list[int]]) -> int:
    # working_sol (62.30%, 71.09%) -> (416ms, 17.00mb)  time: O(m * n) | space: O(m * n)
    # [(dy, dx)]
    options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def bfs(row: int, col: int) -> int:
        que: deque[tuple[int, int]] = deque([(row, col)])
        grid[row][col] = 2  # mark of visited cells.
        out: int = 0
        while que:
            row, col = que.popleft()
            for dy, dx in options:
                step_row: int = row + dy
                step_col: int = col + dx
                # Land we can travel to.
                if 0 <= step_row < len(grid) and 0 <= step_col < len(grid[0]) and grid[step_row][step_col]:
                    if 2 == grid[step_row][step_col]:
                        continue
                    que.append((step_row, step_col))
                    grid[step_row][step_col] = 2
                # Water or grid border.
                else:
                    out += 1
        return out

    for row_ in range(len(grid)):
        for col_ in range(len(grid[row_])):
            if grid[row_][col_]:
                return bfs(row_, col_)


# Time complexity: O(m * n) <- m - number of rows in `grid`, n - number of columns in `grid`.
# Worst case: whole input `grid` is island, all cells == '1'.
# We will traverse whole matrix with BFS => O(m * n).
# -------------------------
# Auxiliary space: O(m * n).
# Standard BFS and we can allocate every cell in `que` => O(m * n).


test: list[list[int]] = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
test_out: int = 16
assert test_out == island_perimeter(test)

test = [[1]]
test_out = 4
assert test_out == island_perimeter(test)

test = [[1, 0]]
test_out = 4
assert test_out == island_perimeter(test)
