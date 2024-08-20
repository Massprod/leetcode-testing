# You are given an array of integers nums.
# Return the length of the longest subarray of nums which
#  is either strictly increasing or strictly decreasing.
# --------------------
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
from random import randint


def longest_monotonic_subarray(nums: list[int]) -> int:
    # working_sol (92.89%, 96.36%) -> (40ms, 16.40mb)  time: O(n) | space: O(n)
    out: int = 0
    stack: list[int] = []
    # Strictly increasing
    for num in nums:
        if stack and stack[-1] < num:
            stack.append(num)
        else:
            out = max(out, len(stack))
            stack = [num]
    out = max(out, len(stack))
    stack = []
    # Strictly decreasing
    for num in nums:
        if stack and stack[-1] > num:
            stack.append(num)
        else:
            out = max(out, len(stack))
            stack = [num]
    out = max(out, len(stack))
    return out


# Time complexity: O(n) < - n - length of the input array `nums`.
# Always traversing whole `nums`, twice => O(2 * n).
# --------------------
# Auxiliary space: O(n)
# `stack` <- allocates space for every number from `nums` => O(n).


test: list[int] = [1, 4, 3, 3, 2]
test_out: int = 2
assert test_out == longest_monotonic_subarray(test)

test = [3, 3, 3, 3]
test_out = 1
assert test_out == longest_monotonic_subarray(test)

test = [3, 2, 1]
test_out = 3
assert test_out == longest_monotonic_subarray(test)

test = [randint(1, 50) for _ in range(50)]
print(test)
