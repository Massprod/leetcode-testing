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
    ch_board = [["." for _ in range(n)] for _ in range(n)]
    row_placements = {}
    busy_box = {}

    def check_pos(pos_y: int, pos_x: int) -> bool:
        if not busy_box[(pos_y, pos_x)]:
            for _ in range(n):
                busy_box[(pos_y, _)] = True
            for _ in range(n):
                busy_box[(_, pos_x)] = True
            try:
                for _ in range(1, n):
                    busy_box[(pos_y + _, pos_x + _)] = True
            except KeyError:
                pass
            try:
                for _ in range(1, n):
                    busy_box[(pos_y + _, pos_x - _)] = True
            except KeyError:
                pass
            return True
        else:
            return False

    all_placements = []
    starting_x = 0
    starting_y = 0
    while starting_x < n:
        copy = deepcopy(ch_board)
        q_count = 0
        for free_y in range(n):
            for free_x in range(n):
                busy_box[(free_y, free_x)] = False
        if q_count == 0:
            for _ in busy_box:
                busy_box[_] = False
        if check_pos(starting_y, starting_x):
            q_count += 1
            row_placements[starting_y] = copy[starting_y]
            row_placements[starting_y][starting_x] = "Q"
            for y in range(n):
                for x in range(n):
                    if check_pos(y, x):
                        q_count += 1
                        row_placements[y] = copy[y]
                        row_placements[y][x] = "Q"
                        break
        if q_count == n:
            variants = len(all_placements)
            all_placements.append([])
            for _ in range(n):
                all_placements[variants].append("".join(row_placements[_]))
        starting_x += 1
    return all_placements


# I was hard_coding, but it worked :)
# 100% this is not a good_looking solution and I can make it better, but today isn't a day for this.

# 1 -> there's always one Queen at any row.
# 2 -> always going from top to bottom -> we can ignore top coordinates and check only: (y+1)(x+1) | (y+1)(x-1)


test1 = 4
test1_out = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
test = place_n_queens(test1)
for _ in test:
    print(_)

test2 = 1
test2_out = [["Q"]]
test = place_n_queens(test2)
for _ in test:
    print(_)

test3 = 5
test3_out = "???"
test = place_n_queens(test3)
for _ in test:
    print(_)

test4 = 6
test4_out = []  # there's no solution for n == 3, 6..., or I don't see it
test = place_n_queens(test4)
for _ in test:
    print(_)
