# Given a 0-indexed integer array nums of length n and an integer target,
#  return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
# ----------------------
# 1 <= nums.length == n <= 50
# -50 <= nums[i], target <= 50
from random import randint


def count_pairs(nums: list[int], target: int) -> int:
    # working_sol (93.23%, 70.82%) -> (40ms, 16.43mb)  time: O(n * log n) | space: O(n)
    nums.sort()
    out: int = 0
    left: int = 0
    right: int = len(nums) - 1
    while left < right:
        cur_sum: int = nums[left] + nums[right]
        # And if we can't, then we can't take anything smaller to check.
        if cur_sum >= target:
            right -= 1
            continue
        # If we can get a correct sum with Min + Max,
        #  then every pair of Min + w.e_between will satisfy it.
        out += right - left
        left += 1
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting the input array, once => O(n * log n)
# Extra traversing whole `nums`, once => O(n * log n + n).
# ----------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n) by itself => O(n).


test: list[int] = [-1, 1, 2, 3, 1]
test_target: int = 2
test_out: int = 3
assert test_out == count_pairs(test, test_target)

test = [-6, 2, 5, -2, -7, -1, 3]
test_target = -2
test_out = 10
assert test_out == count_pairs(test, test_target)

test = [randint(-50, 50) for _ in range(50)]
print(test)
