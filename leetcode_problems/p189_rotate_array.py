# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# --------------------
# 1 <= nums.length <= 105  ,  -231 <= nums[i] <= 231 - 1  ,  0 <= k <= 105
# --------------------
# Try to come up with as many solutions as you can.
# There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


def rotate(nums: list[int], k: int) -> None:
    pass


test1 = [1, 2, 3, 4, 5, 6, 7]
test1_k = 3
test1_out = [5, 6, 7, 1, 2, 3, 4]

test2 = [-1, -100, 3, 99]
test2_k = 2
test2_out = [3, 99, -1, -100]
