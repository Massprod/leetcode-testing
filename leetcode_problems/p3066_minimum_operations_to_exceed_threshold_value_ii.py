# You are given a 0-indexed integer array nums, and an integer k.
# In one operation, you will:
#  - Take the two smallest integers x and y in nums.
#  - Remove x and y from nums.
#  - Add min(x, y) * 2 + max(x, y) anywhere in the array.
# Note that you can only apply the described operation
#  if nums contains at least two elements.
# Return the minimum number of operations needed so that all elements
#  of the array are greater than or equal to k.
# -------------------------
# 2 <= nums.length <= 2 * 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# 1 <= k <= 10 ** 9
# The input is generated such that an answer always exists.
# That is, there exists some sequence of operations after which all elements
#  of the array are greater than or equal to k
import heapq

from random import randint

from pyperclip import copy


def min_operations(nums: list[int], k: int) -> int:
    # working_sol (64.29%, 91.60%) -> (221ms, 35.32mb)  time: O(n * log n) | space: O(n)
    _1val: int
    _2val: int

    out: int = 0
    heapq.heapify(nums)
    while (2 <= len(nums)
           and k > nums[0]):
        # _1val <= _2val <- always stands
        _1val, _2val = heapq.heappop(nums), heapq.heappop(nums)
        new_val: int = _1val * 2 + _2val
        heapq.heappush(
            nums, new_val
        )
        out += 1

    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Creating a heap => O(n * log n).
# We're always taking 2 values from `nums`, and returning only one.
# So, even in the case: [1, 1, 1, 1, 1] k = 10000.
# We will just use every element of `nums` and extra half.
# Should be correct to say => O(n * log n).
# -------------------------
# Auxiliary space: O(n)
# `heap` <- will allocates space for each element of `nums` => O(n).


test: list[int] = [2, 11, 10, 1, 3]
test_k: int = 10
test_out: int = 2
assert test_out == min_operations(test, test_k)

test = [1, 1, 2, 4, 9]
test_k = 20
test_out = 4
assert test_out == min_operations(test, test_k)

test = [randint(1, 10 ** 9) for _ in range(2 * 10 ** 5)]
copy(test)
test_k = randint(1, 10 ** 9)
print(test_k)
