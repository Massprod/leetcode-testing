# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:
#  (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.
# A subsequence is an array that can be derived from another array by deleting some
#  or no elements without changing the order of the remaining elements.
# -----------------------------
# 2 <= nums.length <= 2 * 10 ** 5
# 1 <= nums[i] <= 10 ** 7
from random import randint

from pyperclip import copy


def maximum_length(nums: list[int]) -> int:
    # working_sol (38.76%, 99.22%) -> (99ms, 35.90mb)  time: O(n) | space: O(1)
    # E <= even | O <= odd
    # Sequences which satisfies us.
    # (E + E) % 2 == 0 ==> E -> E -> E -> E -> E ...
    # (O + O) % 2 == 0 ==> O -> O -> O -> O -> O ...
    # (E + O) % 2 == 1 ==> E -> O -> E -> O -> E ...
    # (O + E) % 2 == 1 ==> O -> E -> O -> E -> O ...
    # We can combine (E + O) and (O + E) sequences into One.
    out: int = 0
    even_start: int = -1
    odd_start: int = -1
    # Change every value to it's `parity`.
    # Because we don't care about values, we only care about the `parity`.
    e_sym: str = 'E'
    o_sym: str = 'O'
    for index, value in enumerate(nums):
        if value % 2:
            nums[index] = e_sym  # type: ignore
            if -1 == even_start:
                even_start = index
        else:
            nums[index] = o_sym  # type: ignore
            if -1 == odd_start:
                odd_start = index
    ee_seq: int = 1
    # (E + E)
    for index in range(even_start + 1, len(nums)):
        if e_sym == nums[index]:
            ee_seq += 1
    oo_seq: int = 1
    # (O + O)
    for index in range(odd_start + 1, len(nums)):
        if o_sym == nums[index]:
            oo_seq += 1
    alt_seq: int = 1
    alt_start: int = min(odd_start, even_start)
    odd_target: bool = e_sym == nums[alt_start]
    # (E + O) | (O + E)
    for index in range(alt_start + 1, len(nums)):
        if odd_target and o_sym == nums[index]:
            alt_seq += 1
            odd_target = not odd_target
        elif not odd_target and e_sym == nums[index]:
            alt_seq += 1
            odd_target = not odd_target

    out = max(ee_seq, oo_seq, alt_seq)
    return out if out != 1 else 0


# Time complexity: O(n) <- n - length of the input array `nums`.
# In the worst case we're starting loops from 0 and 1 indexes.
# Always traversing the whole input array `nums`, 4 times => O(4 * n).
# -----------------------------
# Auxiliary space: O(1)
# We're reusing `nums` with changed values, and everything else is constant => O(1).


test: list[int] = [1, 2, 3, 4]
test_out: int = 4
assert test_out == maximum_length(test)

test = [1, 2, 1, 1, 2, 1, 2]
test_out = 6
assert test_out == maximum_length(test)

test = [1, 3]
test_out = 2
assert test_out == maximum_length(test)

test = [randint(1, 10 ** 7) for _ in range(2 * 10 ** 5)]
copy(test)
