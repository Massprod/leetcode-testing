# You are given an integer array nums and an integer x.
# In one operation, you can either remove the leftmost or the rightmost element from the array nums
#   and subtract its value from x. Note that this modifies the array for future operations.
#
# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
# ---------------------------------
# 1 <= nums.length <= 10 ** 5  ,  1 <= nums[i] <= 10 ** 4  ,  1 <= x <= 10 ** 9


def min_operations(nums: list[int], x: int) -> int:
    pass


test1 = [1, 1, 4, 2, 3]
test1_x = 5
test1_out = 2

test2 = [5, 6, 7, 8, 9]
test2_x = 4
test2_out = -1

test3 = [3, 2, 20, 1, 1, 3]
test3_x = 10
test3_out = 5
