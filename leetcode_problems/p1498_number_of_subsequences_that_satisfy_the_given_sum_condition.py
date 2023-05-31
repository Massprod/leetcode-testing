# You are given an array of integers nums and an integer target.
#  Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it
#  is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
# --------------------
# 1 <= nums.length <= 105  ,  1 <= nums[i] <= 106  ,  1 <= target <= 106


def num_subseq(nums: list[int], target: int) -> int:
    pass


test1 = [3, 5, 6, 7]
test1_target = 9
test1_out = 4

test2 = [3, 3, 6, 8]
test2_target = 10
test2_out = 6

test3 = [2, 3, 3, 4, 6, 7]
test3_target = 12
test3_out = 61
