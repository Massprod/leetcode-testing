# Given an array of integers nums and an integer k, an element nums[i]
#  is considered good if it is strictly greater than the elements at indices i - k
#  and i + k (if those indices exist).
# If neither of these indices exists, nums[i] is still considered good.
# Return the sum of all the good elements in the array.
# ---------------------------
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 1000
# 1 <= k <= floor(nums.length / 2)
from pyperclip import copy

from random import randint


def sum_of_good_numbers(nums: list[int], k: int) -> int:
    # working_sol (100.00%, 100.00%) -> (4ms, 17.72mb)  time: O(n) | space: O(1)
    out: int = 0
    for index, value in enumerate(nums):
        neg_diff: int = index - k
        pos_diff: int = index + k
        # If both indexes not exist == good.
        if (not 0 <= neg_diff < len(nums)
            and not 0 <= pos_diff < len(nums)):
            out += value
        # If one of them doesnt exist.
        elif (not 0 <= neg_diff < len(nums)
              or not 0 <= pos_diff < len(nums)):
            # We need to have value on index, higher than existing index == good.
            if (
                (0 <= neg_diff < len(nums)
                and nums[neg_diff] < nums[index])
                or
                (0 <= pos_diff < len(nums)
                and nums[pos_diff] < nums[index])
                ):
                out += value
        # If both indexes exists.
        # Both index values should be lower than existing index == good.
        elif (0 <= neg_diff < len(nums)
              and 0 <= pos_diff < len(nums)
              and nums[neg_diff] < nums[index]
              and nums[pos_diff] < nums[index]):
            out += value
    
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ---------------------------
# Auxiliary space: O(1).
# Only `3` constant INTs used, none of them depends on input => O(1).


test: list[int] = [1, 3, 2, 1, 5, 4]
test_k: int = 2
test_out: int = 12
assert test_out == sum_of_good_numbers(test, test_k)

test = [2, 1]
test_k = 1
test_out = 2
assert test_out == sum_of_good_numbers(test, test_k)

test = [randint(1, 1000) for _ in range(100)]
copy(test)
