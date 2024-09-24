# Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
#  return the number of the battleships on board.
# Battleships can only be placed horizontally or vertically on board.
# In other words, they can only be made of the shape 1 x k (1 row, k columns)
#  or k x 1 (k rows, 1 column), where k can be of any size.
# At least one horizontal or vertical cell separates between two battleships
#  (i.e., there are no adjacent battleships).
# -----------------------
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is either '.' or 'X'.
# -----------------------
# Follow up: Could you do it in one-pass, using only O(1) extra memory
#  and without modifying the values board?


def count_battle_ships(board: list[list[str]]) -> int:
    # working_sol (64.61%, 81.90%) -> (71ms, 17.02mb)  time: O(m * n) | space: O(1)
    def check_sides(
            cell: tuple[int, int],
            side_steps: list[tuple[int, int]],
            ship_board: list[list[str]],
    ) -> bool:
        cell_row: int
        cell_col: int
        row_step: int
        col_step: int
        row_limit: int = len(ship_board)
        col_limit: int = len(ship_board[0])
        cell_row, cell_col = cell
        # We need to check the bottom cell for vertical ship.
        # And left-most cell for horizontal ship.
        for step in side_steps:
            row_step, col_step = step
            new_row: int = cell_row + row_step
            new_col: int = cell_col + col_step
            # Either out of bounds or it should be clear.
            # Otherwise, it's inside cell == False.
            if (0 <= new_row < row_limit
                    and 0 <= new_col < col_limit
                    and '.' != ship_board[new_row][new_col]):
                return False
        return True

    # [ left, bot, right] <- if they're clear == vertical ship
    vertical_ship_steps: list[tuple[int, int]] = [
        (0, -1), (1, 0), (0, 1)
    ]
    # [ top, left, bot ] <- if they're clear == horizontal ship
    horizontal_ship_steps: list[tuple[int, int]] = [
        (-1, 0), (0, -1), (1, 0)
    ]
    # Works because we guaranteed `no adjusted` ships.
    out: int = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if 'X' != board[row][col]:
                continue
            horizontal_check: bool = check_sides(
                (row, col), horizontal_ship_steps, board
            )
            if horizontal_check:
                out += 1
                continue
            vertical_check: bool = check_sides(
                (row, col), vertical_ship_steps, board
            )
            if vertical_check:
                out += 1
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `board`, n - height of the input matrix `board`.
# Always using every cell, once and our side checks are constant => O(m * n).
# -----------------------
# Auxiliary space: O(1)
# Every extra value used is constant and doesn't depend on input => O(1).


test: list[list[str]] = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
test_out: int = 2
assert test_out == count_battle_ships(test)

test = [["."]]
test_out = 0
assert test_out == count_battle_ships(test)
