# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal
# and all the elements on the secondary diagonal that are not part of the primary diagonal.
# --------------------
# n == mat.length == mat[i].length
# 1 <= n <= 100  ,  1 <= mat[i][j] <= 100


def diagonal_sum(mat: list[list[int]]) -> int:
    # working_sol (54.37%, 81.9%) -> (123ms, 16.5mb)  time: O(n) | space: O(1)
    ascend_y: int = len(mat) - 1
    ascend_x: int = 0
    descend_y: int = 0
    descend_x: int = 0
    summ: int = 0
    while ascend_y >= 0:
        summ += mat[descend_y][descend_x]
        if ascend_y != descend_y:
            summ += mat[ascend_y][ascend_x]
        descend_y += 1
        descend_x += 1
        ascend_y -= 1
        ascend_x += 1
    return summ

# Time complexity: O(2 * (sqr(2) * n)) -> traversing both diagonals of a square once => O(2 * (sqr(2) * n) ->
# matrix is always square^^| -> O(2 * 1.4 * n) => O(2.8 * n) => O(n) <- linear grow, depends on input.
# n - len of matrix col^^  |
# Space complexity: O(1) -> 5 extra constants, all INTs, doesn't depends on input => O(1)
# -----------------------
# Basic way is to calc (y - x) == (y1 - x1) == (yn - xn) <- for descending(primary) diag,
#                  and (y + x) == (y1 + x1) == (yn + xn) <- for ascending(secondary) diag.
# But same as with Queen problem, I don't like this solution because we're checking every single index in a matrix,
# if we make pointer and just take steps on +1, +1 for descending and -1, -1 for ascending.
# Then we're skipping extra indexes and only count what we need. Not so much of a speed-up but still.


test1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
test1_out = 25
print(diagonal_sum(test1))
assert test1_out == diagonal_sum(test1)

test2 = mat = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
test2_out = 8
print(diagonal_sum(test2))
assert test2_out == diagonal_sum(test2)

test3 = [[5]]
test3_out = 5
print(diagonal_sum(test3))
assert test3_out == diagonal_sum(test3)
