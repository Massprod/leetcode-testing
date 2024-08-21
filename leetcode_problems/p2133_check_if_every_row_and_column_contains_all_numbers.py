# An n x n matrix is valid if every row
#  and every column contains all the integers from 1 to n (inclusive).
# Given an n x n integer matrix matrix, return true if the matrix is valid.
# Otherwise, return false.
# --------------------------
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# 1 <= matrix[i][j] <= n


def check_valid(matrix: list[list[int]]) -> bool:
    # working_sol (11.45%, 5.51%) -> (651ms, 18.31mb)  time: O(n * m) | space: O(n * m)
    data_bank: dict[str, dict[int, set[int]]] = {
        'rows': {},
        'cols': {},
    }
    for row in range(len(matrix)):
        data_bank['rows'][row] = set()
        for col in range(len(matrix[0])):
            if col not in data_bank['cols']:
                data_bank['cols'][col] = set()
            data_bank['rows'][row].add(matrix[row][col])
            data_bank['cols'][col].add(matrix[row][col])
    for row_vals in data_bank['rows'].values():
        if len(row_vals) != len(matrix):
            return False
    for col_vals in data_bank['cols'].values():
        if len(col_vals) != len(matrix):
            return False
    return True


# Time complexity: O(n * m) <- n - length of the input matrix `matrix`, m - height of the input matrix `matrix`.
# Always traversing whole input matrix `matrix`, once => O(n * m).
# Extra traversing every row and column to check their values => O(n * m + n + m).
# --------------------------
# Auxiliary space: O(n * m)
# Essentially every cell of the matrix is stored in `rows` and `cols` => O(n * m).


test: list[list[int]] = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
test_out: bool = True
assert test_out == check_valid(test)

test = [[1, 1, 1], [1, 2, 3], [1, 2, 3]]
test_out = False
assert test_out == check_valid(test)
