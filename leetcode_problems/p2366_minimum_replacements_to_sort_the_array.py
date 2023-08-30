# You are given a 0-indexed integer array nums.
# In one operation you can replace any element of the array with any two elements that sum to it.
#   For example, consider nums = [5,6,7].
#   In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
# Return the minimum number of operations to make an array that is sorted in non-decreasing order.
# --------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
from math import ceil
from random import randint


def minimum_replacement(nums: list[int]) -> int:
    # working_sol (98.35%, 79.34%) -> (453ms, 31.1mb)  time: O(n) | space: O(1)
    # ! It is optimal to never make an operation to the last element of the array. !
    cur_highest: int = nums[-1]
    replacements: int = 0
    # Example: 883, 221.
    for x in range(len(nums) - 2, -1, -1):
        # We can take 221 3.99 times from 883. Obviously we can't take only part.
        # So we need to remove fractions, either cell or floor with +1.
        cur_parts: int = ceil(nums[x] / cur_highest)
        # And if we take 4 parts from 883 => 220.75. Again we can't take only part.
        # We can't take ceil() 221, because it's over the number limit -> 221 * 4 > 883.
        # But we can take 220 and assume that we're combining other parts with extra value.
        # Like -> 200 + 221 + 221 + 221 == 883. Lowest used, and we used all 4 parts.
        # And it's always lower than number by which we're trying to slice.
        cur_highest = nums[x] // cur_parts
        # We're not slicing last part, so it's need's to be excluded.
        replacements += cur_parts - 1
    return replacements


# Time complexity: O(n) -> traversing whole input array once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 3 extra INTs used, none of them depends on input => O(1).
# --------------
# Hints:
# -> ! It is optimal to never make an operation to the last element of the array. !
# -> ! You can iterate from the second last element to the first.
#      If the current value is greater than the previous bound, we want to break it into pieces
#       so that the smaller one is as large as possible but not larger than the previous one. !
# ceil(array[index] / highest) <- well it will give us maximum parts we can get from it.
# like -> 883, 221 => 883 - 221 => 662 - 221 => 441 - 221 => 220.
# We can slice it in 4 parts, and use 220 as last value.
# And because we can take w.e sums we want, we can always take the smallest by 883 // 4 => 220 == array[index] // parts.
# Assuming that we're allowed to take floats, or just shuffle this sums around.
# Let's try. Working with randoms.


test: list[int] = [3, 9, 3]
test_out: int = 2
assert test_out == minimum_replacement(test)

test = [1, 2, 3, 4, 5]
test_out = 0
assert test_out == minimum_replacement(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 3)]
print(test)
