# You are given an integer array nums.
# In one operation, you can add or subtract 1 from any element of nums.
# Return the minimum number of operations to make all elements of nums divisible by 3.
# ---------------------
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50


def minimum_operations(nums: list[int]) -> int:
    # working_sol (96.53%, 81.16%) -> (31ms, 16.48mb)  time: O(n) | space: O(1)
    out: int = 0
    # We only have 3 options:
    # num % 3 == 1 <- then we decrement it by 1
    # num % 3 == 2 <- then we increment it by 1
    # num % 3 == 0 <- then we do nothing
    for num in nums:
        if num % 3:
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ---------------------
# Auxiliary space: O(1)
# Only one constant INT `out` used => O(1).


test: list[int] = [1, 2, 3, 4]
test_out: int = 3
assert test_out == minimum_operations(test)

test = [3, 6, 9]
test_out = 0
assert test_out == minimum_operations(test)
