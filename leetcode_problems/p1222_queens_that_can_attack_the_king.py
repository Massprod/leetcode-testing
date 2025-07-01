# On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one white king.
# You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni]
#  represents the position of the ith black queen on the chessboard.
# You are also given an integer array king of length 2 where king = [xKing, yKing]
#  represents the position of the white king.
# Return the coordinates of the black queens that can directly attack the king.
# You may return the answer in any order.
# -----------------------------
# 1 <= queens.length < 64
# queens[i].length == king.length == 2
# 0 <= xQueeni, yQueeni, xKing, yKing < 8
# All the given positions are unique.


def queens_attack_the_king(queens: list[list[int]], king: list[int]) -> list[list[int]]:
    # working_sol (100.00%,  7.64%) -> (0ms, 18.05mb)  time: O(n) | space: O(n)
    out: list[list[int]] = []
    
    min_row: int = 0
    min_col: int = 0
    max_row: int = 7
    max_col: int = 7
    # [ (row, col) ]
    fast_queens: set[tuple[int, int]] = set(
        [(pos[1], pos[0]) for pos in queens]
    )
    # [ (dy, dx) ]
    directions: list[tuple[int, int]] = [
        (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    ]
    for dy, dx in directions:
        # [y, x]
        new_row, new_col = king[1], king[0]
        while (min_row <= new_row <= max_row
               and min_col <= new_col <= max_col):
            new_row, new_col = new_row + dy, new_col + dx
            if (new_row, new_col) in fast_queens:
                out.append([new_col, new_row])
                break
    
    return out


# Time complexity: O(n) <- n - length of the input array `queens`.
# Traversing whole input array `queens` to build `fast_queens` => O(n).
# ChessBoard and directions are always of the same size.
# In the worst case we're going to have a king in the middle
#  and all the queens on the edges.
# Whole ChessBoard will be traversed, once => O(1).
# -----------------------------
# Auxiliary space: O(n)
# `fast_queens` <- allocates space for each queen position from the `queens` => O(n).


test_queens: list[list[int]] = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
test_king: list[int] = [0, 0]
test_out: list[list[int]] = [[0, 1], [1, 0], [3, 3]]
assert test_out == sorted(queens_attack_the_king(test_queens, test_king))

test_queens = [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]]
test_king = [3, 3]
test_out = [[2, 2], [3, 4], [4, 4]]
assert test_out == sorted(queens_attack_the_king(test_queens, test_king))
