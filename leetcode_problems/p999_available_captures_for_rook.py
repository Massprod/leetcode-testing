# You are given an 8 x 8 matrix representing a chessboard.
# There is exactly one white rook represented by 'R', some number of white bishops 'B',
#  and some number of black pawns 'p'. Empty squares are represented by '.'.
# A rook can move any number of squares horizontally or vertically (up, down, left, right)
#  until it reaches another piece or the edge of the board.
# A rook is attacking a pawn if it can move to the pawn's square in one move.
# Note: A rook cannot move through other pieces, such as bishops or pawns.
# This means a rook cannot attack a pawn if there is another piece blocking the path.
# Return the number of pawns the white rook is attacking.
# -------------------
# board.length == 8
# board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'

def num_rook_captures(board: list[list[str]]) -> int:
    # working_sol: (78.42%, 32.46%) -> (33ms, 16.51mb)  time: O(n * m) | space: O(1)
    out: int = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if 'R' == board[row][col]:
                # [(dy, dx)]
                options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for dy, dx in options:
                    new_row: int = row
                    new_col: int = col
                    while True:
                        new_row += dy
                        new_col += dx
                        if not (0 <= new_row < len(board)) or not (0 <= new_col < len(board[0])):
                            break
                        if '.' != board[new_row][new_col]:
                            if 'p' == board[new_row][new_col]:
                                out += 1
                            break
    return out


# Time complexity: O(n * m) <- n - height of the input matrix `board`, m - length of the input matrix `board`
# In the worst case: [['.', 'p'], ['p', 'R'].
# Always going to traverse every cell in `board` to get to the `R` => O(n * m).
# Extra we're going to traverse (n * m - 1) elements => O(2 * n * m).
# -------------------
# Auxiliary space: O(1).
# `options` <- always of constant size => O(1).


test: list[list[str]] = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
test_out: int = 3
assert test_out == num_rook_captures(test)

test = [[".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
test_out = 0
assert test_out == num_rook_captures(test)

test = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
        [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
test_out = 3
assert test_out == num_rook_captures(test)

test = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "R", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
test_out = 0
assert test_out == num_rook_captures(test)
