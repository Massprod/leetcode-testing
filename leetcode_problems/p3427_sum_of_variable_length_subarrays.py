# You are given an integer array nums of size n.
# For each index i where 0 <= i < n, define a subarray 
#  nums[start ... i] where start = max(0, i - nums[i]).
# Return the total sum of all elements from the subarray defined
#  for each index in the array.
# -----------------------
# 1 <= n == nums.length <= 100
# 1 <= nums[i] <= 1000
import pyperclip
from random import randint


def subarray_sum(nums: list[int]) -> int:
    # working_sol (94.87%, 78.57%) -> (2ms, 17.80mb)  time: O(n) | space: O(n)
    prefix: int = 0
    prefixes: list[int] = [prefix]
    for num in nums:
        prefix += num
        prefixes.append(prefix)
    out: int = 0
    # nums[start ... index] <- start = max(0, index - nums[index])
    for index in range(len(nums)):
        start: int = max(0, index - nums[index])
        out += (
            (prefixes[index] - prefixes[start]) + nums[index]
        )

    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, twice => O(2 * n).
# -----------------------
# Auxiliary space: O(n)
# `prefixes` <- allocates space for each index of `nums`, and extra 1 => O(n + 1).


test: list[int] = [2, 3, 1]
test_out: int = 11
assert test_out == subarray_sum(test)

test = [3, 1, 1, 2]
test_out = 13
assert test_out == subarray_sum(test)

test = [randint(1, 1000) for _ in range(100)]
pyperclip.copy(test)
