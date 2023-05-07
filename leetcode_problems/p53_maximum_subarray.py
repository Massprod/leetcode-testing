# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.

def max_sub_array(nums: list[int]) -> int:
    pass


# Already been solving tasks with max_sum but for 3 nums, there's used all nums in some range.
# Because of that, we can't skip values and need to check every possible index.
# 100% sure I need to use conquer and divide but with recursion or just while loop?
# Time limit or not, first going to try loop.

test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test1_out = 6

test2 = [1]
test2_out = 1

test3 = [5, 4, -1, 7, 8]
test3_out = 23
