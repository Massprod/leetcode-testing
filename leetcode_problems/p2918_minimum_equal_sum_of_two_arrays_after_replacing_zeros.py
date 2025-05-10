# You are given two arrays nums1 and nums2 consisting of positive integers.
# You have to replace all the 0's in both arrays with strictly positive integers
#  such that the sum of elements of both arrays becomes equal.
# Return the minimum equal sum you can obtain, or -1 if it is impossible.
# ---------------------------
# 1 <= nums1.length, nums2.length <= 10 ** 5
# 0 <= nums1[i], nums2[i] <= 10 ** 6
from random import randint

from pyperclip import copy


def min_sum(nums1: list[int], nums2: list[int]) -> int:
    # working_sol (70.86%, 5.19%) -> (845ms, 37.31mb)  time: O(n + m) | space: O(1)
    # The best approach is to take currently maximum sum from both arrays.
    # Switch all 0's to 1's and add sum of the added 1's to 0's in the other array.
    sum1: int = 0
    zero1: int = 0
    for val in nums1:
        if 0 == val:
            zero1 += 1
            # Flip all 0's to 1's by default => gives us minimum sum.
            sum1 += 1
        else:
            sum1 += val
    
    sum2: int = 0
    zero2: int = 0
    for val in nums2:
        if 0 == val:
            zero2 += 1
            sum2 += 1
        else:
            sum2 += val

    if sum1 == sum2:
        return sum1
    elif sum1 > sum2:
        # We need 0's in the `nums2` to replace and cover difference.
        # And extra we need +1 for each 0's in sum1.
        # So, if there's no 0's in `nums2` => -1.
        if 0 == zero2:
            return -1
        return sum1
    elif sum1 < sum2:
        # Same logic.
        if 0 == zero1:
            return -1
        return sum2
    
    return -1


# Time complexity: O(n + m) <- n - length of the input array `nums1`,
#                              m - length of the input array `nums2`.
# Always traversing both input arrays, once => O(n + m).
# ---------------------------
# Auxiliary space: O(1).


test_1: list[int] = [3, 2, 0, 1, 0]
test_2: list[int] = [6, 5, 0]
test_out: int = 12
assert test_out == min_sum(test_1, test_2)

test_1 = [2, 0, 2, 0]
test_2 = [1, 4]
test_out = -1
assert test_out == min_sum(test_1, test_2)

test_1 = [0, 16, 28, 12, 10, 15, 25, 24, 6, 0, 0]
test_2 = [20, 15, 19, 5, 6, 29, 25, 8, 12]
test_out = 139
assert test_out == min_sum(test_1, test_2)

test_1 = [randint(1, 10 ** 6) for _ in range(10 ** 5)]
copy(test_1)
