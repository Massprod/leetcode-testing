# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# You may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space, respectively.
from copy import deepcopy


def place_n_queens(n: int) -> list[list[str]]:
    # working_sol (5.2%, 6.17%) -> (5338ms, 17mb)  time: (n ** (n * n)) | space: O(n * n)
    ch_board = [["." for _ in range(n)] for _ in range(n)]
    row_placements = {}
    busy_box = {}
    for free_y in range(n):
        for free_x in range(n):
            busy_box[(free_y, free_x)] = False

    def check_pos(busy_b: dict, pos_y: int, pos_x: int) -> dict | bool:
        if not busy_b[(pos_y, pos_x)]:
            for _ in range(n):
                busy_b[(pos_y, _)] = True
            for _ in range(n):
                busy_b[(_, pos_x)] = True
            for _ in range(1, n):
                busy_b[(pos_y + _, pos_x + _)] = True
            for _ in range(1, n):
                busy_b[(pos_y + _, pos_x - _)] = True
            return busy_b
        else:
            return False

    all_placements = []

    def backtrack_count(busy: dict, start_y: int, start_x: int, board: list[list[str]], q_count: int = 0) -> None:
        if q_count == n:
            placement = []
            for _ in row_placements:
                placement.append("".join(row_placements[_]))
            all_placements.append(placement)
            return
        old_busy = deepcopy(busy)
        for _ in range(start_x, n):
            if new_busy := check_pos(old_busy, start_y, _):
                row_placements[start_y] = board[start_y]
                row_placements[start_y][_] = "Q"
                backtrack_count(new_busy, start_y + 1, start_x, board, q_count + 1)
                row_placements[start_y][_] = "."
                old_busy = deepcopy(busy)
    backtrack_count(busy_box, 0, 0, ch_board)
    return all_placements

# Time complexity: O(n ** (n * n)) -> for every n row (we're having rows == input(n)) calling recursion, and for every
#                                     x value in this recursion, calling another recursion.
#                                     Recursion tree with size of n and n * n branches.
# Space complexity: O(n * n) -> list with n * n values, and dictionary for every recursion call.
#                               n + n * n -> worst O(n * n)

# Omega slow and complicated solution, but I don't want to google
# before I hit hard wall or complete it, at least like this.

# Well. Didn't expect old_busy = deepcopy(busy) <- to work but it did :)

# Either I need to save and recover dict with busy coordinates or clear them,
# but I cant clear them, cuz we will rewrite busy coordinates from top points.
# Only way I see is saving prev X coordinates and recreate busy_box on every call

# 1 -> there's always one Queen at any row.
# 2 -> always going from top to bottom -> we can ignore top coordinates and check only: (y+1)(x+1) | (y+1)(x-1)


test1 = 4
test1_out = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
test = place_n_queens(test1)
for _ in test:
    print(_, "1")
    assert _ in test1_out

test2 = 1
test2_out = [["Q"]]
test = place_n_queens(test2)
for _ in test:
    print(_, "2")
    assert _ in test2_out

# test3 - failed - cuz I was recording only solution with 1 way from top -> bottom,
#                  but there's multiple with same start at the top. I need to use backtracking or find a way to record
#                  midways and move through all x's in y loop.
test3 = 5
test3_out = [["Q....", "..Q..", "....Q", ".Q...", "...Q."], ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
             [".Q...", "...Q.", "Q....", "..Q..", "....Q"], [".Q...", "....Q", "..Q..", "Q....", "...Q."],
             ["..Q..", "Q....", "...Q.", ".Q...", "....Q"], ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
             ["...Q.", "Q....", "..Q..", "....Q", ".Q..."], ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
             ["....Q", ".Q...", "...Q.", "Q....", "..Q.."], ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]]
test = place_n_queens(test3)
for _ in test:
    print(_, "3")
    assert _ in test3_out
    assert len(test) == len(test3_out)

test4 = 6
test4_out = []  # there's no solution for n == 3, 6..., or I don't see it <- there's 4 solutions, mistakes_made
test = place_n_queens(test4)
for _ in test:
    print(_)
    print(len(test))
