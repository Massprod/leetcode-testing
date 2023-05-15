# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# m == matrix.length  ,  n == matrix[0].length
# 1 <= m, n <= 200  ,  -231 <= matrix[i][j] <= 231 - 1

# Follow up:
#   A straightforward solution using O(mn) space is probably a bad idea.
#   A simple improvement uses O(m + n) space, but still not the best solution.
#   Could you devise a constant space solution?


def set_zeroes(matrix: list[list[int]]) -> None:
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
