# Given an m x n matrix of distinct numbers,
#  return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element
#  in its row and maximum in its column.
# -----------------------
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 10 ** 5.
# All elements in the matrix are distinct.
from random import randint


def lucky_numbers(matrix: list[list[int]]) -> list[int]:
    # working_sol (38.63%, 43.01%) -> (115ms, 16.82mb)  time: O(m * n + (m + n)) | space: O(n + m)
    max_val: int = 10 ** 5 + 1
    # [max_value on the index_row] <- index == number of the row
    rows: list[int] = [max_val] * len(matrix)
    # [min_value on the index_column] <- index == number of the column
    cols: list[int] = [0] * len(matrix[0])
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            cur_val: int = matrix[row][col]
            rows[row] = min(rows[row], cur_val)
            cols[col] = max(cols[col], cur_val)
    out: list[int] = []
    for row in range(len(rows)):
        for col in range(len(cols)):
            row_min = rows[row]
            col_max = cols[col]
            if row_min == col_max:
                out.append(row_min)
    return out


# Time complexity: O(m * n + (m + n)) <- m - height of the input `matrix`, n - length of the input `matrix`.
# Always creating 2 extra arrays `rows` and `cols` with sizes: `m` and `n` => O(n + m).
# Traversing whole input `matrix` to get all mins and maxs, once => O((n + m) + (n * m)).
# Extra traversing our extra arrays with `n` and `m` sizes to get lucky numbers => O(2 * (n + m) + (n * m)).
# -----------------------
# Auxiliary space: O(n + m)
# `rows` always of size `m` => O(m).
# `cols` always of size `n` => O(n + m).
# `out` at max will store only one value from each row => O(n + 2 * m).


test: list[list[int]] = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
test_out: list[int] = [15]
assert test_out == lucky_numbers(test)

test = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
test_out = [12]
assert test_out == lucky_numbers(test)

test = [[7, 8], [1, 2]]
test_out = [7]
assert test_out == lucky_numbers(test)

test_vals: set[int] = set()
while len(test_vals) < 2500:
    test_vals.add(randint(1, 10 ** 5))
test = [[test_vals.pop() for _ in range(50)] for _ in range(50)]
print(test)
