# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# ------------------------
# 1 <= nums.length <= 10  ,  -10 <= nums[i] <= 10
# All the numbers of nums are unique.


def subsets(nums: list[int]) -> list[list[int]]:
    pass


test1 = [1, 2, 3]
test1_out = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

test2 = [0]
test2_out = [[], [0]]
