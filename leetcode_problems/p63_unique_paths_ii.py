# You are given an m x n integer array grid.
# There is a robot initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
# m == obstacleGrid.length  ,  n == obstacleGrid[i].length
# 1 <= m, n <= 100  ,  obstacleGrid[i][j] is 0 or 1.

def unique_paths_obstacles(obstacleGrid: list[list[int]]) -> int:
    # working_sol (5.30%, 11.2%) -> (68ms, 16.4mb)  time: O(
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
        return 0
    length: int = len(obstacleGrid[0])
    height: int = len(obstacleGrid)
    limit_row: int = 1
    for _ in range(length):
        if obstacleGrid[0][_] == 1:
            limit_row = 0
            obstacleGrid[0][_] = limit_row
        obstacleGrid[0][_] = limit_row
    limit_column: int = 1
    for _ in range(1, height):
        if obstacleGrid[_][0] == 1:
            limit_column = 0
            obstacleGrid[_][0] = limit_column
        obstacleGrid[_][0] = limit_column
    for y in range(1, height):
        for x in range(1, length):
            if obstacleGrid[y][x] == 1:
                obstacleGrid[y][x] = 0
                continue
            obstacleGrid[y][x] = obstacleGrid[y - 1][x] + obstacleGrid[y][x - 1]
    return obstacleGrid[-1][-1]


# Time complexity: O(n * m) -> looping once through whole input of m * n size -> first_row_loop => O(m) ->
# n - height, m - length ^^    -> first_column_loop => O(n)
#                              -> nested loop for 1 <= y <= (n - 1), 1 <= x <= (m - 1)
#                                 depends on input matrix size (n * m) => O(n * m)
# Space complexity: O(1) -> only 4 extra constants: length, height, limit_row, limit_column => O(1)

# Same approach but, if we along the way encounter obstacle we're making this cell unapproachable by giving value of 0.
# Which is 0 path to enter this cell, and we can summ num_of_paths like before.
# ------------------------------
# Mirror of p62, but we need to skip some index_cells with already placed value == 1.


test1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
test1_out = 2
test = unique_paths_obstacles(test1)
print(test)
assert test == test1_out
del test

test2 = [[0, 1], [0, 0]]
test2_out = 1
test = unique_paths_obstacles(test2)
print(test)
assert test == test2_out
del test

test3 = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
test3_out = 0
test = unique_paths_obstacles(test3)
print(test)
assert test == test3_out
del test

# test4 - failed -> considered that [0][0] can be obstacle, but forgot about [-1][-1] can be obstacle as well...
test4 = [
    [0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1],
    [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [0],
    [0], [0], [1], [1], [0], [1], [0], [0], [1], [0], [0], [0], [0],
    [1],
]
test4_out = 0
test = unique_paths_obstacles(test4)
print(test)
assert test == test4_out
del test

# test5 - failed -> I made loop for first row and column breaking when we encounter obstacle.
#                   But didn't consider if there's more than 1 obstacle,
#                   and we need to null all the row, column after first obstacle.
test5 = [
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0],
    [0, 0], [0, 0],
]
test5_out = 0
test = unique_paths_obstacles(test5)
print(test)
assert test == test5_out
del test
