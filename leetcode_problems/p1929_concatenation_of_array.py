# Given an integer array nums of length n, you want to create an array
#  ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
# --------------------------
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000


def get_concatenation(nums: list[int]) -> list[int]:
    # working_sol (93.03%, 82.07%) -> (62ms, 16.74mb)  time: O(n) | space: O(n)
    return nums + nums


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums`, once => O(n).
# --------------------------
# Auxiliary space: O(n).
# `output` array is always with size == `2 * n` => O(2n).


test: list[int] = [1, 2, 1]
test_out: list[int] = [1, 2, 1, 1, 2, 1]
assert test_out == get_concatenation(test)

test = [1, 3, 2, 1]
test_out = [1, 3, 2, 1, 1, 3, 2, 1]
assert test_out == get_concatenation(test)
