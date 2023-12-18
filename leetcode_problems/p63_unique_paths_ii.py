# You are given an m x n integer array grid.
# There is a robot initially located in the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 10 ** 9.
# ----------------------
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
from random import randint


def unique_paths_with_obstacles(obstacleGrid: list[list[int]]) -> int:
    # working_sol (97.96%, 91.84%) -> (37ms, 16.21mb)  time: O(m * n) | space: O(1)
    # 1 == obstacle.
    # 0 == free path.
    # Initial cell or end point is blocked => we can't reach end point.
    if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
        return 0
    paths: int = 1
    # First row == 1 path to every cell.
    for col in range(len(obstacleGrid[0])):
        #  Or it's blocked == 0 paths.
        if obstacleGrid[0][col]:
            paths = 0
            obstacleGrid[0][col] = paths
        else:
            obstacleGrid[0][col] = paths
    # Same for the first column. But first cell is already set.
    paths = 1
    for row in range(1, len(obstacleGrid)):
        if obstacleGrid[row][0]:
            paths = 0
            obstacleGrid[row][0] = paths
        else:
            obstacleGrid[row][0] = paths
    # We can travel down or right => summarize every path options we have from these directions.
    for row in range(1, len(obstacleGrid)):
        for col in range(1, len(obstacleGrid[row])):
            # Blocked => 0 paths from this cell.
            if obstacleGrid[row][col]:
                obstacleGrid[row][col] = 0
            else:
                obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
    return obstacleGrid[-1][-1]


# Time complexity: O(m * n) <- m - number of rows in `obstacleGrid`, n - number of columns in `obstacleGrid`.
# Single traverse of the whole input matrix `obstacleGrid`.
# Auxiliary space: O(1).
# Only 1 extra constant INT used, doesn't depend on input.


test: list[list[int]] = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
test_out: int = 2
assert test_out == unique_paths_with_obstacles(test)

test = [[0, 1], [0, 0]]
test_out = 1
assert test_out == unique_paths_with_obstacles(test)

test = [[1], [0]]
test_out = 0
assert test_out == unique_paths_with_obstacles(test)

test = [[randint(0, 1) for _ in range(100)] for _ in range(100)]
print(test)
