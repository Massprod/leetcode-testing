# Given a m x n grid filled with non-negative numbers,
#  find a path from top left to bottom right,
#  which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# ------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
from random import randint


def min_path_sum(grid: list[list[int]], start_x: int = 0, start_y: int = 0) -> int:
    # working_sol (99.5%, 48.2%) -> (78ms, 18.1mb)  time: O(m * n) | space: O(1)
    # Update first row with travel costs to reach every cell.
    for col in range(1, len(grid[0])):
        grid[0][col] += grid[0][col - 1]
    # Update first column with travel costs to reach every cell.
    for row in range(1, len(grid)):
        grid[row][0] += grid[row - 1][0]
    # We can move only down or right => choose minimum travel cost from these directions.
    for row in range(1, len(grid)):
        for col in range(1, len(grid[row])):
            grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
    return grid[-1][-1]


# Time complexity: O(m * n) <- m - number of rows in `grid`, n - number of columns in `grid`.
# Single traverse of whole input matrix `grid`.
# Auxiliary space: O(1).
# Nothing extra, only using input matrix `grid`.


test: list[list[int]] = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
test_out: int = 7
assert test_out == min_path_sum(test)

test = [[1, 2, 3], [4, 5, 6]]
test_out = 12
assert test_out == min_path_sum(test)

test = [[randint(0, 100) for _ in range(200)] for _ in range(177)]
print(test)
