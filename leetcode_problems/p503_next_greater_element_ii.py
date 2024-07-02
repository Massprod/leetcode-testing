# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
#  return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array,
#  which means you could search circularly to find its next greater number.
# If it doesn't exist, return -1 for this number.
# -------------------------
# 1 <= nums.length <= 10 ** 4
# -10 ** 9 <= nums[i] <= 10 ** 9
from random import randint


def next_greater_elements(nums: list[int]) -> list[int]:
    # working_sol (70.59%, 99.15%) -> (148ms, 17.95mb)  time: O(n) | space: O(n)
    # ! -10 ** 9 <= nums[i] <= 10 ** 9 !
    min_pos: int = (-10 ** 9) - 10
    stack: list[int] = []
    out: list[int] = [min_pos] * len(nums)
    # The Most important part is that we can't travel (RIGHT -> LEFT).
    for index in range(len(nums)):
        # First higher => record.
        while stack and nums[stack[-1]] < nums[index]:
            out[stack.pop()] = nums[index]
        stack.append(index)
    # We always should go in a cycle and check for the higher values again.
    for index in range(len(nums)):
        # And because we can travel only (RIGHT -> LEFT).
        # We don't care about previously used values,
        #  only searching for ones we didn't find higher ones.
        while stack and nums[stack[-1]] < nums[index]:
            out[stack.pop()] = nums[index]
        stack.append(index)
    out = [-1 if val == min_pos else val for val in out]
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Worst case: nums[0] is the Highest value, and everything else is in descending order.
# We will traverse `nums` once and store (n - 1) values in it => O(n).
# Then we're going to use every index stored in `stack` => O(2n).
# And extra traverse `nums` again, without dealing with a `stack` later => O(3n).
# -------------------------
# Auxiliary space: O(n)
# Stack is at max going to store `2n` values == every value is equal.
# So, we will store every index twice => O(2n).
# Extra `out` is always going to be of size `n` => O(n).


test: list[int] = [1, 2, 1]
test_out: list[int] = [2, -1, 2]
assert test_out == next_greater_elements(test)

test = [1, 2, 3, 4, 3]
test_out = [2, 3, 4, -1, 4]
assert test_out == next_greater_elements(test)

test = [340721417, 391789494, -146618623, 343033549, 127899661, 237162346]
test_out = [391789494, -1, 343033549, 391789494, 237162346, 340721417]
assert test_out == next_greater_elements(test)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 4)]
print(test)
