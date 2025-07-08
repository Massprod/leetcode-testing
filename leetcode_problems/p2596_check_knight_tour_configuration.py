# There is a knight on an n x n chessboard.
# In a valid configuration, the knight starts at the top-left cell
#  of the board and visits every cell on the board exactly once.
# You are given an n x n integer matrix grid consisting of distinct integers
#  from the range [0, n * n - 1] where grid[row][col] indicates that the cell
#  (row, col) is the grid[row][col]th cell that the knight visited.
# The moves are 0-indexed.
# Return true if grid represents a valid configuration
#  of the knight's movements or false otherwise.
# Note that a valid knight move consists of moving two squares vertically
#  and one square horizontally, or two squares horizontally and one square vertically.
# The figure below illustrates all the possible eight moves of a knight from some cell.
# ----------------------------
# n == grid.length == grid[i].length
# 3 <= n <= 7
# 0 <= grid[row][col] < n * n
# All integers in grid are unique.
from functools import cache


def check_valid_grid(grid: list[list[int]]) -> bool:
    # working_sol (6.80%, 8.25%) -> (11ms, 18.06mb)  time: O(n ** 2) | space: O(n ** 2)
    # [ (dy, dx) ] <- 
    # <- [ topLeft, topRight, rightTop, rightBot, botRight, botLeft, leftBot, leftTop ]
    moves: list[tuple[int, int]] = [
        (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)
    ]
    # We count every correct spot we visit.
    visited: list[list[int]] = [
        [0 for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]

    @cache
    def dfs(row: int, col: int, step: int) -> None:
        nonlocal visited, grid
        
        if grid[row][col] == step:
            visited[row][col] = 1
        else:
            return

        for dy, dx in moves:
            new_row: int = row + dy
            new_col: int = col + dx
            if (not (0 <= new_row < len(grid))
                or not (0 <= new_col < len(grid[0]))):
                continue
            dfs(new_row, new_col, step + 1)


    dfs(0, 0, 0)

    return all([all(row) for row in visited])


# Time complexity: O(n ** 2) <- n - length of the input array `grid`.
# In the worst case, we will check every cell knight visits.
# And he visits every cell of the chessboard => O(n ** 2).
# ----------------------------
# Auxiliary space: O(n ** 2)
# Recursion stack is at max of `n ** 2` depth => O(n ** 2).


test: list[list[int]] = [
    [0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6],
    [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]
]
test_out: bool = True
assert test_out == check_valid_grid(test)

test = [[0, 3, 6], [5, 8, 1], [2, 7, 4]]
test_out = False
assert test_out == check_valid_grid(test)
