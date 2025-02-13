# Given an m x n matrix mat, return an array of all the elements
#  of the array in a diagonal order.
# --------------------
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10 ** 4
# 1 <= m * n <= 10 ** 4
# -10 ** 5 <= mat[i][j] <= 10 ** 5
from random import randint

from pyperclip import copy


def find_diagonal_order(mat: list[list[int]]) -> list[int]:
    # working_sol (65.47%, 83.44%) -> (11ms, 19.67mb)  time: O(m * n) | space: O(m * n)
    x: int
    y: int
    dy: int
    dx: int
    new_x: int
    new_y: int

    dx, dy = 1, -1
    x, y = 0, 0
    out: list[int] = [mat[y][x]]
    cells_count: int = len(mat) * len(mat[0])
    while len(out) != cells_count:
        new_y, new_x = y + dy, x + dx
        if (not (0 <= new_y < len(mat))
            or not (0 <= new_x < len(mat[0]))):
            if 1 == dy:
                new_y = y + 1
                new_x = x
                # We can't go lower => shift right.
                if not (0 <= new_y < len(mat)):
                    new_y = y
                    new_x = x + 1
                # But direction shift is the same.
                dy, dx = -1, 1
            elif -1 == dy:
                new_y = y
                new_x = x + 1
                # We can't go higher => shift bot.
                if not (0 <= new_x < len(mat[0])):
                    new_y = y + 1
                    new_x = x
                # But direction shift is the same.
                dy, dx = 1, -1

        y, x = new_y, new_x
        out.append(mat[y][x])

    return out


# Time complexity: O(m * n) <- m - height of the input matrix `mat`
#                              n - length of the input matrix `mat`
# Always traversing every value of the input matrix `mat`, once => O(m * n).
# --------------------
# Auxiliary space: O(m * n)
# `out` <- allocates space for each value of the input matrix `mat` => O(m * n).


test: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_out: list[int] = [1, 2, 4, 7, 5, 3, 6, 8, 9]
assert test_out == find_diagonal_order(test)

test = [[1, 2], [3, 4]]
test_out = [1, 2, 3, 4]
assert test_out == find_diagonal_order(test)

test = [[randint(-10 ** 5, 10 ** 5) for _ in range(10 ** 2)] for _ in range(10 ** 2)]
copy(test)
