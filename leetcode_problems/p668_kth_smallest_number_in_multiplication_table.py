# Nearly everyone has used the Multiplication Table.
# The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
# ---------------------
# 1 <= m, n <= 3 * 10 ** 4
# 1 <= k <= m * n


def find_kth_number(m: int, n: int, k: int) -> int:
    # working_sol (60.33%, 97.33%) -> (577ms, 16.19mb)  time: O(m * log(m * n) | space: O(1)
    left_l: int = 1
    right_l: int = m * n

    def check(value: int) -> int:
        # Every row is like: [1 * row, 2 * row, 3 * row ... n * row]
        # For every row we can find how many values are lower:
        # n * row == value, n = value // row, where 'n' is number of used columns.
        # Every column is unique value, so 'n' is actually number of lower values.
        # And if (value // row) > n, we need limit it to 'n'.
        # Cuz there's no row with more than 'n' columns.
        lower_values: int = 0
        for row in range(1, m + 1):
            lower_values += min(value // row, n)
        return lower_values

    # Standard BS with check for # of lower_values on every possible matrix row.
    while left_l < right_l:
        middle: int = (left_l + right_l) // 2
        # If there's (lower_values >= k), then we can make it lower.
        if check(middle) >= k:
            right_l = middle
        # Otherwise, higher.
        else:
            left_l = middle + 1
    return left_l


# Time complexity: O(m * log(m * n)) -> binary search with highest limit == (m * n), and for every check extra
# n - row_length of matrix^^|       traverse of all columns to check() for lower_values => O(m * log (m * n)).
# m - height of matrix^^|
# Auxiliary space: O(1) -> only 4 extra constant INTs used, and check() is always same rows loop => O(1).
# ---------------------
# Binary search problem:
# Min_limit == 1, Max_limit == m * n
# Every row is like: [1 * i, 2 * i, 3 * i ... n * i]
# We can check last value of the row as [n * i], where 'i' is row number.
# For every row we can find how many values are lower than what we're trying to check:
# n * i == value, value // i == n, where 'n' is number of column, and every column is unique value on this row.
# So we can find number of lower values: n == value // i.
# If we have value > n, then there's only n value lower, cuz it's row limit.
# Always taking min(value // i, n) as row values which is lower than our current check.
# Make check_value higher if we hit something with (lower values < k), and lower otherwise.


test_m: int = 3
test_n: int = 3
test_k: int = 5
test_out: int = 3
assert test_out == find_kth_number(test_m, test_n, test_k)

test_m = 2
test_n = 3
test_k = 6
test_out = 6
assert test_out == find_kth_number(test_m, test_n, test_k)

test_m = 30000
test_n = 30000
test_k = 30000
test_out = 3597
assert test_out == find_kth_number(test_m, test_n, test_k)
