# You are given a 2D integer array ranges and two integers left and right.
# Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.
# Return true if each integer in the inclusive range [left, right]
#  is covered by at least one interval in ranges.
# Return false otherwise.
# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
# -----------------------
# 1 <= ranges.length <= 50
# 1 <= starti <= endi <= 50
# 1 <= left <= right <= 50


def is_covered(ranges: list[list[int]], left: int, right: int) -> bool:
    # working_sol (74.43%, 69.98%) -> (41ms, 16.40mb)  time: O(n * k) | space: O(1)
    all_vals: list[bool] = [True for _ in range(51)]
    for start, end in ranges:
        for val in range(start, end + 1):
            all_vals[val] = False
    return not any(all_vals[left: right + 1])


# Time complexity: O(n * k) <- n - length of the input array `ranges`, k - average range size in `ranges`.
# We're always traversing whole `ranges` and cover all values in given ranges => O(n * k).
# In the worst case: left == 0, right == len(range) - 1
# Extra slicing and traversing `all_vals` => O(n * k + 2 * n).
# -----------------------
# Auxiliary space: O(1)
# `all_vals` <- always of the same size == 51 => O(1).


test: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
test_left: int = 2
test_right: int = 5
test_out: bool = True
assert test_out == is_covered(test, test_left, test_right)

test = [[1, 10], [10, 20]]
test_left = 21
test_right = 21
test_out = False
assert test_out == is_covered(test, test_left, test_right)
