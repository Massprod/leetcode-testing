# Given an integer array nums, return the number of elements that have both
#  a strictly smaller and a strictly greater element appear in nums.
# ----------------------------
# 1 <= nums.length <= 100
# -10 ** 5 <= nums[i] <= 10 ** 5
from collections import Counter
from random import randint


def count_elements(nums: list[int]) -> int:
    # working_sol (75.78%, 30.66%) -> (39ms, 16.56mb)  time: O(n * log n) | space: O(n)
    occurrences: dict[int, int] = Counter(nums)
    uniques: list[int] = sorted(occurrences.keys())
    out: int = 0
    if 2 >= len(uniques):
        return out
    for index in range(1, len(uniques) - 1):
        if uniques[index - 1] < uniques[index] < uniques[index + 1]:
            out += occurrences[uniques[index]]
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# In the worst case, every value in `nums` is unique.
# Always traversing it twice and sorting => O(n * log n + 2 * n).
# ----------------------------
# Auxiliary space: O(n)
# `occurrences` <- allocates space for every unique value from `nums` => O(n).
# `uniques` <- allocates space for every unique value from `nums`, as well => O(2 * n).


test: list[int] = [11, 7, 2, 15]
test_out: int = 2
assert test_out == count_elements(test)

test = [-3, 3, 3, 90]
test_out = 2
assert test_out == count_elements(test)

test = [randint(-10 ** 5, 10 ** 5) for _ in range(100)]
print(test)
