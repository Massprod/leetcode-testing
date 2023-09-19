# You start at the cell (rStart, cStart) of an rows x cols grid facing east.
# The northwest corner is at the first row and column in the grid,
#  and the southeast corner is at the last row and column.
# You will walk in a clockwise spiral shape to visit every position in this grid.
# Whenever you move outside the grid's boundary, we continue our walk outside the grid
#  (but may return to the grid boundary later.).
# Eventually, we reach all rows * cols spaces of the grid.
# Return an array of coordinates representing the positions of the grid in the order you visited them.
# ----------------------
# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols


def spiral_matrix(rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
    # working_sol (81.78%, 96.51%) -> (93ms, 17.5mb)  time: O(max(m, n) ** 2) | space: O(m * n)
    # maximum size of row|column, inside the matrix.
    row_limit: int = rows
    col_limit: int = cols
    y: int = rStart
    x: int = cStart
    dx: int = 0
    dy: int = 0
    # All coordinates inside given matrix limits.
    insides: list[list[int]] = [[y, x]]
    # Maximum cells in given matrix.
    all_insides: int = rows * cols
    turn: int = 0
    # Standard steps we need to cover first ROW|COLUMN.
    y_steps: int = 1
    x_steps: int = 1
    # Essentially we're just traversing matrix, and storing correct coordinates.
    # From some given point, we just travel ROW|COLUMN and expand it on turns.
    # Starting from sizes: ROW == 1, COLUMN == 1 and ending only when all coordinates added.
    while len(insides) != all_insides:
        if turn == 4:
            turn = 0
        if turn == 0:
            dx = 1
            dy = 0
        elif turn == 1:
            dx = 0
            dy = 1
        elif turn == 2:
            dx = -1
            dy = 0
        elif turn == 3:
            dx = 0
            dy = -1
        cur_steps: int = 0
        if turn == 0 or turn == 2:
            while cur_steps != x_steps:
                y += dy
                x += dx
                cur_steps += 1
                # Inside matrix.
                if 0 <= y < row_limit and 0 <= x < col_limit:
                    insides.append([y, x])
                # Out of bounds, no reasons to make steps.
                # Just change coordinate to the last position we could have reach.
                elif dx == 1 and x >= col_limit:
                    x += dx * (x_steps - cur_steps)
                    break
                elif dx == -1 and x < 0:
                    x += dx * (x_steps - cur_steps)
                    break
            x_steps += 1
            turn += 1
        elif turn == 1 or turn == 3:
            while cur_steps != y_steps:
                y += dy
                x += dx
                cur_steps += 1
                if 0 <= y < row_limit and 0 <= x < col_limit:
                    insides.append([y, x])
                elif dy == 1 and y >= row_limit:
                    y += dy * (y_steps - cur_steps)
                    break
                elif dy == -1 and y < 0:
                    y += dy * (y_steps - cur_steps)
                    break
            y_steps += 1
            turn += 1
    return insides


# Time complexity: O(max(m, n) ** 2) -> worst case == starting from some corner, so we will traverse almost
# m - rows input_value^^|  whole square matrix with size of distance from starting point to the furthest corner ->
# n - cols input_value^^| -> how to calc it correctly? -> dunno, but it's actually always comes to max(m, n),
#                         at least with picture given, from any point I tried to traverse its same == 6 ->
#                         -> and because it's square we can call it O(max(m, n) ** 2).
#                         Looked in editorial, they have the same complexity. Should be correct.
# Auxiliary space: O(m * n) -> storing all correct indexes of matrix with size == (rows * cols) => O(m * n).
# ----------------------
# We don't care about anything except ROW and COLUMN sizes we're travelling.
# Set row == 1, col = 1 and increment by 1 for some turns?
# And save (y, x) coordinates which exist in matrix.
# Actually, coordinates just needs to be in (0, input_cols) and (0, input_rows) inclusive.
# No reasons to create matrix. Let's test.


test_r: int = 1
test_c: int = 4
r_start: int = 0
c_start: int = 0
test_out: list[list[int]] = [[0, 0], [0, 1], [0, 2], [0, 3]]
assert test_out == spiral_matrix(test_r, test_c, r_start, c_start)

test_r = 5
test_c = 6
r_start = 1
c_start = 4
test_out = [
    [1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2],
    [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0],
    [1, 0], [0, 0]
]
assert test_out == spiral_matrix(test_r, test_c, r_start, c_start)
