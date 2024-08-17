# You are given a non-negative integer array nums.
# In one operation, you must:
#  - Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
#  - Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.
# -----------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
from random import randint


def minimum_operations(nums: list[int]) -> int:
    # working_sol (86.25%, 35.07%) -> (33ms, 16.50mb)  time: O(n) | space: O(n)
    # No matter the case, we will always take some part of higher values.
    # And if they're not equal to the current min, we will get another min to delete.
    # So, we just delete minimum values, while we can.
    out: set[int] = set(nums)
    if 0 in out:
        out.remove(0)
    return len(out)


# Time complexity: O(n) <- n - length of the input array `nums`
# Always traversing `nums` to get all unique values from it => O(n).
# -----------------------
# Auxiliary space: O(n)
# In the worst case there's only unique values in `nums`.
# `out` <- allocates space for every unique value from `nums` => O(n).


test: list[int] = [1, 5, 0, 3, 5]
test_out: int = 3
assert test_out == minimum_operations(test)

test = [0]
test_out = 0
assert test_out == minimum_operations(test)

test = [randint(0, 100) for _ in range(100)]
print(test)
