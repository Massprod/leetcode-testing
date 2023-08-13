# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
#       maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered
#       around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
# Return the generated matrix.
# ---------------------
# n == grid.length == grid[i].length
# 3 <= n <= 100
# 1 <= grid[i][j] <= 100
from random import randint


def largest_local(grid: list[list[int]]) -> list[list[int]]:
    # working_sol (99.52%, 69.63%) -> (117ms, 16.9mb)  time: O((m - 2) * (n - 2)) | space: O((m - 2) * (n - 2))
    length: int = len(grid) - 2
    # ^^Size == ! matrix maxLocal of size (n - 2) x (n - 2) !
    largest: list[list[int]] = [[0 for _ in range(length)] for _ in range(length)]
    for y in range(length):
        for x in range(length):
            # ! largest value of the 3 x 3 matrix in grid centered
            #   around row i + 1 and column j + 1. !
            largest[y][x] = max(
                # First column:
                grid[y][x], grid[y + 1][x], grid[y + 2][x],
                # Second column:
                grid[y][x + 1], grid[y + 1][x + 1], grid[y + 2][x + 1],
                # Third column:
                grid[y][x + 2], grid[y + 1][x + 2], grid[y + 2][x + 2],
            )
    return largest


# Time complexity: O((m - 2) * (n - 2)) -> we're given ideal matrix, so it's always 9 checks for every index =>
# m - row length of input_matrix^^| => O((m - 2) * (n - 2) * 9) -> constant actions for every index, we can cull it =>
# n - height of input_matrix^^|     => O((m - 2) * (n - 2)).
# Auxiliary space: O((m - 2) * (n - 2)) -> matrix of (m - 2) row and (n - 2) height used to store max_locals.


test: list[list[int]] = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
test_out: list[list[int]] = [[9, 9], [8, 6]]
assert test_out == largest_local(test)

test = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
test_out = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
assert test_out == largest_local(test)

test = [[randint(1, 100) for _ in range(100)] for _ in range(100)]
# print(test)
