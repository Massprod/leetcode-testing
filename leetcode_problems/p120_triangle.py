# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row,
#  you may move to either index i or index i + 1 on the next row.
# -------------------
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10 ** 4 <= triangle[i][j] <= 10 ** 4
# -------------------
# Follow up: Could you do this using only O(n) extra space,
#  where n is the total number of rows in the triangle?
from random import randint


def minimum_total(triangle: list[list[int]]) -> int:
    # working_sol (90.85%, 60.98%) -> (61ms, 17.32mb)  time: O((m - 1) * n) | space: O(1)
    # Bottom-up solution.
    # Start from preLast row and choose best option to step for every column(index).
    # And we can only have 2-step options: col -> col | col -> col + 1
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]


# Time complexity: O((m - 1) * n) <- m - number of rows in `triangle`, n - average length of rows in `triangle`.
# We always check every cell in `triangle` except last row.
# And for every cell we check 2-step options.
# O((m - 1) * n *  2), and because we're always checking 2 options we can call it constant and cull.
# Auxiliary space: O(1).


test: list[list[int]] = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
test_out: int = 11
assert test_out == minimum_total(test)

test = [[-10]]
test_out = -10
assert test_out == minimum_total(test)

test = [[randint(-10 ** 4, 10 ** 4) for _ in range(row)] for row in range(1, 201)]
print(test)
