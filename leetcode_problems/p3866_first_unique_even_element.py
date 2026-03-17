# You are given an integer array nums.
# Return an integer denoting the first even integer (earliest by array index)
#  that appears exactly once in nums. If no such integer exists, return -1.
# An integer x is considered even if it is divisible by 2.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from collections import Counter


def first_unique_even(nums: list[int]) -> int:
    # working_solution: (100%, 32.37%) -> (0ms, 19.32mb)  Time: O(n) Space: O(n)
    unique: dict[int, int] = Counter(nums)
    for value in nums:
        if not (value % 2) and 1 == unique.get(value, 2):
            return value
    
    return -1


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [3, 4, 2, 5, 4, 6]
test_out: int = 2
assert test_out == first_unique_even(test)

test = [4, 4]
test_out = -1
assert test_out == first_unique_even(test)
