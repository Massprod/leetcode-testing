# Given an integer array nums containing distinct positive integers,
#  find and return any number from the array that is neither the minimum
#  nor the maximum value in the array, or -1 if there is no such number.
# Return the selected integer.
# ------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# All values in nums are distinct
from random import shuffle, randint


def find_non_min_or_max(nums: list[int]) -> int:
    # working_sol (10.26%, 46.49%) -> (22ms, 16.66mb)  time: O(n) | space: O(1)
    out: int = -1
    if 1 == len(nums):
        return out
    min_val: int = min(nums[0], nums[1])
    max_val: int = max(nums[0], nums[1])
    for index in range(2, len(nums)):
        val: int = nums[index]
        if val > max_val:
            if min_val != val:
                out = max_val
            max_val = val
        if val < min_val:
            if max_val != val:
                out = min_val
            min_val = val
        if min_val < val < max_val:
            out = val
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# Auxiliary space: O(1)
# Only 4 constant INTs used, none of them depends on input => O(1).


test: list[int] = [3, 2, 1, 4]
test_out: int = 3
assert test_out == find_non_min_or_max(test)

test = [1, 2]
test_out = -1
assert test_out == find_non_min_or_max(test)

test = [2, 1, 3]
test_out = 2
assert test_out == find_non_min_or_max(test)

test = list(set([randint(1, 100) for _ in range(100)]))
shuffle(test)
print(test)
