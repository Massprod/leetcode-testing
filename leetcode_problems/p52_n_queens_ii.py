from copy import deepcopy
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.


def queen_variants(n: int) -> int:
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
    return len(all_placements)

# There's no time limit in description and I want to try my variant as first. 5k ms :)
#


test1 = 4
test1_out = 2
assert test1_out == queen_variants(test1)

test2 = 1
test2_out = 1
assert test2_out == queen_variants(test2)
