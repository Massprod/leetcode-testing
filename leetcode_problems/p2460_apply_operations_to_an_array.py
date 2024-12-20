# You are given a 0-indexed array nums of size n consisting of non-negative integers.
# You need to apply n - 1 operations to this array where, in the ith operation (0-indexed),
#  you will apply the following on the ith element of nums:
#  - If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0.
#    Otherwise, you skip this operation.
# After performing all the operations, shift all the 0's to the end of the array.
#  - For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
# Return the resulting array.
# Note that the operations are applied sequentially, not all at once.
# ------------------------
# 2 <= nums.length <= 2000
# 0 <= nums[i] <= 1000
import pyperclip
from random import randint


def apply_operations(nums: list[int]) -> list[int]:
    # working_sol: (100.00%, 9.19%) -> (0ms, 17.79mb)  time: O(n) | space: O(n)
    values: list[int] = []
    limit: int = len(nums) - 1

    for index in range(len(nums)):
        # `0` <- we don't care
        if 0 != nums[index]:
            if index < limit and nums[index + 1] == nums[index]:
                values.append(nums[index] * 2)
                nums[index + 1] = 0
            else:
                values.append(nums[index])
    return values + [0 for _ in range(len(nums) - len(values))]


# Time complexity: O(n) <- n - length of the input array `nums`
# Always traversing whole input array `nums`, once => O(n).
# `len(values)` + zeroes to add is always equal to `n`.
# Extra traversing all `values` and populatin with `0` => O(n).
# ------------------------
# Auxiliary space: O(n)
# In the worst case there's no equal values and zeroes.
# `values` <- allocates space for each valur from `nums` => O(n).
# `out` <- is also going to be of size `n` => O(2 *n).


test: list[int] = [1, 2, 2, 1, 1, 0]
test_out: list[int] = [1, 4, 2, 0, 0, 0]
assert test_out == apply_operations(test)

test = [0, 1]
test_out: list[int] = [1, 0]
assert test_out == apply_operations(test)

test = [randint(0, 1000) for _ in range(2000)]
pyperclip.copy(test)
