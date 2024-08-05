# We are given a list nums of integers representing a list compressed with run-length encoding.
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are freq elements with value val concatenated in a sublist.
# Concatenate all the sublists from left to right to generate the decompressed list.
# Return the decompressed list.
# --------------------------
# 2 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100
from random import randint


def decompress_rle_list(nums: list[int]) -> list[int]:
    # working_sol (87.76%, 36.44%) -> (48ms, 17.08mb)  time: O(n) | space: O(n)
    frequency: int
    value: int
    out: list[int] = []
    for index in range(0, len(nums), 2):
        frequency, value = nums[index], nums[index + 1]
        out += [value for _ in range(frequency)]
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always using every index in `nums`, once => O(n).
# --------------------------
# Auxiliary space: O(n)
# `out` <- always of the size `n // 2` => O(n // 2).


test: list[int] = [1, 2, 3, 4]
test_out: list[int] = [2, 4, 4, 4]
assert test_out == decompress_rle_list(test)

test = [1, 1, 2, 3]
test_out = [1, 3, 3]
assert test_out == decompress_rle_list(test)

test = [randint(1, 100) for _ in range(100)]
print(test)
