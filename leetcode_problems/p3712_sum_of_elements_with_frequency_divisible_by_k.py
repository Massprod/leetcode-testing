# You are given an integer array nums and an integer k.
# Return an integer denoting the sum of all elements in nums whose frequency
#  is divisible by k, or 0 if there are no such elements.
# Note: An element is included in the sum exactly as many times
#  as it appears in the array if its total frequency is divisible by k
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 100
from collections import Counter

from random import randint

from pyperclip import copy


def sum_divisible_by_k(nums: list[int], k: int) -> int:
    # working_solution: (100%, 100%) -> (0ms, 18.06mb)  Time: O(n) Space: O(n)
    frequencies: dict[int, int] = Counter(nums)
    
    out: int = 0
    for value, frequency in frequencies.items():
        out += value * frequency if 0 == (frequency % k) else 0
    
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# In the worst case there's only unique values in `nums`.
# Uses every value of the `nums`, twice => O(2 * n)
# --- --- --- ---
# Space complexity: O(n)
# `frequencies` <- allocates space for each unique value from `nums` => O(n).


test: list[int] = [1, 2, 2, 3, 3, 3, 3, 4]
test_k: int = 2
test_out: int = 16
assert test_out == sum_divisible_by_k(test, test_k)

test = [1, 2, 3, 4, 5]
test_k = 2
test_out = 0
assert test_out == sum_divisible_by_k(test, test_k)

test = [4, 4, 4, 1, 2, 3]
test_k = 3
test_out = 12
assert test_out == sum_divisible_by_k(test, test_k)

test = [randint(1, 100) for _ in range(100)]
copy(test)  # type: ignore
