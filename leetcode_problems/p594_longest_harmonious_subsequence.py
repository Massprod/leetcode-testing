# We define a harmonious array as an array
#  where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence
#  among all its possible subsequences.
# A subsequence of array is a sequence that can be derived from the array
#  by deleting some or no elements without changing the order of the remaining elements.
# ------------------------------
# 1 <= nums.length <= 2 * 10 ** 4
# -10 **9 <= nums[i] <= 10 ** 9
from collections import Counter
from random import randint


def find_lhs(nums: list[int]) -> int:
    # working_sol (81.45%, 54.25%) -> (229ms, 18.33mb)  time: O(n) | space: O(n)
    # {value: occurrences}
    count: dict[int, int] = Counter(nums)
    out: int = 0
    for num in count:
        f_sequence: int = 0
        if (num - 1) in count:
            f_sequence = count[num] + count[num - 1]
        s_sequence: int = 0
        if (num + 1) in count:
            s_sequence = count[num] + count[num + 1]
        out = max(out, f_sequence, s_sequence)
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# We're always traversing `num` once to get all the unique values and their occurrences => O(n).
# ------------------------------
# Auxiliary space: O(n)
# Worst case: all the values from `nums` are unique.
# All the unique values are stored in `count` and assigned INT as value => O(n).


test: list[int] = [1, 3, 2, 2, 5, 2, 3, 7]
test_out: int = 5
assert test_out == find_lhs(test)

test = [1, 2, 3, 4]
test_out = 2
assert test_out == find_lhs(test)

test = [1, 1, 1, 1]
test_out = 0
assert test_out == find_lhs(test)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 4)]
print(test)
