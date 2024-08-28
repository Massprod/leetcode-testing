# You are given an array nums, where each number in the array appears either once or twice.
# Return the bitwise XOR of all the numbers that appear twice in the array,
#  or 0 if no number appears twice.
# ---------------------------
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
# Each number in nums appears either once or twice.
from collections import Counter


def duplicate_numbers_xor(nums: list[int]) -> int:
    # working_sol (94.66%, 30.30%) -> (39ms, 16.52mb)  time: O(n) | space: O(n)
    out: int = 0
    # { value: # of occurrences }
    occurs: dict[int, int] = Counter(nums)
    for value, occurrence in occurs.items():
        if 2 <= occurrence:
            out ^= value
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums`, once => O(n).
# In the worst case there's only unique values.
# Extra traversing every value as keys in `occurs` => O(2 * n).
# ---------------------------
# Auxiliary space: O(n)
# `occurs` <- allocates space for each unique value from `nums` => O(n).


test: list[int] = [1, 2, 1, 3]
test_out: int = 1
assert test_out == duplicate_numbers_xor(test)

test = [1, 2, 3]
test_out = 0
assert test_out == duplicate_numbers_xor(test)

test = [1, 2, 2, 1]
test_out = 3
assert test_out == duplicate_numbers_xor(test)
