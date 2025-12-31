# There is a 1-based binary matrix where 0 represents land and 1 represents water.
# You are given integers row and col representing the number of rows
#  and columns in the matrix, respectively.
# Initially on day 0, the entire matrix is land. However,
#  each day a new cell becomes flooded with water.
# You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents
#  that on the ith day, the cell on the rith row and cith column (1-based coordinates)
#  will be covered with water (i.e., changed to 1).
# You want to find the last day that it is possible to walk from the top to the bottom
#  by only walking on land cells.
# You can start from any cell in the top row and end at any cell in the bottom row.
# You can only travel in the four cardinal directions (left, right, up, and down).
# Return the last day where it is possible to walk from the top
#  to the bottom by only walking on land cells.
# --- --- --- ---
# 2 <= row, col <= 2 * 10 ** 4
# 4 <= row * col <= 2 * 10 ** 4
# cells.length == row * col
# 1 <= ri <= row
# 1 <= ci <= col
# All the values of cells are unique.
from collections import deque


def latest_day_to_cross(row: int, col: int, cells: list[list[int]]) -> int:
    # working_solution: (12.15%, 43.09%) -> (1781ms, 26.84mb)  Time: O(k * log(k) * n * m) Space: O(n * m)
    # BS + BFS
    def bfs(day: int, rows: int, cols: int, water_cells: list[list[int]]) -> bool:
        cell_row: int
        cell_col: int
        n_cell_row: int
        n_cell_col: int

        last_row: int = rows - 1
        # top, right, bot, left <- (dy, dx)
        directions: list[tuple[int, int]] = [
            (-1, 0), (0, 1), (1, 0), (0, -1)
        ]
        visited: set[tuple[int, int]] = set()
        matrix: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]
        water_sign: int = 1
        for cell in water_cells[:day + 1]:
            # (1-based coordinates) -1 for that.
            cell_row, cell_col = cell[0] - 1, cell[1] - 1
            matrix[cell_row][cell_col] = water_sign
            visited.add((cell_row, cell_col))

        # (row, col) | and ignore already water taken cells.
        que: deque[tuple[int, int]] = deque(
            [(0, column) for column in range(cols) if 0 == matrix[0][column]]
        )
        while que:
            cell_row, cell_col = que.popleft()
            for dy, dx in directions:
                n_cell_row, n_cell_col = cell_row + dy, cell_col + dx
                new_cell: tuple[int, int] = (n_cell_row, n_cell_col)
                if not (
                    0 <= n_cell_row < rows                   # row bound
                    and 0 <= n_cell_col < cols               # column bound
                    and 0 == matrix[n_cell_row][n_cell_col]  # not water cell
                    and new_cell not in visited              # still not visited
                ):
                    continue
                # Already last row.
                if last_row == n_cell_row:
                    return True
                
                que.append(new_cell)
                visited.add(new_cell)

        return False
    
    left: int = 0
    right: int = len(cells) - 1
    out: int = -1
    while left <= right:
        middle: int = (right + left) // 2
        # We're still capable of crossing it.
        if bfs(middle, row, col, cells):
            out = middle
            left = middle + 1
        else:
            right = middle - 1

    return out + 1  # +1 for 1 indexed rules.


# Time complexity: O(k * log(k) * n * m )
# n - `row` input value
# m - `cols` input value
# k - length of the input array `cells`
# We check every cell option of the `cells`, and we use `BFS` to check them
# Every `BFS`` `n * m`, `BS` checks `k * log(k)` => O(k * log(k) * n * m).
# --- --- --- ---
# Space complexity: O(n * m)
# `matrix` <- allocates space for each cell of the given size => O(n * m).
# `visited` <- allocates space for each cell of the `matrix` => O(n * m).


test_row: int = 2
test_col: int = 2
test_cells: list[list[int]] = [[1, 1], [2, 1], [1, 2], [2, 2]]
test_out: int = 2
assert test_out == latest_day_to_cross(test_row, test_col, test_cells)

test_row = 2
test_col = 2
test_cells = [[1, 1], [1, 2], [2, 1], [2, 2]]
test_out = 1
assert test_out == latest_day_to_cross(test_row, test_col, test_cells)

test_row = 3
test_col = 3
test_cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
test_out = 3
assert test_out == latest_day_to_cross(test_row, test_col, test_cells)
