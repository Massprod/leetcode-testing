# Given two n x n binary matrices mat and target,
#  return true if it is possible to make mat equal to target by rotating mat
#  in 90-degree increments, or false otherwise.
# ---------------------------
# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 <= n <= 10
# mat[i][j] and target[i][j] are either 0 or 1.


def find_rotation(mat: list[list[int]], target: list[list[int]]) -> bool:
    # working_sol (41.93%, 77.54%) -> (47ms, 16.50mb)  time: O(n * n) | space: O(n * n)

    # Transpose -> every column to row
    # mat[i][j] = mat[j][i] <- transpose
    # Reverse every row == 90 degrees clockwise
    # OR <- all in one:
    # mat[i][j] = mat[j][n - i - 1] <- n - length of the matrix
    def rotate_clockwise(matrix: list[list[int]]) -> list[list[int]]:
        length: int = len(matrix)
        rotated: list[list[int]] = [
            [0 for _ in range(length)] for _ in range(length)
        ]
        for row in range(length):
            for col in range(length):
                new_row, new_col = col, length - 1 - row
                rotated[new_row][new_col] = matrix[row][col]
        return rotated

    option: list[list[int]] = mat
    for _ in range(4):
        option = rotate_clockwise(option)
        if option == target:
            return True
    return False


# Time complexity: O(n * n) <- n - length | height of the input matrix `mat`.
# At max, we're going to rotate the original matrix 4 times => O(4 * (n * n)).
# And for every rotation we compare it to `target` => O(4 * 2 * (n * n)).
# `len(mat)` == `len(target)` <- extra 2 traverses of `n * n` elements.
# ---------------------------
# Auxiliary space: O(n * n)
# `option` <- is a copy of original `mat` => O(n * n).
# `rotated` <- always a copy of original `mat` in size => O(2 * (n * n)).


test: list[list[int]] = [[0, 1], [1, 0]]
test_target: list[list[int]] = [[1, 0], [0, 1]]
test_out: bool = True
assert test_out == find_rotation(test, test_target)

test = [[0, 1], [1, 1]]
test_target = [[1, 0], [0, 1]]
test_out = False
assert test_out == find_rotation(test, test_target)

test = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
test_target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
test_out = True
assert test_out == find_rotation(test, test_target)
