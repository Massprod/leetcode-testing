# You are given a 0-indexed array nums of length n, consisting of non-negative integers.
# For each index i from 0 to n - 1, you must determine the size of the minimum sized
#  non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.
#  - In other words, let Bij be the bitwise OR of the subarray nums[i...j].
#  You need to find the smallest subarray starting at i, such that bitwise OR
#   of this subarray is equal to max(Bik) where i <= k <= n - 1.
# The bitwise OR of an array is the bitwise OR of all the numbers in it.
# Return an integer array answer of size n where answer[i] is the length
#  of the minimum sized subarray starting at i with maximum bitwise OR.
# A subarray is a contiguous non-empty sequence of elements within an array.
# ------------------------------
# n == nums.length
# 1 <= n <= 10 ** 5
# 0 <= nums[i] <= 10 ** 9
from random import randint

from pyperclip import copy


def smallest_subarrays(nums: list[int]) -> list[int]:
    # working_sol (33.86%, 29.13%) -> (990ms, 30.99mb)  time: O(n) | space: O(n)
    # We need a maximised value from the minimum array.
    # Maximum value, we can get is when `OR` doesnt change bits to `0`.
    # So, we only care about the `MSB` being further and not zeroed by other values.
    # ---
    out: list[int] = []
    # [ index of the furthest value of the `nums` from the left side,
    #  which have this `bit` set  ]
    bit_indexes: list[int] = [-1 for _ in range(32)]
    for index in range(len(nums) - 1, -1, -1):
        furthest_index: int = index
        # 10 ** 9 <= maximum `bin(val)` is going to have a 30 bits.
        for bit_ind in range(30):
            check_bit: int = 1 << bit_ind
            # `nums[index]` <- have this bit set, and we previously met the value
            #  on the index == `bit_indexes[bit_ind]`, which had this bit set as well.
            # So, we can guarantee that `bit_indexes[bit_ind]` is the furthest_index
            #  we can use to get the maximised value, so far.
            if 0 == nums[index] & check_bit:
                if -1 != bit_indexes[bit_ind]:
                    furthest_index = max(furthest_index, bit_indexes[bit_ind])
            # Otherwise, we can get the maximised value from the `nums[index]`,
            #  and it's index is the furthest we can use.
            else:
                bit_indexes[bit_ind] = index
        out.append(furthest_index - index + 1)  # +1 for 0-indexed
    # Reversed, because we were going backwads.
    return out[::-1]


# Time complexity: O(n) <- n - length of the input array `nums`.
# We're always traversing the whole input array `nums`, once.
# And for each index, we always check all the possible bit positions => O(n * 30).
# Extra reversing the `out` => O(n * 30 + n).
# ------------------------------
# Auxiliary space: O(n)
# `out` <- allocates space for each index of the `nums` => O(n).
# `bit_indexes` <- constant size array for 32 possible bits => O(n + 32)


test: list[int] = [1, 0, 2, 1, 3]
test_out: list[int] = [3, 3, 2 ,2, 1]
assert test_out == smallest_subarrays(test)

test = [1, 2]
test_out = [2, 1]
assert test_out == smallest_subarrays(test)

test = [randint(0, 10 ** 9) for _ in range(10 ** 5)]
copy(test)  # type: ignore
