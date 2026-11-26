# You are given an m x n matrix grid where each cell contains one of the following characters:
#  - 'L': move one cell left.
#  - 'R': move one cell right.
#  - 'U': move one cell up.
#  - 'D': move one cell down.
# You start at cell (0, 0), which is considered visited.
# At each step, move to the cell indicated by the character in your current cell.
# The process ends if the indicated move would either leave the grid or enter a cell
#  that has already been visited. In either case, the move is not made.
# Return an integer array [r, c] representing the row and column indices
#  of the last visited cell. The indices are 0-based.
# --- --- --- ---
# 1 <= m == grid.length <= 10 ** 5
# 1 <= n == grid[i].length <= 10 ** 5
# m * n <= 10 ** 5
# grid[i][j] is one of 'L', 'R', 'U', or 'D'.
from collections import deque


def last_visited_cell(grid: list[list[str]]) -> list[int]:
    # working_solution: (19.08%, 44.31%) -> (582ms, 50.78mb)  Time: O(n * m) Space: O(n * m)
    # (drow, dcolumn)
    directions: dict[str, tuple[int, int]] = {
        'U': (-1, 0),
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1),
    }
    # {(row, column)}
    visited: set[tuple[int, int]] = {(0, 0)}
    # [(row, column)]
    que: deque[tuple[int, int]] = deque([(0, 0)])
    while que:
        row, column = que.popleft()
        direction: str = grid[row][column]
        shift: tuple[int, int] = directions[direction]
        new_row, new_column = row + shift[0], column + shift[1]
        if not (0 <= new_row < len(grid)):
            return [row, column]
        if not (0 <= new_column < len(grid[0])):
            return [row, column]
        if (new_row, new_column) in visited:
            return [row, column]
        que.append((new_row, new_column))
        visited.add((new_row, new_column))

    return -1


# Time complexity: O(n * m)
# n - length of the input matrix `grid`
# m - height of the input matrix `grid`
# --- --- --- ---
# Space complexity: O(n * m)


test: list[list[str]] = [["R", "D"], ["U", "L"]]
test_out: list[int] = [1, 0]
assert test_out == last_visited_cell(test)

test = [["R", "R", "R"]]
test_out = [0, 2]
assert test_out == last_visited_cell(test)
