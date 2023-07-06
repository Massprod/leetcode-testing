# Given an array of positive integers nums and a positive integer target,
#  return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
# --------------------
# Follow up: If you have figured out the O(n) solution,
#  try coding another solution of which the time complexity is O(n log(n)).
# --------------------
# 1 <= target <= 10 ** 9
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 4


def min_subarray_len(target: int, nums: list[int]) -> int:
    pass


test1 = [2,3,1,2,4,3]
test1_target = 7
test1_out = 2

test2 = [1,4,4]
test2_target = 4
test2_out = 1

test3 = [1,1,1,1,1,1,1,1]
test3_target = 11
test3_out = 0
