# You are given an integer array nums of size n.
# Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
#  - In other words, let k be the maximum value of the bitwise
#   AND of any subarray of nums.
# Then, only subarrays with a bitwise AND equal to k should be considered.
# Return the length of the longest such subarray.
# The bitwise AND of an array is the bitwise AND of all the numbers in it.
# A subarray is a contiguous sequence of elements within an array.
# --------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 6
from random import randint

from pyperclip import copy


def longest_subarray(nums: list[int]) -> int:
    # working_sol (96.45%, 84.62%) -> (17ms, 30.56mb)
    # Bitwise `AND` is always going to make any value lower,
    #  except for the values with the same `MSB` == leftMost.
    # And the further placed `MSB` => higher the value.
    # So, essentially we only care about the highest value of the array.
    # Because, `subarray` `AND` should be equal to the whole `nums` `AND`.
    out: int = 0
    cur_sub: int = 0
    max_value: int = max(nums)
    for value in nums:
        if value == max_value:
            cur_sub += 1
        else:
            out = max(out, cur_sub)
            cur_sub = 0

    # We can have the last index unchecked.
    return max(out, cur_sub)


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing the whole input array `nums`, once => O(n).
# --------------------------
# Auxiliary space: O(1)


test: list[int] = [1, 2, 3, 3, 2, 2]
test_out: int = 2
assert test_out == longest_subarray(test)

test = [1, 2, 3, 4]
test_out = 1
assert test_out == longest_subarray(test)

test = [randint(1, 10 ** 6) for _ in range(10 ** 5)]
copy(test)  # type: ignore
