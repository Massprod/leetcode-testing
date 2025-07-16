# You are given a 0-indexed m x n integer matrix grid consisting of distinct integers
#  from 0 to m * n - 1. You can move in this matrix from a cell to any other cell
#  in the next row.
# That is, if you are in cell (x, y) such that x < m - 1, you can move to any
#  of the cells (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1).
# Note that it is not possible to move from cells in the last row.
# Each possible move has a cost given by a 0-indexed 2D array moveCost
#  of size (m * n) x n, where moveCost[i][j] is the cost of moving from a cell
#  with value i to a cell in column j of the next row.
# The cost of moving from cells in the last row of grid can be ignored.
# The cost of a path in grid is the sum of all values of cells visited plus
#  the sum of costs of all the moves made.
# Return the minimum cost of a path that starts from any cell in the first row
#  and ends at any cell in the last row.
# ------------------------------
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# grid consists of distinct integers from 0 to m * n - 1.
# moveCost.length == m * n
# moveCost[i].length == n
# 1 <= moveCost[i][j] <= 100
from functools import cache


def min_path_cost(grid: list[list[int]], moveCost: list[list[int]]) -> int:
    # working_sol (20.08%, 11.89%) -> (319ms, 25.33mb)  time: O(m * n) | space: O(m * n)

    @cache
    def dfs(row: int, col: int) -> int:
        cell_cost: int = grid[row][col]
        if len(grid) <= row + 1:
            return grid[row][col]
        lowest_move: int = 100 * 100
        for column in range(0, len(grid[0])):
            move_cost: int = moveCost[grid[row][col]][column]
            lowest_move = min(
                lowest_move,
                move_cost + cell_cost + dfs(row + 1, column)
            )

        return lowest_move

    out: int = 100 * 100
    for column in range(len(grid[0])):
        out = min(out, dfs(0, column))
    
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `grid`,
#                              n - height of the input matrix `grid`.
# We're always using every cell of the input matrix `grid`, once => O(m * n).
# ------------------------------
# Auxiliary space: O(m * n)
# Ignore stack. But cache is O(m * n) <- every cell coords pair is stored.


test: list[list[int]] = [[5, 3], [4, 0], [2, 1]]
test_movecost: list[list[int]] = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
test_out: int = 17
assert test_out == min_path_cost(test, test_movecost)

test = [[5, 1, 2], [4, 0, 3]]
test_movecost = [
    [12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]
]
test_out = 6
assert test_out == min_path_cost(test, test_movecost)
