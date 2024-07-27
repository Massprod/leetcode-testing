# Given a zero-based permutation nums (0-indexed),
#  build an array ans of the same length where ans[i] = nums[nums[i]]
#  for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
# --------------------------
# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# The elements in nums are distinct.
# --------------------------
# Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?


def build_array(nums: list[int]) -> list[int]:
    # working_sol (99.58%, 94.14%) -> (80ms, 16.68mb)  time: O(n) | space: O(n)
    out: list[int] = [0 for _ in nums]
    for index in range(len(nums)):
        out[index] = nums[nums[index]]
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Traversing whole `num`, once to create `out` => O(n).
# Extra traversing whole `num` to get values in correct positions => O(2 * n).
# --------------------------
# Auxiliary space: O(n)
# `out` <- always of the same size as `nums` => O(n).


test: list[int] = [0, 2, 1, 5, 3, 4]
test_out: list[int] = [0, 1, 2, 4, 5, 3]
assert test_out == build_array(test)

test = [5, 0, 1, 2, 3, 4]
test_out = [4, 5, 0, 1, 2, 3]
assert test_out == build_array(test)
