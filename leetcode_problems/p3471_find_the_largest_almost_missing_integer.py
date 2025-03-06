# You are given an integer array nums and an integer k.
# An integer x is almost missing from nums if x appears
#  in exactly one subarray of size k within nums.
# Return the largest almost missing integer from nums.
# If no such integer exists, return -1.
# A subarray is a contiguous sequence of elements within an array.
# ---------------------------
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 1 <= k <= nums.length
from collections import defaultdict

from random import randint

from pyperclip import copy


def largest_integer(nums: list[int], k: int) -> int:
    # working_sol (81.63%, 94.81%) -> (3ms, 17.68mb)  time: O(n * k + n ) | space: O(n)
    # All we care about is window of size `k`.
    # And elements which appeared in such windows only 1 time.
    out: int = -1
    count: dict[int, int] = defaultdict(int)
    left_l: int = 0
    right_l: int = k
    cur_window: dict[int, int] = defaultdict(int)
    for index in range(left_l, right_l):
        cur_window[nums[index]] += 1
    for unique in cur_window:
        count[unique] += 1
    while right_l < len(nums):
        cur_window[nums[left_l]] -= 1
        if 0 == cur_window[nums[left_l]]:
            cur_window.pop(nums[left_l])
        left_l += 1
        cur_window[nums[right_l]] += 1
        right_l += 1
        for unique in cur_window:
            count[unique] += 1

    for key, value in count.items():
        if 1 == value:
            out = max(key, out)
    
    return out


# Time complexity: O(n * k + n) <- n - length of the input array `nums`.
# We're always start a new window from each index of the input array `nums`.
# In the worst case every window is going to have unique value,
#  `cur_window` will allocate space for `k` values and we loop them on each index => O(n * k).
# In the worst case every value in `nums` is unique, so we extra loop `n` to check
#  for desired option => O(n * k + n)) => O(n * k + n).
# ---------------------------
# Auxiliary space: O(n)
# In the worst case `k` == len(nums), and all values are unique.
# `cur_window` <- allocates space for each value from `nums` => O(n).
# `count` <- allocates space for each unique value from `nums` => O(2 * n).


test: list[int] = [0, 0]
test_k: int = 1
test_out: int = -1
assert test_out == largest_integer(test, test_k)

test = [3, 9, 2, 1, 7]
test_k = 3
test_out = 7
assert test_out == largest_integer(test, test_k)

test = [3, 9, 7, 2, 1, 7]
tet_k = 4
test_out = 3
assert test_out == largest_integer(test, test_k)

test = [randint(0, 50) for _ in range(50)]
copy(test)
