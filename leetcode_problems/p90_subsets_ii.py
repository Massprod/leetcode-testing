# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# -------------------------
# 1 <= nums.length <= 10  ,  -10 <= nums[i] <= 10


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    pass


test1 = [1, 2, 2]
test1_out = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

test2 = [0]
test2_out = [[], [0]]
