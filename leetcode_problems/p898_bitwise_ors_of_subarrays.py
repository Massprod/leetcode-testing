# Given an integer array arr, return the number of distinct bitwise ORs
#  of all the non-empty subarrays of arr.
# The bitwise OR of a subarray is the bitwise OR of each integer in the subarray.
# The bitwise OR of a subarray of one integer is that integer.
# A subarray is a contiguous non-empty sequence of elements within an array.
# ---------------------------
# 1 <= arr.length <= 5 * 10 ** 4
# 0 <= arr[i] <= 10 ** 9
from random import randint

from pyperclip import copy


def subarray_bitwise_ors(arr: list[int]) -> int:
    # working_sol (66.67%, 51.19%) -> (415ms, 44.86mb)  time: O(n * log w) | space: O(n)
    # Every value is the correct subarray by itself.
    out: set[int] = set(arr)
    # There's only 32 bit values. And the maximum len(current) is 32.
    current: set[int] = {0}
    for value in arr:
        # Expand on each step.
        current.add(value)
        # Check every value we met with the new one.
        current = {value | cur_val for cur_val in current}
        out |= current

    return len(out)


# Time complexity: O(n * log w) <- n - length of the input array `arr`,
#                                  w - maximum value size of the input array `arr`.
# Always traversing the whole input array `arr`, once => O(n).
# And for each index we check previously set bit values => O(n * log w).
# ---------------------------
# Auxiliary space: O(n)
# `current` <- holds 32 value at max => O(1).
# In the worst case, every index will give us unique value.
# `out` <- allocates space for each unique value => O(n).


test: list[int] = [0]
test_out: int = 1
assert test_out == subarray_bitwise_ors(test)

test = [1, 1, 2]
test_out = 3
assert test_out == subarray_bitwise_ors(test)

test = [1, 2, 4]
test_out = 6
assert test_out == subarray_bitwise_ors(test)

test = [randint(0, 10 ** 9) for _ in range(5 * 10 ** 4)]
copy(test)  # type: ignore
