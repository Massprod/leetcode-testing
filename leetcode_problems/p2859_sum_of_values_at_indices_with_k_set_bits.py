# You are given a 0-indexed integer array nums and an integer k.
# Return an integer that denotes the sum of elements in nums whose corresponding
#  indices have exactly k set bits in their binary representation.
# The set bits in an integer are the 1's present when it is written in binary.
# For example, the binary representation of 21 is 10101, which has 3 set bits.
# ------------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10 ** 5
# 0 <= k <= 10
from random import randint


def sum_indices_with_set_k_bits(nums: list[int], k: int) -> int:
    # working_sol (99.75%, 96.50%) -> (55ms, 16.57mb)  time: O(n) | space: O(1)
    out: int = 0
    for index, value in enumerate(nums):
        if index.bit_count() == k:
            out += value
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole `nums`, once => O(n).
# ------------------------
# Auxiliary space: O(1).


test: list[int] = [5, 10, 1, 5, 2]
test_k: int = 1
test_out: int = 13
assert test_out == sum_indices_with_set_k_bits(test, test_k)

test = [4, 3, 2, 1]
test_k = 2
test_out = 1
assert test_out == sum_indices_with_set_k_bits(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(1000)]
print(test)
