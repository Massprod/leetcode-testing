# You are given an integer array nums.
# The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr]
#  is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
# Return the maximum absolute sum of any (possibly empty) subarray of nums.
# Note that abs(x) is defined as follows:
#  - If x is a negative integer, then abs(x) = -x.
#  - If x is a non-negative integer, then abs(x) = x.
# ----------------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 4 <= nums[i] <= 10 ** 4
from random import randint


def max_absolute_sum(nums: list[int]) -> int:
    # working_sol (96.93%, 69.35%) -> (299ms, 30.19mb)  time: O(n) | space: O(1)
    # Kadane's algorithm
    # Only thing we care about, is that we can have abs() of the sum.
    # But, it's only the abs(sum) not elements of the sum.
    # So, we can have maximized a sum with all positive values, and maximized sum with all negative values.
    # And use abs(negative_sum), which can be higher than sum of the positive values.
    cur_max: int = 0
    max_ending: int = 0
    # max_sum
    for num in nums:
        max_ending += num
        if max_ending > cur_max:
            cur_max = max_ending
        if max_ending < 0:
            max_ending = 0
    cur_min: int = 0
    max_ending = 0
    # min_sum
    for num in nums:
        max_ending += num
        if max_ending < cur_min:
            cur_min = max_ending
        if max_ending > 0:
            max_ending = 0
    return max(cur_max, abs(cur_min))


# Time complexity: O(n) <- n - length of input array `nums`.
# Always traversing whole input array `nums` twice.
# First time to get maximum positive sum => O(n).
# Second time to get maximum negative sum => O(2n).
# ----------------------
# Auxiliary space: O(1)
# Only 3 constant INT's used, none of them depends on input => O(1).


test: list[int] = [1, -3, 2, 3, -4]
test_out: int = 5
assert test_out == max_absolute_sum(test)

test = [2, -5, 1, -4, 3, -2]
test_out = 8
assert test_out == max_absolute_sum(test)

test = [randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 5)]
print(test)
