# Given an array of integers nums,
#  you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.
# -------------------------
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
from random import randint


def min_start_value(nums: list[int]) -> int:
    # working_sol (81.91%, 19.84%) -> (32ms, 16.56mb)  time: O(n) | space: O(1)
    out: int = 0
    prefix: int = 0
    # If we go from left -> right.
    # We will get some values and spend some values.
    # We should never go below 1.
    # So, when we travel, we're going to have some spike with maximum change.
    # And our first `startValue` should cover this spike and have an extra `1`.
    # Because we need `>= 1`
    for num in nums:
        prefix += num
        out = min(prefix, out)
    return out * -1 + 1


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# -------------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used, none of them depends on input => O(1).


test: list[int] = [-3, 2, -3, 4, 2]
test_out: int = 5
assert test_out == min_start_value(test)

test = [1, 2]
test_out = 1
assert test_out == min_start_value(test)

test = [1, -2, -3]
test_out = 5
assert test_out == min_start_value(test)

test = [randint(-100, 100) for _ in range(100)]
print(test)
