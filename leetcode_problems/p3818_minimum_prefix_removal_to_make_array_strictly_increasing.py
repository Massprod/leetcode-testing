# You are given an integer array nums.
# You need to remove exactly one prefix (possibly empty) from nums.
# Return an integer denoting the minimum length of the removed prefix
#  such that the remaining array is strictly increasing.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# -10 ** 9 <= nums[i] <= 10 ** 9
from random import randint
from pyperclip import copy


def minimum_prefix_length(nums: list[int]) -> int:
    # working_solution: (82.67%, 71.62%) -> (8ms, 34.40mb)  Time: O(n) Space: O(1)
    out: int = 0
    for index in range(len(nums) - 2, -1, -1):
        if nums[index] < nums[index + 1]:
            continue
        out = index + 1
        break

    return out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, -1, 2, 3, 3, 4, 5]
test_out: int = 4
assert test_out == minimum_prefix_length(test)

test = [4, 3, -2, -5]
test_out = 3
assert test_out == minimum_prefix_length(test)

test = [1, 2, 3, 4]
test_out = 0
assert test_out == minimum_prefix_length(test)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 5)]
copy(test)  # type: ignore
