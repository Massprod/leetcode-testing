# You are given a 0-indexed array nums and a non-negative integer k.
# In one operation, you can do the following:
#  - Choose an index i that hasn't been chosen before from the range [0, nums.length - 1].
#  - Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].
# The beauty of the array is the length of the longest subsequence consisting of equal elements.
# Return the maximum possible beauty of the array nums after applying the operation any number of times.
# Note that you can apply the operation to each index only once.
# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none)
#  without changing the order of the remaining elements.
# ---------------------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i], k <= 10 ** 5
import pyperclip
from random import randint


def maximum_beauty(nums: list[int], k: int) -> int:
    # working_sol: (46.58%, 45.21%) -> (233ms, 27.95mb)  time: O(n * log n) | space: O(n)
    # After sorting, all of the closes values are going to be as close as possible.
    # And after that, we essentially just want to get subarray with first and last element being in range
    # [(first + k), (last - k)] => [last - first <= k + k]
    # Because everything before `last` is 100% smaller and we have range for that values == value - k.
    # And everything after `first` is 100% bigger and we have range for that values == value + k.
    # So, now it's just a sliding_window to get this subarray :)
    sorted_nums: list[int] = sorted(nums)
    left: int = 0
    right: int = -1
    range_limit: int = k + k
    
    out: int = 1
    while right < len(sorted_nums) - 1:
        right += 1
        while (sorted_nums[right] - sorted_nums[left]) > range_limit and left < right:
            left += 1
        out = max(out, (right - left) + 1)  # +1 for 0-indexed
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting input array `nums` => O(n * log n).
# Extra traversing sorted array to get the correct window => O((n * log n) + n).
# ---------------------------
# Auxiliary space: O(n)
# `sorted_nums` <- allocates space for each value from `nums` => O(n).


test: list[int] = [4, 6, 1, 2]
test_k: int = 2
test_out: int = 3
assert test_out == maximum_beauty(test, test_k)

test = [1, 1, 1, 1]
test_k = 10
test_out = 4
assert test_out == maximum_beauty(test, test_k)

test = [randint(0, 10 ** 5) for _ in range(10 ** 3)]
pyperclip.copy(test)
