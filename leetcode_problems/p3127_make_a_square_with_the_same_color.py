# You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'.
# Character 'W' represents the white color, and character 'B' represents the black color.
# Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square
#  where all cells are of the same color.
# Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.
# ------------------------
# grid.length == 3
# grid[i].length == 3
# grid[i][j] is either 'W' or 'B'.


def can_make_square(grid: list[list[str]]) -> bool:
    # working_sol (26.85%, 6.86%) -> (2ms, 16.80mb)  time: O(1) | space: O(1)
    def check_corner(
            row: int,
            col: int,
            _corner_options: list[tuple[int, int]],
            _grid: list[list[str]],
    ) -> bool:
        start_cell: str = grid[row][col]
        w_neighbours: int = 0
        b_neighbours: int = 0
        for dy, dx in _corner_options:
            new_row: int = row + dy
            new_col: int = col + dx
            if 0 <= new_row < len(_grid) and 0 <= new_col < len(_grid[0]):
                if 'B' == _grid[new_row][new_col]:
                    b_neighbours += 1
                else:
                    w_neighbours += 1
        if 'B' == start_cell and (1 >= w_neighbours or 3 == w_neighbours):
            return True
        if 'W' == start_cell and (1 >= b_neighbours or 3 == b_neighbours):
            return True
        return False

    # (dy, dx)
    options: list[list[tuple[int, int]]] = [
        [(-1, 0), (-1, -1), (0, -1)],  # top-left corner
        [(-1, 0), (-1, 1), (0, 1)],  # top-right corner
        [(0, -1), (1, -1), (1, 0)],  # bot-left corner
        [(0, 1), (1, 1), (1, 0)],  # bot-right corner
    ]
    start_row: int = 1
    start_col: int = 1
    for corner_options in options:
        if check_corner(start_row, start_col, corner_options, grid):
            return True
    return False


# Time complexity: O(1).
# Always traversing all matrix corners, withing the same matrix of constant size => O(1).
# ------------------------
# Auxiliary space: O(1).


test: list[list[str]] = [["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]
test_out: bool = True
assert test_out == can_make_square(test)

test = [["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]
test_out = False
assert test_out == can_make_square(test)

test = [["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]
test_out = True
assert test_out == can_make_square(test)
