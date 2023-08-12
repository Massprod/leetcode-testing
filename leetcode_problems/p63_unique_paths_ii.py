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
# ------------------------------
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.


def unique_paths_obstacles(obstacleGrid: list[list[int]]) -> int:
    # working_sol (99.30%, 97.56%) -> (38ms, 16.28mb)  time: O(n * m) | space: O(1)
    # Start or End points blocked. We can't start moving,
    # and we can't come into correct end_point at all.
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
        return 0
    # Row length.
    length: int = len(obstacleGrid[0])
    # Height length.
    height: int = len(obstacleGrid)
    # There's only 1 way to go through first row ->
    limit_row: int = 1
    for _ in range(length):
        # -> but if it's blocked, we can't move to the next indexes
        #    in this row.
        if obstacleGrid[0][_] == 1:
            # 0 Ways starts from this point.
            limit_row = 0
        obstacleGrid[0][_] = limit_row
    # Same goes for column ->
    limit_column: int = 1
    for _ in range(1, height):
        # -> if path is blocked, we can't move to the next indexes
        #    in the column.
        if obstacleGrid[_][0] == 1:
            limit_column = 0
        obstacleGrid[_][0] = limit_column
    # We can reach any point [y][x] by summarizing
    # [y - 1][x] <- vertical paths.
    # [y][x - 1] <- horizontal paths.
    for y in range(1, height):
        for x in range(1, length):
            # First row and column skipped, so if we ever met any point with value == 1.
            # It's blocked point, and we can't start moving from it == 0 paths started.
            if obstacleGrid[y][x] == 1:
                obstacleGrid[y][x] = 0
                continue
            obstacleGrid[y][x] = obstacleGrid[y - 1][x] + obstacleGrid[y][x - 1]
    # All paths summarized.
    return obstacleGrid[-1][-1]


# Time complexity: O(n * m) -> looping once through whole input of m * n size -> first_row_loop => O(m) ->
# n - height of input_matrix^^|  -> first_column_loop => O(n) ->
# m - length of input_matrix^^|  -> nested loop for 1 <= y <= (n - 1), 1 <= x <= (m - 1)
#                                depends on input matrix size (n * m) => O(n * m).
# Space complexity: O(1) -> only 4 extra constant INTs used, none depends on input => O(1).
# ------------------------------
# Same approach but, if we encounter obstacle along the way we're making this cell unapproachable by giving value of 0.
# Which is 0 path to enter this cell, and we can summ num_of_paths like before.
# ------------------------------
# Mirror of p62, but we need to skip some index_cells with already placed value == 1.


test: list[list[int]] = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
test_out: int = 2
test_result: int = unique_paths_obstacles(test)
assert test_out == test_result

test = [[0, 1], [0, 0]]
test_out = 1
test_result = unique_paths_obstacles(test)
assert test_out == test_result

test = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
test_out = 0
test_result = unique_paths_obstacles(test)
assert test_out == test_result

# test4 - failed -> considered that [0][0] can be obstacle, but forgot about [-1][-1] being obstacle as well...
test = [
    [0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1],
    [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [0],
    [0], [0], [1], [1], [0], [1], [0], [0], [1], [0], [0], [0], [0],
    [1],
]
test_out = 0
test_result = unique_paths_obstacles(test)
assert test_out == test_result

# test5 - failed -> I made loop for first row and column breaking when we encounter obstacle.
#                   But didn't consider if there's more than 1 obstacle,
#                   and we need to null all the row, column after first obstacle.
test = [
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0],
    [0, 0], [0, 0],
]
test_out = 0
test_result = unique_paths_obstacles(test)
assert test_out == test_result
