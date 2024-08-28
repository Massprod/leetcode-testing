# Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer.
# Make answer equal to matrix, then replace each element with the value -1 with the maximum element
#  in its respective column.
# Return the matrix answer.
# ----------------------------------
# m == matrix.length
# n == matrix[i].length
# 2 <= m, n <= 50
# -1 <= matrix[i][j] <= 100
# The input is generated such that each column contains at least one non-negative integer.


def modified_matrix(matrix: list[list[int]]) -> list[list[int]]:
    # working_sol (79.32%, 97.02%) -> (72ms, 16.45mb)  time: O(m * n) | space: O(m * n)
    column_maxes: list[int] = [-1 for _ in range(len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            column_maxes[col] = max(column_maxes[col], matrix[row][col])
    out: list[list[int]] = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if -1 == matrix[row][col]:
                out[row][col] = column_maxes[col]
            else:
                out[row][col] = matrix[row][col]
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `matrix`, n - height of the input matrix `matrix`.
# Creating `column_maxes` with the size of `m` => O(m).
# Traversing whole input matrix `matrix` => O(m + m * n).
# Creating `out` of the same size as `matrix` => O(m + m * n + m * n).
# Extra traversing whole `matrix`, again => O(m + m * n * 3)
# ----------------------------------
# Auxiliary space: O(m * n).
# `column_maxes` <- allocates space for `m` values => O(m).
# `out` <- allocates space for each value from `matrix`, copy of it => O(m * n + m).


test: list[list[int]] = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]
test_out: list[list[int]] = [[1, 2, 9], [4, 8, 6], [7, 8, 9]]
assert test_out == modified_matrix(test)

test = [[3, -1], [5, 2]]
test_out = [[3, 2], [5, 2]]
assert test_out == modified_matrix(test)
