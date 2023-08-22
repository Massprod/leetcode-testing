# There is a robot on an m x n grid.
# The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths
#   that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 10 ** 9.
# ----------------------
# 1 <= m, n <= 100


def unique_paths(m: int, n: int) -> int:
    # working_sol (84.46%, 48.48%) -> (37ms, 16.3mb)  time: O(n * m) | space: O(n * m)
    matrix: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
    # Because we can move only from cell -> down | cell -> right.
    # Unique path -> first row, there's only 1 way to get to any cell.
    for _ in range(n):
        matrix[0][_] = 1
    # Unique path -> first column, only 1 way to get to these cells.
    for _ in range(m):
        matrix[_][0] = 1
    # Every other cell paths is sum of Top & Left cells.
    # Cells from which we can move correctly.
    for y in range(1, m):
        for x in range(1, n):
            matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]
    return matrix[-1][-1]


# Time complexity: O(m * n) -> nested_loop to create matrix of m * n size O(m * n) ->
# m - height of matrix^^|  -> two loops to populate unique row O(n), column O(m) ->
# n - length of matrix^^|  -> nested_loop to populate empty cells O((m - 1) * (n - 1)) => O(m * n).
# Space complexity: O(m * n) -> creating matrix with height of input_m and length of input_n => O(m * n).
# ----------------------
# Already met something familiar with p64, and solved it with semi_googled solution.
# So if I recall correctly, there's rule that every possible path we can encounter on one_index,
#  is equal to a summ of all num_of_paths from possible ways to enter it.
# We only allowed to go like this: top -> bottom, left -> right,
#  so we can calc num_of_paths on any cell just with summing top and left cells value of their num_of_paths.
# There's unique row and column with only num_of_paths to enter any index on them equal to 1.
# First row -> to enter any index on this row we can use only one path -> from left to right.
# First column -> to enter any index on this column we can use only one path -> from top to bottom.


test_m: int = 3
test_n: int = 7
test_out: int = 28
assert test_out == unique_paths(test_m, test_n)

test_m = 3
test_n = 2
test_out = 3
assert test_out == unique_paths(test_m, test_n)
