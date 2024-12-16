# You are given a 0-indexed array of integers nums.
# A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1.
# In particular, the prefix consisting only of nums[0] is sequential.
# Return the smallest integer x missing from nums such that x is greater than
#  or equal to the sum of the longest sequential prefix.
# -------------------------
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
import pyperclip
from random import randint


def missing_integer(nums: list[int]) -> int:
    # working_sol: (100.00%, 31.29%) -> (0ms, 17.14mb)  time: O(n) | space: O(n)
    # Garbage wording in description.
    # We can only consider prefix from 0 -> i.
    # We don't need to consider any prefixes we can build after breaking sequence.
    # Neither any other starting points.
    # Just starts from 0 and end on any break index.
    present: set[int] = set(nums)
    stack: list[int] = [nums[0]]
    for index in range(1, len(nums)):
        cur_val: int = nums[index]
        if stack[-1] == (cur_val - 1):
           stack.append(cur_val)
        else:
            break
    out: int = sum(stack)
    while out in present:
        out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole `nums` to get `present` => O(n).
# Extra traversing every index of `nums` to get maximum 0 -> i prefix => O(n).
# In the worst case, every value from `nums` will collide with prefix sum.
# And we will increase it with `n` iterations => O(3 * n).
# -------------------------
# Auxiliary space: O(n)
# `present` <- allocates space for each value from `nums` => O(n).
# `stack` <- allocates space for each value from `nums` => O(2 * n).


test: list[int] = [1, 2, 3, 2, 5]
test_out: int = 6
assert test_out == missing_integer(test)

test = [3, 4, 5, 1, 12, 14, 13]
test_out = 15
assert test_out == missing_integer(test)

test = [randint(1, 50) for _ in range(50)]
pyperclip.copy(test)
