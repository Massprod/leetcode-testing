# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# m == matrix.length  ,  n == matrix[0].length
# 1 <= m, n <= 200  ,  -231 <= matrix[i][j] <= 231 - 1

# Follow up:
#   A straightforward solution using O(mn) space is probably a bad idea.
#   A simple improvement uses O(m + n) space, but still not the best solution.
#   Could you devise a constant space solution?


def set_zeroes(matrix: list[list[int]]) -> None:
    # working_sol (21.85%, 12.99%) -> (157ms, 18.6mb)  time: O(m * n) | space: O(m * n)
    def zeroing(y: int, x: int) -> None:
        for g in range(len(matrix[0])):
            if matrix[y][g] == 0:
                continue
            matrix[y][g] = 0
            used.add((y, g))
        for h in range(len(matrix)):
            if matrix[h][x] == 0:
                continue
            matrix[h][x] = 0
            used.add((h, x))

    used: set = set()
    for _y in range(len(matrix)):
        for _x in range(len(matrix[0])):
            if (_y, _x) in used:
                continue
            if matrix[_y][_x] == 0:
                used.add((_y, _x))
                zeroing(_y, _x)


# Time complexity: O(m * n) -> nested loop for length_n and height_m => O(m * n) ->
#                                  -> and inside of nested loop we're calling zeroing() => O(m + n) ->
#                                  -> worst case calling zeroing() and looping every row and column for m * n times ->
#                                  -> O(m * n)
# Space complexity: O(m * n) -> worst case, set is going to be fulled with every index being 0 => O(m * n)
# --------------------
# For now, only solved it with used indexes. Don't know how to avoid
# skipping another 0 on the way, without it -> auxiliary space => O(m * n)


def set_zeroes_const(matrix: list[list[int | str]]) -> None:
    # working_sol (21.85%, 12.99%) -> (143ms, 17.3mb)  time: O(m * n) | space: O(N)
    def zeroing(y: int = 0, x: int = 0, found: bool = False):
        if found:
            for _ in range(y + 1, len(matrix)):
                if matrix[_][x] == 0:
                    matrix[_][x] = "-"
                    zeroing(_, x, found=True)
                matrix[_][x] = "-"
            for _ in range(x + 1, len(matrix[0])):
                if matrix[y][_] == 0:
                    matrix[y][_] = "-"
                    zeroing(y, _, found=True)
                matrix[y][_] = "-"
            for _ in range(y - 1, -1, -1):
                if matrix[_][x] == 0:
                    matrix[_][x] = "-"
                    zeroing(_, x, found=True)
                matrix[_][x] = "-"
            for _ in range(x - 1, -1, -1):
                if matrix[y][_] == 0:
                    matrix[y][_] = "-"
                    zeroing(y, _, found=True)
                matrix[y][_] = "-"
            return
        for _y in range(y, len(matrix)):
            for _x in range(x, len(matrix[0])):
                if matrix[_y][_x] == 0:
                    matrix[_y][_x] = "-"
                    zeroing(_y, _x, found=True)

    zeroing()
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            if matrix[a][b] == "-":
                matrix[a][b] = 0

# Time complexity: O(m * n) -> 2 nested loops => O(m * n)
# Space complexity: O(m * n) -> recursion calls for m * n times in worst case
# -----------------------------------
# Made a recursion with auxiliary space of O(m * n).
# ! constant space complexity means the amount of space used
#   by your algorithm is independent of the size of the input. so you can't use recursion. !
# How can I make it work in 1 nested loop?


test1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
test1_out = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# set_zeroes(test1)
set_zeroes_const(test1)
print(test1)
for _ in test1_out:
    assert _ in test1

test2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
test2_out = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
# set_zeroes(test2)
set_zeroes_const(test2)
print(test2)
for _ in test2_out:
    assert _ in test2

test3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
test3_out = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# set_zeroes(test3)
set_zeroes_const(test3)
print(test3)
for _ in test3_out:
    assert _ in test3

test4 = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
test4_out = [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
set_zeroes_const(test4)
print(test4)
for _ in test4_out:
    assert _ in test4

test5 = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]
test5_out = [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 4], [0, 0, 0, 3], [0, 0, 0, 0]]
set_zeroes_const(test5)
print(test5)
for _ in test5_out:
    assert _ in test5
