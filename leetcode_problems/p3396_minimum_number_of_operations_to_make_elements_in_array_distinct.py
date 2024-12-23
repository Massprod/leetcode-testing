# You are given an integer array nums.
# You need to ensure that the elements in the array are distinct.
# To achieve this, you can perform the following operation any number of times:
#  - Remove 3 elements from the beginning of the array.
#    If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements.
# Return the minimum number of operations needed to make the elements
#  in the array distinct.
# ---------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
import pyperclip
from random import randint
from collections import Counter


def minimum_operations(nums: list[int]) -> int:
    # working_sol: (100.00%, 100.00%) -> (7ms, 17.91mb)  time: O(n) | space: O(n)
    # { value: occurrences }
    all_vals: dict[int, int] = Counter(nums)
    over_limited: int = 0
    # How many values are not unique == we need to remove their occurrences.
    for val, count in all_vals.items():
        if 1 < count:
            over_limited += 1
    out: int = 0
    start: int = 0
    end: int = 2
    while over_limited and end < len(nums):
        for index in range(start, end + 1):
            val: int = nums[index]
            # Remove extra occurrences.
            if 1 < all_vals[val]:
                all_vals[val] -= 1
                if 1 == all_vals[val]:
                    over_limited -= 1
        out += 1
        start, end = start + 3, end + 3
    return out if not over_limited else out + 1


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array to get all values and their occurrences => O(n).
# Extra traversing every index of the array, to check if we deleted enougth => O(2 * n).
# ---------------------------
# Auxiliary space: O(n)
# In the worst case, every value is already unique in `nums`.
# `all_vals` <- allocates space for each unique value => O(n).


test: list[int] = [1, 2, 3, 4, 2, 3, 3, 5, 7]
test_out: int = 2

test = [4, 5, 6, 4, 4]
test_out = 2

test = [6, 7, 8, 9]
test_out = 0

test = [randint(1, 100) for _ in range(100)]
pyperclip.copy(test)
 