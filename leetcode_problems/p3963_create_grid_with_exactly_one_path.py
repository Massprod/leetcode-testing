# You are given two integers m and n, representing the number of rows
#  and columns of a grid.
# Construct any m x n grid consisting only of the characters '.' and '#', where:
#  - '.' represents a free cell.
#  - '#' represents an obstacle cell.
# A valid path is a sequence of free cells that:
#  - Starts at the top-left cell (0, 0).
#  - Ends at the bottom-right cell (m - 1, n - 1).
#  - Moves only:
#   - Right, from (i, j) to (i, j + 1), or
#   - Down, from (i, j) to (i + 1, j).
# Return any grid such that there is exactly one valid path from the top-left cell
#  to the bottom-right cell.
# --- --- --- ---
# 1 <= m, n <= 25


def create_grid(m: int, n: int) -> list[str]:
    # working_solution: (100.00%, 66.67%) -> (0ms, 19.29mb)  Time: O(m * n) Space: O(m * n)
    grid: list[list[str]] = [
        ['#' for _ in range(n)] for _ in range(m)
    ]
    for col in range(n):
        grid[0][col] = '.'
    for row in range(m):
        grid[row][-1] = '.'
    
    out: list[str] = [
        ''.join(row) for row in grid
    ]

    return out


# Time complexity: O(m * n)
# --- --- --- ---
# Space complexity: O(m * n)


test_m: int = 2
test_n: int = 3
test_out: list[str] = ["...", "##."]
assert test_out == create_grid(test_m, test_n)

test_m = 3
test_n = 3
test_out = ["...", "##.", "##."]
assert test_out == create_grid(test_m, test_n)

test_m = 1
test_n = 4
test_out = ["...."]
assert test_out == create_grid(test_m, test_n)
