# You have a 2-D grid of size m x n representing a box, and you have n balls.
# The box is open on the top and bottom sides.
# Each cell in the box has a diagonal board spanning two corners of the cell
#  that can redirect a ball to the right or to the left.
# A board that redirects the ball to the right spans the top-left corner
#  to the bottom-right corner and is represented in the grid as 1.
# A board that redirects the ball to the left spans the top-right corner
#  to the bottom-left corner and is represented in the grid as -1.
# We drop one ball at the top of each column of the box.
# Each ball can get stuck in the box or fall out of the bottom.
# A ball gets stuck if it hits a "V" shaped pattern between two boards
#  or if a board redirects the ball into either wall of the box.
# Return an array answer of size n where answer[i] is the column that the ball
#  falls out of at the bottom after dropping the ball from the ith column at the top,
#  or -1 if the ball gets stuck in the box.
# ----------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is 1 or -1.
from functools import cache

from random import choice

from pyperclip import copy


def find_ball(grid: list[list[int]]) -> list[int]:
    # working_sol (8.59%, 6.25%) -> (25ms, 22.32mb)  time: O(m * n) | space: O(n + m)
    # All we actually care, ball stuck or not?
    # And the ball is stuck, only when \/ -> neighbour column is an counterpart.
    # Otherwise, ball will fall through bottom.

    @cache
    def dfs(col: int, row: int) -> int:
        # Out of bounds == `\/` stuck.
        if not (0 <= col < len(grid[0])):
            return -1
        # We passed everything, and still in the boundaries.
        if len(grid) <= row:
            # We always pass `col + turn` previous column will be `col - turn`
            return col
        # -1 == left | 1 == right
        turn: int = grid[row][col]
        # We need the same: `\\` `//` otherwise we're stuck `\/`
        neighbour_col: int = col + turn
        # We hit the wall == `\/` stuck.
        if not (0 <= neighbour_col < len(grid[0])):
            return -1
        neighbour: int = grid[row][neighbour_col]
        if neighbour != turn:
            return -1

        return dfs(col + turn, row + 1)


    out: list[int] = [_ for _ in grid[0]]
    for column in range(len(grid[0])):
        out[column] = dfs(column, 0)
    
    return out


# Time complexity: O(m * n) <- m - length of the input array `grid`,
#                              n - height of the input array `grid`.
# We start from each cell of the first row of the `grid`.
# In the worst case, every ball will fall through == traverse every row => O(m * n).
# ----------------------
# Auxiliary space: O(n + m)
# `out` <- allocates space for each column of the `grid` => O(m).
# `dfs` <- stack of the recursion is at max of size `n` => O(n + m).


test: list[list[int]] = [
    [1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
    [-1, -1, -1, 1, 1],[1, 1, 1, 1, -1],[-1, -1, -1, -1, -1]
]
test_out: list[int] = [1, -1, -1, -1, -1]
assert test_out == find_ball(test)

test = [[-1]]
test_out = [-1]
assert test_out == find_ball(test)

test = [
    [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], 
    [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]
]
test_out = [0, 1, 2, 3, 4, -1]
assert test_out == find_ball(test)

test = [
    [choice([1, -1]) for _ in range(100)] for _ in range(100)
]
copy(test)
