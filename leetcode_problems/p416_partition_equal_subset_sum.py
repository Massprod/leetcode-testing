# Given an integer array nums, return true if you can partition the array
#  into two subsets such that the sum of the elements
#  in both subsets is equal or false otherwise.
# --------------------------
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
from functools import cache


def can_partition(nums: list[int]) -> bool:
    # working_sol (23.23%, 5.02%) -> (1694ms, 493.90mb)  time: O(2 ** n) | space: O(1)
    ar_sum: int = sum(nums)
    # ODD == we can't split it.
    if ar_sum % 2:
        return False
    # EVEN == we can try to split and we just need to find all values.
    # Sum of which should be equal to `ar_sum` // 2.
    target: int = ar_sum // 2

    @cache
    def check(index: int, c_sum: int) -> bool:
        nonlocal target
        if index >= len(nums):
            return target == c_sum
        # Skip value        
        if check(index + 1, c_sum):
            return True
        # Use value
        if check(index + 1, c_sum + nums[index]):
            return True
        return False

    return check(0, 0)


# Time complexity: O(2 ** n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, with 2 options to check => O(2 ** n).
# --------------------------
# Auxiliary space: O(1)
# We don't care about recursion stack => O(1).


test: list[int] = [1, 5, 11, 5]
test_out: bool = True
assert test_out == can_partition(test)

test = [1, 2, 3, 5]
test_out = False
assert test_out == can_partition(test)
