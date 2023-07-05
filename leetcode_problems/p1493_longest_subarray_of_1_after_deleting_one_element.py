# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.
# ----------------------
# 1 <= nums.length <= 10 ** 5
# nums[i] is either 0 or 1.


def longest_subarray(nums: list[int]) -> int:
    pass


test1 = [1, 1, 0, 1]
test1_out = 3

test2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
test2_out = 5

test3 = [1, 1, 1]
test3_out = 3
