# You are given two arrays rowSum and colSum of non-negative integers
#  where rowSum[i] is the sum of the elements in the ith row and colSum[j]
#  is the sum of the elements of the jth column of a 2D matrix.
# In other words, you do not know the elements of the matrix,
#  but you do know the sums of each row and column.
# Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies
#  the rowSum and colSum requirements.
# Return a 2D array representing any matrix that fulfills the requirements.
# It's guaranteed that at least one matrix that fulfills the requirements exists.
# ----------------------
# 1 <= rowSum.length, colSum.length <= 500
# 0 <= rowSum[i], colSum[i] <= 10 ** 8
# sum(rowSum) == sum(colSum)


def restore_matrix(row_sum: list[int], col_sum: list[int]) -> list[list[int]]:
    # working_sol (89.53%, 36.82%) -> (371ms, 21.88mb)  time: O(n + m) | space: O(n * m)
    row_index: int = 0
    col_index: int = 0
    out: list[list[int]] = [[0 for _ in range(len(col_sum))] for _ in range(len(row_sum))]
    while row_index < len(row_sum) and col_index < len(col_sum):
        cur_val: int = min(row_sum[row_index], col_sum[col_index])
        out[row_index][col_index] = cur_val
        row_sum[row_index] -= cur_val
        col_sum[col_index] -= cur_val
        if not row_sum[row_index]:
            row_index += 1
        else:
            col_index += 1
    return out


# Time complexity: O(n * m) <- n - length of the input array `row_sum`,
#                              m - length of the input array `col_sum`.
# We're always creating an array `out` with size of (`n * m`) => O(n * m)
# And we're always exhausting every `row` + `col` until we can take values from them => O(n * m + n + m).
# ----------------------
# Auxiliary space: O(n * m)
# `out` is always of size `n * m` => O(n * m).


test_row: list[int] = [3, 8]
test_col: list[int] = [4, 7]
test_out: list[list[int]] = [[3, 0], [1, 7]]
assert test_out == restore_matrix(test_row, test_col)

test_row = [5, 7, 10]
test_col = [8, 6, 8]
test_out = [[5, 0, 0], [3, 4, 0], [0, 2, 8]]
assert test_out == restore_matrix(test_row, test_col)
