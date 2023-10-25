# We build a table of n rows (1-indexed).
# We start by writing 0 in the 1st row. Now in every subsequent row,
#  we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
# ---------------------
# 1 <= n <= 30
# 1 <= k <= 2 ** (n - 1)


def kth_grammar(n: int, k: int) -> int:
    # working_sol (96.91%, 79.64%) -> (28ms, 16.16mb)  time: O(n) | space: O(1)
    # Every new row is x2 size of previous row.
    # And new values are always flipped values from previous row.
    # 0 <- 1 row.
    # 0 | 1 <- 2 row.
    # 01 | 10 <- 3 row.
    # 0110 | 1001 <- 4 row, etc.
    if n == 1:
        return 0
    # 0 or 1 assume it's value on random.
    cur_sym: int = 1
    for row in range(n, 1, -1):
        all_row: int = 2 ** (row - 1)
        half_row: int = all_row // 2
        # Index on right side -> switch value.
        if k > half_row:
            cur_sym = 1 - cur_sym
            k -= half_row
    # If original assumption was correct.
    if cur_sym:
        return 0
    # Otherwise, return opposite.
    return 1


# Time complexity: O(n) -> we're always decreasing current 'row' to the first row => O(n).
# n - input value 'n'^^|
# Auxiliary space: O(1) -> nothing extra which depends on input => O(1).


test_n: int = 1
test_k: int = 1
test_out: int = 0
assert test_out == kth_grammar(test_n, test_k)

test_n = 2
test_k = 1
test_out = 0
assert test_out == kth_grammar(test_n, test_k)

test_n = 2
test_k = 2
test_out = 1
assert test_out == kth_grammar(test_n, test_k)

test_n = 30
test_k = 2 ** 29
test_out = 1
assert test_out == kth_grammar(test_n, test_k)
