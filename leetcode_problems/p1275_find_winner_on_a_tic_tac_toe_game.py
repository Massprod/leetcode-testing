# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
# The rules of Tic-Tac-Toe are:
#  - Players take turns placing characters into empty squares ' '.
#  - The first player A always places 'X' characters, while the second player B always places 'O' characters.
#  - 'X' and 'O' characters are always placed into empty squares, never on filled ones.
#  - The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
#  - The game also ends if all squares are non-empty.
#  - No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli]
#  indicates that the ith move will be played on grid[rowi][coli].
# Return the winner of the game if it exists (A or B).
# In case the game ends in a draw return "Draw".
# If there are still movements to play return "Pending".
# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe),
#  the grid is initially empty, and A will play first.
# ---------------------
# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= rowi, coli <= 2
# There are no repeated elements on moves.
# moves follow the rules of tic tac toe.


def tic_tac_toe(moves: list[list[int]]) -> str:
    # working_sol (99.44%, 40.87%) -> (23ms, 16.53mb)  time: O(n) | space: O(1)
    cur_player: str = 'A'
    # [dy, dx]
    checks: list[list[list[int]]] = [
        [[-1, 0], [1, 0]],   # top dir, bot dir
        [[-1, -1], [1, 1]],  # desc diag dir
        [[-1, 1], [1, -1]],  # asc diag dir
        [[0, -1], [0, 1]]    # left dir, right dir
    ]
    moves_a: int = 0
    moves_b: int = 0
    board: list[list[str]] = [['' for _ in range(3)] for _ in range(3)]
    for row, col in moves:
        board[row][col] = cur_player
        moves_a += 1 if cur_player == 'A' else 0
        moves_b += 1 if cur_player == 'B' else 0
        if not ('A' == cur_player and 2 < moves_a) and not ('B' == cur_player and 2 < moves_b):
            cur_player = 'B' if cur_player == 'A' else 'A'
            continue
        for check in checks:
            count: int = 1
            for dy, dx in check:
                new_row = row
                new_col = col
                while True:
                    new_row += dy
                    new_col += dx
                    if (not 0 <= new_row < len(board)
                            or not 0 <= new_col < len(board[0])
                            or not board[new_row][new_col]):
                        break
                    if cur_player == board[new_row][new_col]:
                        count += 1
                    if count == 3:
                        return cur_player
        cur_player = 'B' if cur_player == 'A' else 'A'
    if 9 > len(moves):
        return 'Pending'
    return 'Draw'


# Time complexity: O(n) <- n - length of the input array `moves`.
# We always check the same number of options for every move, so we can count it as constant.
# And we only check these options for every move from `moves` => O(n).
# ---------------------
# Auxiliary space: O(1).
# `check` are always of the same size => O(1).
# `boars` is always 3x3 size as well => O(1).


test: list[list[int]] = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
test_out: str = "A"
assert test_out == tic_tac_toe(test)

test = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
test_out = "B"
assert test_out == tic_tac_toe(test)

test = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
test_out = "Draw"
assert test_out == tic_tac_toe(test)
