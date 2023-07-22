# On an n x n chessboard, a knight starts at the cell (row, column)
#   and attempts to make exactly k moves.
# The rows and columns are 0-indexed, so the top-left cell is (0, 0),
#   and the bottom-right cell is (n - 1, n - 1).
# A chess knight has eight possible moves it can make.
# Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
# Each time the knight is to move,
#   it chooses one of eight possible moves uniformly at random
#   (even if the piece would go off the chessboard) and moves there.
# The knight continues moving until it has made exactly k moves or has moved off the chessboard.
# Return the probability that the knight remains on the board after it has stopped moving.
# ---------------------------
# 1 <= n <= 25
# 0 <= k <= 100
# 0 <= row, column <= n - 1


def knight_probability(n: int, k: int, row: int, column: int) -> float:
    # working_sol (74.82%, 30.27%) -> (227ms, 25.6mb)  time: O(log(8 ** k)) | space: O(log(8 ** k)) <- doubt.
    # (steps, y_coor, x_coor) -> storing every possible cell
    # we already visited with STEPS.
    # Because STEPS will affect probability of this cell.
    # STEPS -> steps left to do/use.
    visited: dict[tuple[int, int, int], float] = {}
    # y - row, x - column
    y_limit: int = n - 1
    x_limit: int = n - 1
    # dy, dx -> possible cell coor changes(steps), knight moves.
    possible_moves: list[tuple[int, int]] = [
        (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)
    ]

    def all_moves(steps: int, start_y: int, start_x: int) -> int | float:
        # If we land on chessboard we should calc probability of this cell.
        if steps != 0 and 0 <= start_y <= y_limit and 0 <= start_x <= x_limit:
            # Default is always 0.
            all_prob: float = 0.0
            # Doing every possible knight_move.
            for dy, dx in possible_moves:
                # Cell to move.
                new_cell: tuple[int, int, int] = (steps, start_y + dy, start_x + dx)
                # If we already visited this cell, with the same
                # steps left we can reuse it.
                if new_cell in visited:
                    visit: float = visited[new_cell]
                else:
                    visit = all_moves(steps - 1, start_y + dy, start_x + dx)
                # Probability of a cell is SUM of every probability to land on chessboard
                # of all possible moves from this cell.
                all_prob += visit
                visited[new_cell] = visit
            return all_prob / 8
        # If we land on chessboard and there's no steps left then it's 100% move.
        if steps == 0 and 0 <= start_y <= y_limit and 0 <= start_x <= x_limit:
            return 1
        # Otherwise, it's 0% to stay on chessboard with this move.
        if not 0 <= start_y <= y_limit or not 0 <= start_x <= x_limit:
            return 0

    return all_moves(k, row, column)


# Time complexity: O(log(8 ** K)) -> standard recursion call for K == 1 is simple check of 8 possible knight_moves,
# K - input steps^^|       so for any K it should be like (8 ** K), but some calls will be reused ->
#                          -> and if call leading off board then it's recorded, and we didn't make any calls from it ->
#                          -> so we're not recalling from OFF_board and REUSE already visited nodes with same STEPS ->
#                          -> how to calc it? Actually no idea how to calc it correctly, suppose it's =>
#                          => O(log (8 ** k)) <- log() to take some part of (8 ** k), no idea what base of log().
# Auxiliary space: O(log(8 ** K)) -> for every recursion call we're storing its (steps, y, x) data ->
#                                 -> so it should be the same number of values as number of calls => O(log(8 ** K)).
# ^^Doubt it correctness, but I don't understand how to calc this recursion correctly.
#   Like in the worst case it's 8 calls for 8 possible moves and for every of these moves the same extra (K - 1) calls.
#   8 ** K should be correct, if we don't include reused cells and off_board cells.
#   But how we can calculate their number and exclude it?
# ---------------------------
# So it's recursion with checking of all moves from particular CELL and doing K steps from it.
# For every step it's either 1 or 0 if we land on chessboard or not and remembering where we already landed.
# Because we're doing same 8 moves, we don't need to recheck them.
# Ok. Important part, I was trying to store only VISITED CELLS, but we need STEPS to be stored as well.
# Because for a different STEPS left we're going to get different probabilities for that cell.
# ---------------------------
# Only part I don't understand is HOW to calculate PROBABILITY.
# All moves can be checked with recursion and remembering already visited coordinates.
# Don't have even the slightest idea about probability of staying on board, after all moves.
# Like it should be something like -> start from some COOR and try to move to 8 positions,
# if we lend at position which is ON chessboard than it's 1, and then we can summarize all correct
# landing positions and divide by all possible moves. But how we calculate it for WHOLE board?
# Ok. Found that we can do this by summarizing every COOR probabilities.
# Like -> we should calculate probabilities for all CELLS(coor) by themselves and summarize them all after.


test1 = 3
test1_k = 2
test1_row = 0
test1_col = 0
test1_out = 0.0625
assert test1_out == round(knight_probability(test1, test1_k, test1_row, test1_col), 5)

test2 = 1
test2_k = 0
test2_row = 0
test2_col = 0
test2_out = 1
assert test2_out == round(knight_probability(test2, test2_k, test2_row, test2_col), 5)

test3 = 25
test3_k = 100
test3_row = 12
test3_col = 12
test3_out = 0.04743
assert test3_out == round(knight_probability(test3, test3_k, test3_row, test3_col), 5)

test4 = 25
test4_k = 77
test4_row = 23
test4_col = 10
test4_out = 0.02712
assert test4_out == round(knight_probability(test4, test4_k, test4_row, test4_col), 5)
