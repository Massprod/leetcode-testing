# Given an m x n matrix, return true if the matrix is Toeplitz.
# Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left
#  to bottom-right has the same elements.
# ------------------------
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99


def is_toeplitz_matrix(matrix: list[list[int]]) -> bool:
    # working_sol (16.90%, 49.75%) -> (91ms, 16.50mb)  time: O(n * m) | space: O(1)

    def check_diag(start_cell: tuple[int, int]) -> bool:
        check_out: bool = True
        dy: int = 1
        dx: int = 1
        base_val: int = matrix[start_cell[0]][start_cell[1]]
        y: int = start_cell[0] + dy
        x: int = start_cell[1] + dx
        while 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
            if base_val != matrix[y][x]:
                check_out = False
                break
            y += dy
            x += dx
        return check_out

    for start_x in range(0, len(matrix[0])):
        if not check_diag((0, start_x)):
            return False
    for start_y in range(1, len(matrix)):
        if not check_diag((start_y, 0)):
            return False
    return True


# Time complexity: O(n * m) <- n - height of the input matrix `matrix`, m - length of the input matrix `matrix`.
# In the worst case, we're traversing whole input matrix `matrix`, once => O(n * m).
# ------------------------
# Auxiliary space: O(1).
# Only constant INT's used, none of them depends on the input `matrix` => O(1).


test: list[list[int]] = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
test_out: bool = True
assert test_out == is_toeplitz_matrix(test)

test = [[1, 2], [2, 2]]
test_out = False
assert test_out == is_toeplitz_matrix(test)
