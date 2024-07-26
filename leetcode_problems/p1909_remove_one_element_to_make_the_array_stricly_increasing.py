# Given a 0-indexed integer array nums, return true if it can be made
#  strictly increasing after removing exactly one element, or false otherwise.
# If the array is already strictly increasing, return true.
# The array nums is strictly increasing if nums[i - 1] < nums[i]
#  for each index (1 <= i < nums.length).
# ------------------------
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
from random import randint


def can_be_increasing(nums: list[int]) -> bool:
    # working_sol (99.24%, 88.09%) -> (37ms, 16.58mb)  time: O(n) | space: O(1)
    if 2 == len(nums):
        return True
    first: bool = True
    for index in range(1, len(nums)):
        if nums[index - 1] >= nums[index]:
            if not first:
                return False
            first = False
            # We can delete either current nums[index].
            # Or we can delete previous nums[index - 1].
            # But we need to know which of them is bigger than previous nums[index - 2].
            # If nums[index] satisfies us, we can leave it.
            # Otherwise, we delete it and nums[index - 1] will be a new value.
            # Edge case, we can't compare [index - 2] when index is lower than 2.
            if index >= 2 and not (nums[index - 2] < nums[index]):
                nums[index] = nums[index - 1]
    return True


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `n - 1` elements in `nums` => O(n).
# ------------------------
# Auxiliary space: O(1)
# Only one BOOLean used => O(1).


test: list[int] = [1, 2, 10, 5, 7]
test_out: bool = True
assert test_out == can_be_increasing(test)

test = [2, 3, 1, 2]
test_out = False
assert test_out == can_be_increasing(test)

test = [1, 1, 1]
test_out = False
assert test_out == can_be_increasing(test)

test = [100, 21, 100]
test_out = True
assert test_out == can_be_increasing(test)

test = [randint(1, 1000) for _ in range(1000)]
print(test)
