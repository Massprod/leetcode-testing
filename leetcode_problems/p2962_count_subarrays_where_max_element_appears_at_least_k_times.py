# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums
#  appears at least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.
# -----------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 6
# 1 <= k <= 10 ** 5
from random import randint


def count_subarrays(nums: list[int], k: int) -> int:
    # working_sol (69.08%, 80.15%) -> (867ms, 30.89mb)  time: O(n) | space: O(1)
    out: int = 0
    left_l: int = 0
    right_l: int = 0
    max_elem: int = max(nums)
    occurs: int = 0
    # Every value from 0 -> left_l will give us 1 subarray.
    # And because we're always placing left_l on +1 index of pre_last max_element,
    #  we don't need +1 for 0 indexed.
    while right_l < len(nums):
        if nums[right_l] == max_elem:
            occurs += 1
        while occurs == k:
            if nums[left_l] == max_elem:
                occurs -= 1
            left_l += 1
        out += left_l
        right_l += 1
    return out


# Time complexity: O(n) <- n - length of an input array `nums`.
# Standard sliding window, in the worst case, we will use every Index only Twice => O(2n).
# -----------------------
# Auxiliary space: O(1)
# Only 5 constant INT's used.


test: list[int] = [1, 3, 2, 3, 3]
test_k: int = 2
test_out: int = 6
assert test_out == count_subarrays(test, test_k)

test = [1, 4, 2, 1]
test_k = 3
test_out = 0
assert test_out == count_subarrays(test, test_k)

test = [4, 3, 7, 10, 2, 10, 1, 6, 10, 7, 10, 10, 9, 8, 3]
test_k = 3
test_out = 50
assert test_out == count_subarrays(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(10 ** 3)]
print(test)
