# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
#   from robbing each of them is that adjacent houses have security systems connected,
#   and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
#   return the maximum amount of money you can rob tonight without alerting the police.
# ----------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
from random import randint


def rob(nums: list[int]) -> int:
    # working_sol (88.64%, 56.96%) -> (32ms, 16.56mb)  time: O(n) | space: O(1)
    # With 2 or less houses, we can only choose one.
    if len(nums) < 3:
        return max(nums)
    # If we start from First house, we can continue only from Third.
    nums[2] += nums[0]
    for x in range(3, len(nums)):
        nums[x] += max(nums[x - 2], nums[x - 3])
    # We will have 2 maximized paths: ending on last house, and pre-last.
    # We need the highest value.
    return max(nums[-1], nums[-2])


# Time complexity: O(n) <- n - length of input array `nums`.
# Single traverse of the whole input array `nums`.
# ----------------------
# Auxiliary space: O(1).
# Nothing extra used, reusing input array `nums`.
# ----------------------
# Extra part, logic and counting is correct. But there's a paths which could be ended on -1 and -2.
# So we need to find best option from this two, otherwise we're missing maximized path and just returning
# maximized path leading to the LAST house, and it could be wrong.
# And extra to that, edge case with only 1 house: just return this house value.
# ----------------------
# DP problem, and after a night of thinking finally see how it can be solved:
# Like -> 1, 2, 3, 4, 5 ->
# -> If we use standard recursion then we're checking paths like 1 -> 3 -> 5 | 1 -> 5 | 3 -> 5 | 2 -> 4 | 2 -> 5
#  which can be actually culled into 1 -> 3 -> 5 | 2 -> 4 | 2 -> 5
#  because we're having only positive integers and there's no reason to skip any houses.
# So we can just summarize everything on this 3 paths and any other path which is going to be continuation of them,
#  and it's already going to have maximized previous part of the array.
# Like if we start a path from 5 we already have maximized option from previous indexes(houses).
# We can just use [x - 2] or [x - 3] + [x] => and we will cover all these paths together.
# Like if we add 6 into this sequence, actually is better to use normal values =>
# => 11, 5, 17, 14, 11, 12 -> for first 2 indexes we ignore it, because obvious index error =>
# -> start == 17 -> x == 2 -> [0] == 11 or  [-1] <- ignoring -> taking best(highest) option => [2] = 17 + 11 == 28
#    ^^This is correct path of 0 -> 2, and only possible
# => 11, 5, 28, 14, 11, 12
# -> start == 14 -> x == 3 -> [1] == 5 or [0] == 11 -> best option => [3] = 11 + 14 == 25
#    ^^This one is covering not only one path, but all possible ways until this house:
#      0 -> 3 | 1 -> 3  <- anything else is in a cop_zone, and we can't use it.
# => 11, 5, 28, 25, 11, 12
# -> start == 11 -> x == 4 -> [2] == 28 or [1] == 5 -> best option => [4] = 28 + 11 == 39
#    ^^Again we're covering all options: 0 -> 2 -> 4 | 1 -> 4 |
#      And because we already have best option stored in 2 we can just take it, and be sure
#      that's maximized value we could get before 2.
# => 11, 5, 28, 25, 39, 12
# -> start == 12 -> x == 5 -> [3] == 25  or [2] == 28 -> bes option => [5] = 28 + 12 == 40
#    ^^Now it's more convincing that this approach is correct, because we're taking one of already summarized option
#      not just 1 starting point and other summarized like before.
#      Covering: 0 -> 3 -> 5 | 0 -> 2 -> 5 | 1 -> 3 -> 5 |
#       0 -> 3 is already calculated before and stored in 3 index
#       0 -> 2 same
#       1 -> 3 same
#       But we're not storing these paths, we're storing BEST option we could take on path before we hit some house.
#       So we can freely just take index 3 or 2 as best option and be sure it's maximized.


test: list[int] = [1, 2, 3, 1]
test_out: int = 4
assert test_out == rob(test)

test = [2, 7, 9, 3, 1]
test_out = 12
assert test_out == rob(test)

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
test_out = 36
assert test_out == rob(test)

test = [1]
test_out = 1
assert test_out == rob(test)

test = [1, 333, 99]
test_out = 333
assert test_out == rob(test)

test = [randint(0, 400) for _ in range(100)]
print(test)
