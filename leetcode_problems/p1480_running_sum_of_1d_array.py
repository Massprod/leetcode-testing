# Given an array nums.
# We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# --------------------------
# 1 <= nums.length <= 1000
# -10 ** 6 <= nums[i] <= 10 ** 6


def running_sum(nums: list[int]) -> list[int]:
    # working_sol (91.48%, 67.09%) -> (35ms, 16.68mb)  time: O(n) | space: O(1)
    for index in range(1, len(nums)):
        nums[index] += nums[index - 1]
    return nums


# Time complexity: O(n) <- n - length of the input array `nums`.
# We always traverse `nums`, only once => O(n).
# --------------------------
# Auxiliary space: O(1)
# We reuse input array `nums`, and nothing extra is added => O(1).


test: list[int] = [1, 2, 3, 4]
test_out: list[int] = [1, 3, 6, 10]
assert test_out == running_sum(test)

test = [1, 1, 1, 1, 1]
test_out = [1, 2, 3, 4, 5]
assert test_out == running_sum(test)

test = [3, 1, 2, 10, 1]
test_out = [3, 4, 6, 16, 17]
assert test_out == running_sum(test)
