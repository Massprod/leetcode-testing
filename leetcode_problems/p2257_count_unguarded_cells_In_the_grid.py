# You are given two integers m and n representing a 0-indexed m x n grid.
# You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli]
#  and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
# A guard can see every cell in the four cardinal directions (north, east, south, or west)
#  starting from their position unless obstructed by a wall or another guard.
# A cell is guarded if there is at least one guard that can see it.
# Return the number of unoccupied cells that are not guarded.
# -------------------------
# 1 <= m, n <= 10 ** 5
# 2 <= m * n <= 10 ** 5
# 1 <= guards.length, walls.length <= 5 * 10 ** 4
# 2 <= guards.length + walls.length <= m * n
# guards[i].length == walls[j].length == 2
# 0 <= rowi, rowj < m
# 0 <= coli, colj < n
# All the positions in guards and walls are unique.


def count_unguarded(m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
    # working_sol (54.00%, 94.15%) -> (399ms, 38.10mb)  time: O(m * n) | space: O(m * n)
    out: int = m * n - len(guards) - len(walls)
    # -1 <- guarded
    # 0 <- unchecked
    # 1 <- guard
    # 2 <- wall

    def check_dirs(row: int, col: int, matrix: list[list[int]]) -> int:
        guarded: int = 0
        directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dy, dx in directions:
            new_row: int = row + dy
            new_col: int = col + dx
            while 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                if 0 < matrix[new_row][new_col]:
                    break
                if 0 == matrix[new_row][new_col]:
                    matrix[new_row][new_col] = -1
                    guarded += 1
                new_row += dy
                new_col += dx
        return guarded

    grid: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
    for g_row, g_col in guards:
        grid[g_row][g_col] = 1
    for w_row, w_col in walls:
        grid[w_row][w_col] = 2
    for _row in range(len(grid)):
        for _col in range(len(grid[0])):
            if 1 != grid[_row][_col]:
                continue
            out -= check_dirs(_row, _col, grid)
    return out


# Time complexity: O(m * n)
# Always creating a `grid` and traversing it, size == `m * n` size => O(2 * (m * n)).
# In the worst case: there's no walls and all First column cells taken by guards.
# We will extra traverse a whole `grid` again => O(3 * (m * n)).
# -------------------------
# Auxiliary space: O(m * n)
# `grid` <- only extra space we use and its size == `m * n` => O(m * n).


test_m: int = 4
test_n: int = 6
test_guards: list[list[int]] = [[0, 0], [1, 1], [2, 3]]
test_walls: list[list[int]] = [[0, 1], [2, 2], [1, 4]]
test_out: int = 7
assert test_out == count_unguarded(test_m, test_n, test_guards, test_walls)

test_m = 3
test_n = 3
test_guards = [[1, 1]]
test_walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
test_out = 4
assert test_out == count_unguarded(test_m, test_n, test_guards, test_walls)
