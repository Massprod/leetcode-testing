# You are given an integer array nums.
# Return an integer denoting the first element (scanning from left to right)
#  in nums whose frequency is unique. That is, no other integer appears
#  the same number of times in nums. If there is no such element, return -1.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5
from pyperclip import copy
from random import randint
from collections import Counter


def first_unique_freq(nums: list[int]) -> int:
    # working_solution: (96.60%, 22.76%) -> (137ms, 41.64mb)  Time: O(n) Space: O(n)
    # Values occurrences.
    val_occurs: dict[int, int] = Counter(nums)
    # Count of each occurrence
    occur_occurs: dict[int, int] = Counter(val_occurs.values())
    unique: list[int] = [
        key for key, value in occur_occurs.items() if value == 1
    ]
    if not unique:
        return -1
    unique_occur: int = unique[0]
    for num in nums:
        if val_occurs[num] == unique_occur:
            return num

    return -1


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [20, 10, 30, 30]
test_out: int = 30
assert test_out == first_unique_freq(test)

test = [20, 20, 10, 30, 30, 30]
test_out = 20
assert test_out == first_unique_freq(test)

test = [10, 10, 20, 20]
test_out = -1
assert test_out == first_unique_freq(test)

test = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
copy(test)  # type: ignore
