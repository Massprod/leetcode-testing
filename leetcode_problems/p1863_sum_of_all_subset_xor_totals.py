# The XOR total of an array is defined as the bitwise XOR of all its elements,
#  or 0 if the array is empty.
#  - For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums.
# Note: Subsets with the same elements should be counted multiple times.
# An array a is a subset of an array b if a can be obtained from b
#  by deleting some (possibly zero) elements of b.
# ------------------------------
# 1 <= nums.length <= 12
# 1 <= nums[i] <= 20
from random import randint


def subset_xor_sum(nums: list[int]) -> int:
    # working_sol (76.70%, 84.04%) -> (42ms, 16.46mb)  time: O(2 ** n) | space: O(n)

    def check(index: int, path: int) -> int:
        if index >= len(nums):
            return path
        we_xor: int = check(index + 1, nums[index] ^ path)
        we_dont: int = check(index + 1, path)
        # ! return the sum of all XOR totals for every subset of nums !
        return we_xor + we_dont

    return check(0, 0)


# Time complexity: O(2 ** n) <- n - length of an input array `nums`.
# Standard BT with 2 options and max depth == `n` => O(2 ** n).
# ------------------------------
# Auxiliary space: O(n)
# Maximum depth == `n` == recursion stack will hold at max `n` => O(n).


test: list[int] = [1, 3]
test_out: int = 6
assert test_out == subset_xor_sum(test)

test = [5, 1, 6]
test_out = 28
assert test_out == subset_xor_sum(test)

test = [3, 4, 5, 6, 7, 8]
test_out = 480
assert test_out == subset_xor_sum(test)

test = [randint(1, 20) for _ in range(12)]
print(test)
