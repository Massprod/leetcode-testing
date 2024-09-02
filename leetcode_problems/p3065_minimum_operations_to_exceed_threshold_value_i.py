# You are given a 0-indexed integer array nums, and an integer k.
# In one operation, you can remove one occurrence of the smallest element of nums.
# Return the minimum number of operations needed so that all elements
#  of the array are greater than or equal to k.
# ------------------------
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 10 ** 9
# 1 <= k <= 10 ** 9
# The input is generated such that there is at least one index i such that nums[i] >= k.


def min_operations(nums: list[int], k: int) -> int:
    # working_sol (86.51%, 98.64%) -> (41ms, 16.34mb)  time: O(n) | space: O(1)
    out: int = 0
    for num in nums:
        if num < k:
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always using every value from `nums`, once => O(n).
# ------------------------
# Auxiliary space: O(1).
# Only one constant INT is used, doesn't depends on input => O(1).


test: list[int] = [2, 11, 10, 1, 3]
test_k: int = 10
test_out: int = 3
assert test_out == min_operations(test, test_k)

test = [1, 1, 2, 4, 9]
test_k = 1
test_out = 0
assert test_out == min_operations(test, test_k)

test = [1, 1, 2, 4, 9]
test_k = 9
test_out = 4
assert test_out == min_operations(test, test_k)
