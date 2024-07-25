# You are given an integer array nums (0-indexed).
# In one operation, you can choose an element of the array and increment it by 1.
#  - For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.
# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
# An array of length 1 is trivially strictly increasing.
# ------------------
# 1 <= nums.length <= 5000
# 1 <= nums[i] <= 10 ** 4
from random import randint


def min_operations(nums: list[int]) -> int:
    # working_sol (93.03%, 86.32%) -> (94ms, 17.17mb)  time: O(n) | space: O(1)
    out: int = 0
    for index in range(1, len(nums)):
        if nums[index - 1] >= nums[index]:
            diff: int = nums[index - 1] - nums[index]
            nums[index] += diff + 1
            out += diff + 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing every index of `nums`, once => O(n).
# ------------------
# Auxiliary space: O(1)
# Only one constant INT used => O(1).


test: list[int] = [1, 1, 1]
test_out: int = 3
assert test_out == min_operations(test)

test = [1, 5, 2, 4, 1]
test_out = 14
assert test_out == min_operations(test)

test = [8]
test_out = 0
assert test_out == min_operations(test)

test = [randint(1, 10 ** 4) for _ in range(5_000)]
print(test)
