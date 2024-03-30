# You are given an integer array nums and an integer k.
# The frequency of an element x is the number of times it occurs in an array.
# An array is called good if the frequency of each element in this array is less than or equal to k.
# Return the length of the longest good subarray of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.
# -------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# 1 <= k <= nums.length
from random import randint
from collections import defaultdict


def max_subarray_length(nums: list[int], k: int) -> int:
    # working_sol (50.80%, 7.01%) -> (1163ms, 32.18mb)  time: O(n) | space: O(n)
    out: int = 0
    # {integer: occurrences}
    window: dict[int, int] = defaultdict(int)
    # Maximum occurrences of 'cur_max_int'
    cur_max_oc: int = 0
    # Integer, which occurs the most, used as a key.
    cur_max_int: int = 0
    # Standard sliding window.
    left_l: int = 0
    right_l: int = 0
    while right_l != len(nums):
        cur_int: int = nums[right_l]
        window[cur_int] += 1
        # New value which occurs more than the previous one.
        if cur_max_oc < window[cur_int]:
            cur_max_int = cur_int
            cur_max_oc = window[cur_int]
        # Shrink, until a window exists or k < current max occurrences.
        while left_l <= right_l and cur_max_oc > k:
            del_int: int = nums[left_l]
            if del_int == cur_max_int:
                cur_max_oc -= 1
            window[del_int] -= 1
            left_l += 1
        out = max(out, (right_l - left_l) + 1)  # +1 for 0-indexed.
        right_l += 1
    return out


# Time complexity: O(n) <- n - length of an input array `nums`.
# The worst case, every value is more than `k`. So, we will use every index Twice => O(2n).
# -------------------------
# Auxiliary space: O(n)
# The worst case, every value is Unique, and we will store them all in `window' as unique Keys.


test: list[int] = [1, 2, 3, 1, 2, 3, 1, 2]
test_k: int = 2
test_out: int = 6
assert test_out == max_subarray_length(test, test_k)

test = [1, 2, 1, 2, 1, 2, 1, 2]
test_k = 1
test_out = 2
assert test_out == max_subarray_length(test, test_k)

test = [5, 5, 5, 5, 5, 5, 5]
test_k = 4
test_out = 4
assert test_out == max_subarray_length(test, test_k)

test = [randint(1, 10 ** 9) for _ in range(10 ** 3)]
print(test)
print(randint(1, 1000))
