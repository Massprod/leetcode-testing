# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
#   find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where
#   1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2,
#   added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
# Your solution must use only constant extra space.
# -------------------
# 2 <= numbers.length <= 3 * 10 ** 4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
from random import randint


def two_sum(numbers: list[int], target: int) -> list[int]:
    # working_sol (79.84%, 94.99%) -> (136ms, 17.1mb)  time: O(n) | space: O(1)
    left: int = 0
    right: int = len(numbers) - 1
    while left < right:
        cur_sum: int = numbers[left] + numbers[right]
        if cur_sum == target:
            # zero_indexed -> 1_indexed
            return [left + 1, right + 1]
        if cur_sum > target:
            right -= 1
        if cur_sum < target:
            left += 1


# Time complexity: O(n) -> in the worst_case answer is indexes: first = (len(numbers) // 2) and sec = first + 1 ->
# n - len of input_array^^| -> then we need to travel whole input_array until we find it => O(n).
# Auxiliary space: O(1) -> using 3 extra INTs, none of them depends on input => O(1).
# -------------------
# Took a peak into BIG_BOYS with 90% and I missed most simple way to do this.
# This is just a closing_window problem, made it overcomplicated AF.
# Rebuild.
# -------------------
# Rushed and didn't take a break after BT task, failed 2 commits and missed most basic parts.
# Like middle and break when found index is same as x...
# -------------------
# Before I just stored every possible numbers[x] - target and just searched for this.
# Now we can't use any storage, so it's should be binary search.


test1 = [2, 7, 11, 15]
test1_t = 9
test1_out = [1, 2]
print(two_sum(test1, test1_t))
assert test1_out == two_sum(test1, test1_t)

test2 = [2, 3, 4]
test2_t = 6
test2_out = [1, 3]
print(two_sum(test2, test2_t))
assert test2_out == two_sum(test2, test2_t)

test3 = [-1, 0]
test3_t = -1
test3_out = [1, 2]
print(two_sum(test3, test3_t))
assert test3_out == two_sum(test3, test3_t)

test4 = [0, 0, 3, 4]
test4_t = 0
test4_out = [1, 2]
print(two_sum(test4, test4_t))
assert test4_out == two_sum(test4, test4_t)

test5 = [3, 24, 50, 79, 88, 150, 345]
test5_t = 200
test5_out = [3, 6]
print(two_sum(test5, test5_t))
assert test5_out == two_sum(test5, test5_t)
