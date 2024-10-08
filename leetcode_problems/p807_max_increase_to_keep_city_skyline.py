# There is a city composed of n x n blocks,
#  where each block contains a single building shaped like a vertical square prism.
# You are given a 0-indexed n x n integer matrix grid where grid[r][c]
#  represents the height of the building located in the block at row r and column c.
# A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance.
# The skyline from each cardinal direction north, east, south, and west may be different.
# We are allowed to increase the height of any number of buildings by any amount
#  (the amount can be different per building).
# The height of a 0-height building can also be increased.
# However, increasing the height of a building should not affect the city's skyline from any cardinal direction.
# Return the maximum total sum that the height of the buildings can be increased by
#  without changing the city's skyline from any cardinal direction.
# -------------------------
# n == grid.length
# n == grid[r].length
# 2 <= n <= 50
# 0 <= grid[r][c] <= 100
from random import randint
from collections import defaultdict


def max_increase_keeping_skyline(grid: list[list[int]]) -> int:
    # working_sol (45.12%, 40.99%) -> (68ms, 16.66mb)  time: O(n * n) | space: O(n)
    # { row: max_value of this row }
    row_maxs: dict[int, int] = defaultdict(int)
    # { col: max_value of this column}
    col_maxs: dict[int, int] = defaultdict(int)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            row_maxs[row] = max(grid[row][col], row_maxs[row])
            col_maxs[col] = max(grid[row][col], col_maxs[col])
    out: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            out += min(row_maxs[row], col_maxs[col]) - grid[row][col]
    return out


# Time complexity: O(n * n) <- n - length | height of the input matrix `grid`.
# Always traversing all the input matrix `grid` cells, twice => O(n * n).
# -------------------------
# Auxiliary space: O(n)
# `row_maxs` <- allocates space for all rows of the `grid` => O(n).
# `col_maxs` <- allocates space for all columns of the `grid` => O(n + n).


test: list[list[int]] = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
test_out: int = 35
assert test_out == max_increase_keeping_skyline(test)

test = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
test_out = 0
assert test_out == max_increase_keeping_skyline(test)

test = [[randint(0, 100) for _ in range(50)] for _ in range(50)]
print(test)
