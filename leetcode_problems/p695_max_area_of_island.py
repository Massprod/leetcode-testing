# You are given an m x n binary matrix grid.
# An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid.
# If there is no island, return 0.
# ----------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
from random import randint
from collections import deque


def max_area_of_island(grid: list[list[int]]) -> int:
    # working_sol (100%, 89.41%) -> (20ms, 16.84mb)  time: O(n * m) | space: O(n * m)
    out: int = 0

    def check_island(start_row: int, start_col: int) -> int:
        nonlocal grid
        cur_row: int
        cur_col: int
        dy: int
        dx: int
        grid[start_row][start_col] = 0
        # top, right, bot, left
        options: list[tuple[int, int]] = [
            (-1, 0), (0, 1), (1, 0), (0, -1)
        ]
        que: deque[tuple[int, int]] = deque(
            [(start_row, start_col)]
        )
        island_size: int = 1
        while que:
            cur_row, cur_col = que.popleft()
            for option in options:
                dy, dx = option
                step_row: int = cur_row + dy
                step_col: int = cur_col + dx
                if ((0 <= step_row < len(grid) and 0 <= step_col < len(grid[0]))
                        and (1 == grid[step_row][step_col])):
                    grid[step_row][step_col] = 0
                    que.append(
                        (step_row, step_col)
                    )
                    island_size += 1
        return island_size

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if 1 == grid[row][col]:
                out = max(
                    out, check_island(row, col)
                )
    return out


# Time complexity: O(n * m) <- n - length of the input matrix `grid`, m - height of the input matrix `grid`.
# Always traversing whole input matrix `grid`, once => O(m * n).
# In the worst case, there's only `1` in `grid` we will extra traverse every index of `grid` => O(2 * m * n).
# ----------------------
# Auxiliary space: O(n * m)
# In the worst case, there's only `1` in the `grid`.
# And every cell of the `grid` will be used in `que` => O(n * m).


test: list[list[int]] = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
test_out: int = 6
assert test_out == max_area_of_island(test)

test = [[0, 0, 0, 0, 0, 0, 0, 0]]
test_out = 0
assert test_out == max_area_of_island(test)

test = [[randint(0, 1) for _ in range(50)] for _ in range(50)]
print(test)
