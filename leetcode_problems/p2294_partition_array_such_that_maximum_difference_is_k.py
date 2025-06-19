# You are given an integer array nums and an integer k.
# You may partition nums into one or more subsequences such that
#  each element in nums appears in exactly one of the subsequences.
# Return the minimum number of subsequences needed such that the difference
#  between the maximum and minimum values in each subsequence is at most k.
# A subsequence is a sequence that can be derived from another sequence
#  by deleting some or no elements without changing the order of the remaining elements.
# ------------------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 10 ** 5
# 0 <= k <= 10 ** 5
from random import randint

from pyperclip import copy


def partition_array(nums: list[int], k: int) -> int:
    # working_sol (41.24%, 73.61%) -> (93ms, 29.03mb)  time: O(n * log n) | space: O(n)
    # Dunno, about linear but linear-logarithmic is easy.
    # Sort, and take what we can. Because we can delete w.e we want =>
    # => dont care about ordering.
    out: int = 1
    # We can even alter `nums` in place, but it's a bad practice => extra space.
    order_nums: list[int] = sorted(nums)
    cur_min: int = order_nums[0]
    for value in order_nums:
        if value < cur_min:
            cur_min = value
        cur_diff: int = value - cur_min
        if cur_diff > k:
            out += 1
            cur_min = value
    
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting the input array `nums`, once => O(n * log n).
# Extra traversing sorted array, to get the subsequences => O((n * log n) + n).
# ------------------------
# Auxiliary space: O(n)
# `order_nums` <- allocates space for each value of the input array `nums` => O(n).


test: list[int] = [3, 6, 1, 2, 5]
test_k: int = 2
test_out: int = 2
assert test_out == partition_array(test, test_k)

test = [1, 2, 3]
test_k = 1
test_out = 2
assert test_out == partition_array(test, test_k)

test = [2, 2, 4, 5]
test_k = 0
test_out = 3
assert test_out == partition_array(test, test_k)

test = [randint(0, 10 ** 5) for _ in range(10 ** 5)]
copy(test)
