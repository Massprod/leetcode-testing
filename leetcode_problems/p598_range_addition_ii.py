# You are given an m x n matrix M initialized with all 0's and an array of operations ops,
#  where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
# Count and return the number of maximum integers in the matrix after performing all the operations.
# -------------------------
# 1 <= m, n <= 4 * 10 ** 4
# 0 <= ops.length <= 10 ** 4
# ops[i].length == 2
# 1 <= ai <= m
# 1 <= bi <= n


def max_count(m: int, n: int, ops: list[list[int]]) -> int:
    # working_sol (77.83%, 95.06%) -> (63ms, 18.31mb)  time: O(n) | space: O(1)
    # We can't simulate it with these constraints.
    if not ops:
        return m * n
    min_x: int = m * n
    min_y: int = m * n  # can't be higher
    # But we can see, that we're always changing values in slices.
    # Like 0 -> slice_x all of these values going to grow by 1.
    # And w.e the next `operation` is going to be, it's always going to change at least
    #  x == 0, and it will grow by 1. So it's always growing.
    # But it goes for all the values we use with minimum `slice_x` we use.
    # Every value from this minimum `slice_x` is going to be higher than everything on the right.
    # If we don't care about `Y` it's all we need.
    # But with `Y` axis, we need to consider what values sliced by `slice_y`.
    # It's the same rule, and we're getting rectangle of `m * n` size in the end.
    # And all the values inside this rectangle going to be the Highest.
    for slice_x, slice_y in ops:
        min_x = min(min_x, slice_x)
        min_y = min(min_y, slice_y)
    return min_x * min_y


# Time complexity: O(n) <- n - length of the input array `ops`.
# Always traversing whole `ops`, once => O(n).
# -------------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input.


test_m: int = 3
test_n: int = 3
test_ops: list[list[int]] = [[2, 2], [3, 3]]
test_out: int = 4
assert test_out == max_count(test_m, test_n, test_ops)

test_m = 3
test_n = 3
test_ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
test_out = 4
assert test_out == max_count(test_m, test_n, test_ops)

test_m = 3
test_n = 3
test_ops = []
test_out = 9
assert test_out == max_count(test_m, test_n, test_ops)
