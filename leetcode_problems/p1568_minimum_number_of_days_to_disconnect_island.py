# You are given an m x n binary grid grid where 1 represents land and 0 represents water.
# An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
# In one day, we are allowed to change any single land cell (1) into a water cell (0).
# Return the minimum number of days to disconnect the grid.
# -------------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either 0 or 1.
from collections import deque


def min_days(grid: list[list[int]]) -> int:
    # working_sol (54.21%, 82.24%) -> (744ms, 16.66mb)  time: O((n * m) ** 2) | space: O(n * m)

    def count_islands() -> int:
        cell_row: int
        cell_col: int
        # Standard BFS from every cell we can start an island.
        islands = 0
        visited: set[tuple[int, int]] = set()
        for _row in range(len(grid)):
            for _col in range(len(grid[0])):
                if 1 == grid[_row][_col] and (_row, _col) not in visited:
                    # [(dy, dx)]
                    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    que: deque[tuple[int, int]] = deque([(_row, _col)])
                    while que:
                        cell_row, cell_col = que.popleft()
                        for dy, dx in directions:
                            new_row: int = cell_row + dy
                            new_col: int = cell_col + dx
                            if ((new_row, new_col) not in visited
                                    and 0 <= new_row < len(grid)
                                    and 0 <= new_col < len(grid[0])
                                    and 1 == grid[new_row][new_col]):
                                que.append((new_row, new_col))
                                visited.add((new_row, new_col))
                    islands += 1
        return islands

    if 1 < count_islands():
        return 0
    # If there are 0 `1`s cells or `1` cell, we need to cover it.
    one_cells: int = 0
    # Remove cell from island, and check how many there's after it.
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 1 == grid[row][col]:
                one_cells += 1
                grid[row][col] = 0
                if 1 < count_islands():
                    return 1
                grid[row][col] = 1
    if 2 > one_cells:
        return one_cells
    return 2


# Time complexity: O((n * m) ** 2) <- n - height of the input array `grid`, m - length of the input array `grid`.
# In the worst case, we're going to have every cell with `1`.
# From every cell we will traverse the whole `grid` to count islands => O((m * n) * (m * n)).
# -------------------------
# Auxiliary space: O(n * m)
# In the worst case every cell is `1`s.
# `visited` <- will allocate space for each cell we visit => O(n * m)
# `que` <- will allocate space for each cell we use => O(n * m + n * m).


test: list[list[int]] = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
test_out: int = 2
assert test_out == min_days(test)

test = [[1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
test_out = 1
assert test_out == min_days(test)

test = [[1, 1]]
test_out = 2
assert test_out == min_days(test)
