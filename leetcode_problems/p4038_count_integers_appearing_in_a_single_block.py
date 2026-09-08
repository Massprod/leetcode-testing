# You are given an integer array nums.
# An integer x is special if all occurrences of x
#  in nums appear in a single contiguous block.
# Return the number of distinct special integers in nums.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from random import randint
from pyperclip import copy
from collections import defaultdict


def count_special_integers(nums: list[int]) -> int:
    # working_solution: (100%, 100%) -> (0ms, 18.88mb)  Time: O(n) Space: O(n)
    out: int = 0
    visited: dict[int, int] = defaultdict(int)
    visited[nums[0]] += 1
    prev: int = nums[0]
    for val in nums[1:]:
        if prev == val:
            continue
        visited[val] += 1
        prev = val
    for val, occurs in visited.items():
        if 1 == occurs:
            out += 1

    return out


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 2, 2, 1]
test_out: int = 1
assert test_out == count_special_integers(test)

test = [3, 3, 1, 2, 2, 1]
test_out = 2
assert test_out == count_special_integers(test)

test = [randint(1, 100) for _ in range(100)]
copy(test) # type: ignore
