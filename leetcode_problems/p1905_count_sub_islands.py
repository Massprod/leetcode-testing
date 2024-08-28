# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water)
#  and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical).
# Any cells outside of the grid are considered water cells.
# An island in grid2 is considered a sub-island if there is an island
#  in grid1 that contains all the cells that make up this island in grid2.
# Return the number of islands in grid2 that are considered sub-islands.
# -----------------------------
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.
from collections import deque


def count_sub_islands(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    # working_sol (31.12%, 49.05%) -> (2270ms, 40.08mb)  time: O(m * n) | space: O(m * n)

    def get_island(row: int, col: int) -> set[tuple[int, int]]:
        cur_row: int
        cur_col: int
        # [dy, dx] -> top, right, bot, left
        visited: set[tuple[int, int]] = {(row, col)}
        options: list[list[int]] = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        que: deque[tuple[int, int]] = deque([(row, col)])
        while que:
            cur_row, cur_col = que.popleft()
            for dy, dx in options:
                new_row: int = cur_row + dy
                new_col: int = cur_col + dx
                if ((new_row, new_col) not in visited
                        and 0 <= new_row < len(grid2)
                        and 0 <= new_col < len(grid2[0])
                        and 1 == grid2[new_row][new_col]):
                    que.append((new_row, new_col))
                    visited.add((new_row, new_col))
        return visited

    out: int = 0
    visited_main: set[tuple[int, int]] = set()
    for _row in range(len(grid2)):
        for _col in range(len(grid2[0])):
            if 1 == grid2[_row][_col] and (_row, _col) not in visited_main:
                cur_island: set[tuple[int, int]] = get_island(_row, _col)
                visited_main.update(cur_island)
                correct: bool = True
                for cell_row, cell_col in cur_island:
                    if not grid1[cell_row][cell_col]:
                        correct = False
                        break
                if correct:
                    out += 1
    return out


# Time complexity: O(m * n) <- m - length of the input arrays `grid1` | `grid2`,
#                              n - length of the input arrays `grid1` | `grid2`.
# Always using every cell from `grid2`, once => O(m * n).
# And extra check its state in the `grid1` => O(2 * (m * n)).
# -----------------------------
# Auxiliary space: O(m * n)
# In the worst case whole `grid2` is an island.
# `que` <- allocates space for each cell from `grid2` => O(m * n).
# `visited_main` <- allocates space for each cell from `grid2` => O(m * n * 2).
# `visited` <- allocates space for each cell from `grid2` => O(m * n * 3).
# `cur_island` <- same size as an `visited` => O(m * n * 4).


test_1: list[list[int]] = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
test_2: list[list[int]] = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
test_out: int = 3
assert test_out == count_sub_islands(test_1, test_2)

test_1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
test_2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
test_out = 2
assert test_out == count_sub_islands(test_1, test_2)
