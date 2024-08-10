# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\',
#  or blank space ' '.
# These characters divide the square into contiguous regions.
# Given the grid grid represented as a string array, return the number of regions.
# Note that backslash characters are escaped, so a '\' is represented as '\\'.
# -----------------------
# n == grid.length == grid[i].length
# 1 <= n <= 30
# grid[i][j] is either '/', '\', or ' '.
from collections import deque


def regions_by_slashes(grid: list[str]) -> int:
    # working_sol (39.92%, 100%) -> (151ms, 16.40mb)  time: O(m * n) | space: O(m * n)
    # Expand to x3 of size, and mark zones for every slash.
    new_grid: list[list[int]] = [[0 for _ in range(len(grid[0]) * 3)] for _ in range(len(grid) * 3)]
    for row in range(len(grid)):
        shift_y: int = 3 * row
        for col in range(len(grid[0])):
            shift_x: int = 3 * col
            if grid[row][col] == '\\':
                new_grid[shift_y][shift_x] = 1
                new_grid[shift_y + 1][shift_x + 1] = 1
                new_grid[shift_y + 2][shift_x + 2] = 1
            elif grid[row][col] == '/':
                new_grid[shift_y][shift_x + 2] = 1
                new_grid[shift_y + 1][shift_x + 1] = 1
                new_grid[shift_y + 2][shift_x] = 1

    def bfs_mark(start_row: int, start_col: int) -> None:
        cell_row: int
        cell_col: int
        # (dy, dx)
        check_dirs: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        que: deque[tuple[int, int]] = deque([(start_row, start_col)])
        while que:
            cell_row, cell_col = que.popleft()
            for dy, dx in check_dirs:
                new_row: int = cell_row + dy
                new_col: int = cell_col + dx
                if (0 <= new_row < len(new_grid)
                        and 0 <= new_col < len(new_grid[0])
                        and 1 != new_grid[new_row][new_col]):
                    que.append((new_row, new_col))
                    new_grid[new_row][new_col] = 1

    out: int = 0
    for row in range(len(new_grid)):
        for col in range(len(new_grid[0])):
            if 1 != new_grid[row][col]:
                bfs_mark(row, col)
                out += 1
    return out


# Time complexity: O(m * n) <- m - height of the input matrix `grid`, n - length of the input matrix `grid`.
# Always creating a x3 size of the `grid` => `new_grid` => O((m * n) * 3).
# Traversing every cell of the `grid` and filling the slashes, always the same 3 moves => O((m * n) * 3 + m * n).
# Checking every empty area with BFS, and in the worst case there's all cells are empty.
# So, we're going to traverse the whole `grid`, once => O((m * n) * 3 + m * n + (m * n) * 3).
# -----------------------
# Auxiliary space: O(m * n)
# `new_grid` <- always of the same size == `(m * n) * 3` => O((m * n) * 3).
# `que` <- in the worst case, when every cell is empty, `que` will allocate space for each => O(((m * n) * 3) * 2)


test: list[str] = [" /", "/ "]
test_out: int = 2
assert test_out == regions_by_slashes(test)

test = [" /", "  "]
test_out = 1
assert test_out == regions_by_slashes(test)

test = ["/\\", "\\/"]
test_out = 5
assert test_out == regions_by_slashes(test)
