# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
#  - A land cell if grid[r][c] = 0, or
#  - A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:
#  - Catch all the fish at cell (r, c), or
#  - Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally,
#  or 0 if no water cell exists.
# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c)
#  or (r - 1, c) if it exists.
# ------------------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# 0 <= grid[i][j] <= 10
from random import randint
from collections import deque


def find_max_fix(grid: list[list[int]]) -> int:
    # working_sol (88.26%, 90.89%) -> (201ms, 16.52mb)  time: O(n * m) | space: O(n * m)
    def bfs(cell: tuple[int, int]) -> int:
        cur_row: int
        cur_col: int
        bfs_out: int = grid[cell[0]][cell[1]]
        grid[cell[0]][cell[1]] = 0
        options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        que: deque[tuple[int, int]] = deque([cell])
        while que:
            cur_row, cur_col = que.popleft()
            for row_step, col_step in options:
                step_row: int = cur_row + row_step
                if not (0 <= step_row < len(grid)):
                    continue
                step_col: int = cur_col + col_step
                if not (0 <= step_col < len(grid[0])):
                    continue
                if 0 == grid[step_row][step_col]:
                    continue
                que.append((step_row, step_col))
                bfs_out += grid[step_row][step_col]
                grid[step_row][step_col] = 0
        return bfs_out

    out: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if 0 != grid[row][col]:
                out = max(out, bfs((row, col)))
    return out


# Time complexity: O(n * m) <- n - number of columns in the input matrix `grid`,
#                              m - number of rows in the input matrix `grid`.
# We're always traversing the whole matrix `grid`, once => O(n * m).
# And for every cell we check, there are 4 options to check => O(4 * (n * m)).
# ------------------------------
# Auxiliary space: O(n * m)
# In the worst case, we will have space allocated for every cell of the `grid` in a `que` => O(n * m).


test: list[list[int]] = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
test_out: int = 7
assert test_out == find_max_fix(test)

test = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
test_out = 1
assert test_out == find_max_fix(test)

test = [[randint(0, 10) for _ in range(10)] for _ in range(10)]
print(test)
