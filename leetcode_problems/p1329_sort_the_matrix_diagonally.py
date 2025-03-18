# A matrix diagonal is a diagonal line of cells starting from some cell
#  in either the topmost row or leftmost column and going in the
#  bottom-right direction until reaching the matrix's end.
# For example, the matrix diagonal starting from mat[2][0],
#  where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
# Given an m x n matrix mat of integers, sort each matrix diagonal
#  in ascending order and return the resulting matrix.
# --------------------------
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100


def diagonal_sort(mat: list[list[int]]) -> list[list[int]]:
    # working_sol (35.39%, 99.38%) -> (7ms, 18.06mb)  time: O(m * n * log(m * n))
    #                                                 space: O(sqr(m ** 2 + n ** 2))

    def sort_diag(start_y: int, start_x: int, matrix: list[list[int]]) -> None:
        values: list[int] = []
        populate: bool = False
        index: int = 0
        for step in range(2):
            if 1 == step:
                populate = True
                values.sort()
            row: int = start_y
            column: int = start_x
            while (0 <= row < len(matrix)
                and 0 <= column < len(matrix[0])):
                if not populate:
                    values.append(matrix[row][column])
                else:
                    matrix[row][column] = values[index]
                    index += 1
                row += 1
                column += 1

    for column in range(len(mat[0])):
        sort_diag(0, column, mat)
    for row in range(1, len(mat)):
        sort_diag(row, 0, mat)

    return mat


# Time complexity: O(m * n * log(m * n)) <- m - length of the input matrix `mat`,
#                                           n - length of the input matrix `mat`.
# Essentially we're sorting whole matrix `mat` => O(m * n * log(m * n)).
# --------------------------
# Auxiliary space: O(sqr(m ** 2 + n ** 2))
# `values` <- allocates space for all diagonals.
# diag of rectangle == sqr(m ** 2 + n ** 2).


test: list[list[int]] = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
test_out: list[list[int]] = [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]
assert test_out == diagonal_sort(test)
