# You are given an integer array nums of even length.
# You have to split the array into two parts nums1 and nums2 such that:
#  - nums1.length == nums2.length == nums.length / 2.
#  - nums1 should contain distinct elements.
#  - nums2 should also contain distinct elements.
# Return true if it is possible to split the array,
#  and false otherwise.
# --------------------------
# 1 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100
from random import randint
from collections import defaultdict


def is_possible_to_split(nums: list[int]) -> bool:
    # working_sol (83.74%, 96.52%) -> (42ms, 16.34mb)  time: O(n) | space: O(n)
    # { value: # of occurrences }
    occurs: dict[int, int] = defaultdict(int)
    for num in nums:
        occurs[num] += 1
    duplicates: int = 0
    singles: int = 0
    for num, occur in occurs.items():
        if 2 < occur:
            return False
        elif 2 == occur:
            duplicates += 2
        else:
            singles += 1
    # we can spread them equally.
    if duplicates == len(nums):
        return True
    # We can use some duplicates, but we still need to cover a single values.
    return singles == len(nums) - duplicates


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, to get all occurrences => O(n).
# If every value is going to be unique, we're going to traverse them again => O(2 * n).
# --------------------------
# Auxiliary space: O(n).
# `occurs` <- allocates space for each unique value from `nums` => O(n).


test: list[int] = [1, 1, 2, 2, 3, 4]
test_out: bool = True
assert test_out == is_possible_to_split(test)

test = [1, 1, 1, 1]
test_out = False
assert test_out == is_possible_to_split(test)

test = [randint(1, 100) for _ in range(100)]
print(test)
