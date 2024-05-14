# In a gold mine grid of size m x n, each cell in this mine has
#  an integer representing the amount of gold in that cell, 0 if it is empty.
# Return the maximum amount of gold you can collect under the conditions:
#  - Every time you are located in a cell you will collect all the gold in that cell.
#  - From your position, you can walk one step to the left, right, up, or down.
#  - You can't visit the same cell more than once.
#  - Never visit a cell with 0 gold.
#  - You can start and stop collecting gold from any position in the grid that has some gold.
# ----------------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 15
# 0 <= grid[i][j] <= 100
# There are at most 25 cells containing gold.
from random import randint, choice


def get_maximum_gold(grid: list[list[int]]) -> int:
    # working_sol (96.37%, 94.92%) -> (1122ms, 16.48mb)  time: O(m * n * 4 ** g) | space: O(g)
    # (top, right, bot, left)
    options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # W.e the # of cells present, we're always limited by all gold in the `grid` anyway.
    max_gold: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            max_gold += grid[row][col]

    def dfs(_row: int, _col: int) -> int:
        nonlocal options
        dfs_out: int = 0
        restore_val: int = grid[_row][_col]
        for option in options:
            new_row: int = _row + option[0]
            new_col: int = _col + option[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col]:
                grid[_row][_col] = 0
                dfs_out = max(dfs_out, dfs(new_row, new_col))
                grid[_row][_col] = restore_val
        # (dfs path + cell value)
        return dfs_out + restore_val

    out: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            out = max(out, dfs(row, col))
            if max_gold == out:
                break
    return out


# Time complexity: O(m * n * 4 ** g) <- m - number of rows in input matrix `grid`,
#                                       n - number of columns in input matrix `grid`,
#                                       g - number of gold cells in input matrix `grid`.
# Strange task, because if we had other constraints with all cells being gold.
# Then it could be O((m * n) ** 2), but because we're limited in gold-cells and have only 15 * 15 matrix's.
# It can be solved with this, no idea how we could cache or reuse values, so don't see another way anyway.
# In this case, we're always trying to start from every cell (m * n) and check 4 directions.
# But all of this limited by golden cells == g, we can only have `dfs` path with 25 cells at max => O(m * n * 4 ** g).
# ----------------------------
# Auxiliary space: O(g)
# Maximum depth of the `dfs` is equal to # of the golden cells => O(g).


test: list[list[int]] = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
test_out: int = 24
assert test_out == get_maximum_gold(test)

test = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
test_out = 28
assert test_out == get_maximum_gold(test)

test = [[0 for _ in range(15)] for _ in range(15)]
gold_cells: int = 0
for row in range(len(test)):
    for col in range(len(test[0])):
        test[row][col] = choice([randint(1, 100), 0]) if gold_cells < 25 else 0
        if test[row][col]:
            gold_cells += 1
print(test)
