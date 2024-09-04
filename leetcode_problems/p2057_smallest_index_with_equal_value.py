# Given a 0-indexed integer array nums, return the smallest index i
#  of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
# x mod y denotes the remainder when x is divided by y.
# -----------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 9


def smallest_equal(nums: list[int]) -> int:
    # working_sol (74.97%, 83.02%) -> (72ms, 16.48mb)  time: O(n) | space: O(1)
    for index in range(len(nums)):
        if (index % 10) == nums[index]:
            return index
    return -1


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# -----------------------
# Auxiliary space: O(1).
# Nothing extra is used.


test: list[int] = [0, 1, 2]
test_out: int = 0
assert test_out == smallest_equal(test)

test = [4, 3, 2, 1]
test_out = 2
assert test_out == smallest_equal(test)

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
test_out = -1
assert test_out == smallest_equal(test)
