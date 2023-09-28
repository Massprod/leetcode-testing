# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
#  to be validated according to the following rules:
#   - Each row must contain the digits 1-9 without repetition.
#   - Each column must contain the digits 1-9 without repetition.
#   - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#   - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#   - Only the filled cells need to be validated according to the mentioned rules.
# ------------------------
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


def valid_sudoku(board: list[list[str]]) -> bool:
    # working_sol (81.62%, 93.48%) -> (97ms, 16.2mb)  time: O(n) | space: O(n)
    # Always 9 rows, 9 cols, 9 cubes == constraints.
    rows: dict[int, set[str]] = {row: set() for row in range(len(board))}
    columns: dict[int, set[str]] = {col: set() for col in range(len(board[0]))}
    cubes: dict[int, set[str]] = {cube: set() for cube in range(len(board))}
    cur_cube: int = 0
    # Rows from top -> bottom and cubes from left -> right.
    for row in range(len(board)):
        # Starting cube.
        if 0 <= row < 3:
            cur_cube = 0
        elif 3 <= row < 6:
            cur_cube = 3
        elif 6 <= row < 9:
            cur_cube = 6
        for col in range(len(board[0])):
            # Every 3 columns(indexes) we're stepping into a new cube.
            if col != 0 and col % 3 == 0:
                cur_cube += 1
            if board[row][col] != '.':
                cell_value: str = board[row][col]
                # Check for value being unique in cur_cube,
                if cell_value not in cubes[cur_cube]:
                    cubes[cur_cube].add(cell_value)
                else:
                    return False
                # row,
                if cell_value not in rows[row]:
                    rows[row].add(cell_value)
                else:
                    return False
                # and column.
                if cell_value not in columns[col]:
                    columns[col].add(cell_value)
                else:
                    return False
    return True


# Time complexity: O(n) -> we're always have same input size, so creating of dictionaries for cubes, rows, cols => O(1)
# n - length of input matrix^^| -> traversing whole input matrix, once => O(n).
# m - height of input matrix^^|
# Auxiliary space: O(n) -> because we're having same input size we will have same dictionaries, but values placed
#                          inside will depend on input matrix, we can have 2 values on whole matrix or None, or even
#                          fully correct sudoku as input -> but we will store at max full rows, columns and cubes ->
#                          -> rows + columns == input matrix values, except '.' they're ignored ->
#                          -> cubes will have same values stored => O(2n).


test: list[list[str]] = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
test_out: bool = True
assert test_out == valid_sudoku(test)

test = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
test_out = False
assert test_out == valid_sudoku(test)

test = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]
test_out = False
assert test_out == valid_sudoku(test)
