# You are given a 0-indexed integer array mapping which represents the mapping rule
#  of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.
# The mapped value of an integer is the new integer obtained by replacing each occurrence
#  of digit i in the integer with mapping[i] for all 0 <= i <= 9.
# You are also given another integer array nums.
# Return the array nums sorted in non-decreasing order based on the mapped values of its elements.
# Notes:
#   - Elements with the same mapped values should appear in the same relative order as in the input.
#   - The elements of nums should only be sorted based on their mapped values and not be replaced by them.
# -----------------------------
# mapping.length == 10
# 0 <= mapping[i] <= 9
# All the values of mapping[i] are unique.
# 1 <= nums.length <= 3 * 10 ** 4
# 0 <= nums[i] < 10 ** 9
from random import randint, shuffle


def sort_jumbled(mapping: list[int], nums: list[int]) -> list[int]:
    # working_sol (88.31%, 13.64%) -> (930ms, 27.7mb)  time: O(n * log n) | space: O(n)
    # Rebuild and sort is simple, but we need Tiebreaker for the same values.
    # And because we need to save relative order from original `nums`, we need (new_val, orig_index).
    # (converted_version, orig_index)
    new_order: list[tuple[int, int]] = []
    # {orig_value: converted_version} <- We allowed duplicates, so we can reuse.
    converted: dict[int, int] = {}
    for index, val in enumerate(nums):
        new_val: int = 0
        if val in converted:
            new_order.append((converted[val], index))
            continue
        for digit in str(val):
            new_val *= 10
            new_val += mapping[int(digit)]
        new_order.append((new_val, index))
        converted[val] = new_val
    new_order.sort()
    new_nums: list[int] = [nums[index] for val, index in new_order]
    return new_nums


# Time complexity: O(n * log n) <- n - length of input array `nums`.
# Worst case: every value in `nums` is unique.
# We rebuild all values in `nums` => O(n).
# Because every value is unique, their rebuild versions should be as well.
# So, we will sort() same number of values in `new_order` => O(n * log n).
# We traverse `new_order` again to get original values in desired order => O(n).
# O(2 * n + n * log n).
# -----------------------------
# Auxiliary space: O(n)
# With the same worst case `new_order` will have all unique values => O(n).
# Extra to this `converted` will have all original values from `nums` stored => O(n).
# Because we can have duplicates, it's not a bad idea to cull some recalc, even if they're fast.
# Standard sort() will also take O(n).
# And `new_nums` is just a sorted version of original `nums` => O(n).
# Extra we have 1 extras INT `new_val` which doesn't depend on input, and `str(val)`.
# `str(val)` will have max_size of 10 symbols (0 <= nums[i] < 10 ** 9), which is somewhat constant. So ignore it :)
# O(4n).


test: list[int] = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
test_nums: list[int] = [991, 338, 38]
test_out: list[int] = [338, 38, 991]
assert test_out == sort_jumbled(test, test_nums)

test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_nums = [789, 456, 123]
test_out = [123, 456, 789]
assert test_out == sort_jumbled(test, test_nums)

shuffle(test)
test_nums = [randint(0, 10 ** 9) for _ in range(3 * 10 ** 4)]
print(test)
print('!!!!!!!!!!!!===')
print(test_nums)
