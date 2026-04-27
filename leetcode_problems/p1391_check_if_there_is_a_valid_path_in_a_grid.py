# You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:
# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.
# You will initially start at the street of the upper-left cell (0, 0).
# A valid path in the grid is a path that starts from the upper left cell (0, 0)
#  and ends at the bottom-right cell (m - 1, n - 1).
# The path should only follow the streets.
# Notice that you are not allowed to change any street.
# Return true if there is a valid path in the grid or false otherwise.
# --- --- --- ---
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# 1 <= grid[i][j] <= 6
from collections import deque


def has_valid_path(grid: list[list[int]]) -> bool:
    # working_solution: (75.75%, 61.57%) -> (179ms, 35.57mb)  Time: O(n * m) Space: O(n * m)
    # [ top), (right), (bot), (left) ] <- dy, dx
    directions: list[tuple[int, int]] = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]
    # { road_type: {str : {available directions} } }
    roads: dict[int, dict[str, set[int]]] = {
        1: {
            'in': {3, 1},
            'out': {1, 3},
        },
        2: {
            'in': {0, 2},
            'out': {0, 2},
        },
        3: {
            'in': {1, 0},
            'out': {3, 2},
        },
        4: {
            'in': {0, 3},
            'out': {2, 1},
        },
        5: {
            'in': {1, 2},
            'out': {3, 0},
        },
        6: {
            'in': {2, 3},
            'out': {0, 1},
        },
    }
    # (y, x)
    target: tuple[int, int] = (len(grid) - 1, len(grid[0]) - 1)
    limit_y: int = len(grid)
    limit_x: int = len(grid[0])
    # [ (y, x) ]
    que: deque[tuple[int, int]] = deque([(0, 0)])
    visited: set[tuple[int, int]] = {(0, 0)}
    while que:
        cell = que.popleft()
        if cell == target:
            return True
        y, x = cell
        cur_road: int = grid[y][x]
        for direction in roads[cur_road]['out']:
            # Check if we can move at all.
            dy, dx = directions[direction]
            new_y, new_x = y + dy, x + dx
            if (
                (new_y, new_x) in visited
                or not (0 <= new_y < limit_y)
                or not (0 <= new_x < limit_x)
            ):
                continue
            # Check if we can enter the next cell.
            new_road: int = grid[new_y][new_x]
            # We can't enter into the cell.
            if direction not in roads[new_road]['in']:
                continue
            new_cell: tuple[int, int] = (new_y, new_x)
            # Every cell has 1 entrance and 1 exit.
            # So, we can mark it visited imediately.
            visited.add(new_cell)
            que.append(new_cell)

    return False


# Time complexity: O(n * m)
# n - length of the input matrix `grid`
# m - height of the input matrix `grid`
# ---
# Standard BFS traversal of the whole matrix, once => O(n * m).
# --- --- --- ---
# Space complexity: O(n * m)
# `visited` <- allocates space for each visited cell => O(n * m).


test: list[list[int]] = [[2, 4, 3], [6, 5, 2]]
test_out: bool = True
assert test_out == has_valid_path(test)

test = [[1, 2, 1], [1, 2, 1]]
test_out = False
assert test_out == has_valid_path(test)

test = [[1, 1, 2]]
test_out = False
assert test_out == has_valid_path(test)
