# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# m == matrix.length  ,  n == matrix[0].length
# 1 <= m, n <= 200  ,  -231 <= matrix[i][j] <= 231 - 1

# Follow up:
#   A straightforward solution using O(mn) space is probably a bad idea.
#   A simple improvement uses O(m + n) space, but still not the best solution.
#   Could you devise a constant space solution?


def set_zeroes(matrix: list[list[int]]) -> None:
    # working_sol (21.85%, 12.99%) -> (157ms, 18.6mb)  time: O(
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

# Time complexity: O(m * n * (m + n)) -> nested loop for length_n and height_m => O(m * n) ->
#                                  -> and inside of nested loop we're calling zeroing() => O(m + n) ->
#                                  -> worst case calling zeroing() and looping every row and column for m * n times ->
#                                  -> O(m * n * (m + n)) <- not sure about this.
# Space complexity: O(m * n) -> worst case, set is going to be fulled with every index being 0 => O(m * n)
# --------------------
# For now, only solved it with used indexes. Don't know how to avoid
# skipping another 0 on the way, without it -> auxiliary space => O(m * n)


test1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
test1_out = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
set_zeroes(test1)
print(test1)
for _ in test1_out:
    assert _ in test1

test2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
test2_out = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
set_zeroes(test2)
print(test2)
for _ in test2_out:
    assert _ in test2

test3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
test3_out = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
set_zeroes(test3)
print(test3)
for _ in test3_out:
    assert _ in test3
