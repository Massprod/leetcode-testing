# You are given an integer array nums.
# Consider all pairs of distinct values x and y from nums such that:
#  - x < y
#  - x and y have different frequencies in nums.
# Among all such pairs:
#  - Choose the pair with the smallest possible value of x.
#  - If multiple pairs have the same x,
#    choose the one with the smallest possible value of y.
# Return an integer array [x, y]. If no valid pair exists, return [-1, -1].
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from collections import Counter
from random import randint
from pyperclip import copy


def min_distinct_freq_pair(nums: list[int]) -> list[int]:
    # working_solution: (100%, 88.86%) -> (0ms, 19.30mb)  Time: O(n * log n) Space: O(n)
    out: list[int] = [-1, -1]
    
    counts: dict[int, int] = Counter(nums)
    sorted_counts: list[int] = sorted(counts.keys())
    first_val: int = sorted_counts[0]
    first_occurs: int = counts[first_val]
    for index in range(1, len(sorted_counts)):
        second_val: int = sorted_counts[index]
        if not (first_val < second_val):
            continue
        second_occurs: int = counts[second_val]
        if first_occurs == second_occurs:
            continue
        out = [first_val, second_val]
        break
    
    return out


# Time complexity: O(n * log n)
# n - length of the input array `nums`
# ---
# In the worst case there's only unique values in `nums`.
# We will traverse and sort them => O(n * log n).
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 1, 2, 2, 3, 4]
test_out: list[int] = [1, 3]
assert test_out == min_distinct_freq_pair(test)

test = [1, 5]
test_out = [-1, -1]
assert test_out == min_distinct_freq_pair(test)

test = [7]
test_out = [-1, -1]
assert test_out == min_distinct_freq_pair(test)

test = [randint(1, 100) for _ in range(100)]
copy(test)  # type: ignore
