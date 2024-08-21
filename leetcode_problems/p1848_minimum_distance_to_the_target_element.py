# Given an integer array nums (0-indexed) and two integers target and start,
#  find an index i such that nums[i] == target and abs(i - start) is minimized.
# Note that abs(x) is the absolute value of x.
# Return abs(i - start).
# It is guaranteed that target exists in nums.
# -----------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10 ** 4
# 0 <= start < nums.length
# target is in nums.


def get_min_distance(nums: list[int], target: int, start: int) -> int:
    # working_sol (57.81%, 61.46%) -> (53ms, 16.60mb)  time: O(n) | space: O(1)
    out: int = len(nums)
    for index, num in enumerate(nums):
        if num == target:
            out = min(out, abs(start - index))
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums`, once => O(n).
# -----------------------
# Auxiliary space: O(1).


test: list[int] = [1, 2, 3, 4, 5]
test_target: int = 5
test_start: int = 3
test_out: int = 1
assert test_out == get_min_distance(test, test_target, test_start)

test = [1]
test_target = 1
test_start = 0
test_out = 0
assert test_out == get_min_distance(test, test_target, test_start)

test = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_target = 1
test_start = 0
test_out = 0
assert test_out == get_min_distance(test, test_target, test_start)
