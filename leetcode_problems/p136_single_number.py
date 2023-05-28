# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# --------------------------
# 1 <= nums.length <= 3 * 104  ,  -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


def single_number(nums: list[int]) -> int:
    pass


# O(1) - space, O(n) - time, huh.
# So we can't rebuild or sort, only some constants.
# Sum? Like, left_right loop with summarizing everything and extracting after we encounter double?
# Nah, we would need extra space to store used values, and if only 1 value remembered we will lose values.
#


test1 = [2, 2, 1]
test1_out = 1

test2 = [4, 1, 2, 1, 2]
test2_out = 4

test3 = [1]
test3_out = 1
