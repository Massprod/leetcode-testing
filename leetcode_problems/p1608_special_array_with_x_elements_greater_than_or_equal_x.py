# You are given an array nums of non-negative integers.
# nums is considered special if there exists a number x such
#   that there are exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1.
# It can be proven that if nums is special, the value for x is unique.
# ------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
from random import randint


def special_array(nums: list[int]) -> int:
    # working_sol (80.18%, 95.57%) -> (51ms, 16.2mb)  time: O(n * n) | space: O(1)
    # all X possible
    encounters: list[int] = [0 for _ in range(101)]
    last_value: int = nums[0]
    # count every encounter of values higher than possible X's
    for x in range(len(nums)):
        # we can limit checks to 100, cuz there's no possible X > 100
        # extra we can limit every X encounter to nums[x],
        # because every nums[x] should be >= X
        limit: int = nums[x]
        last_value = max(last_value, nums[x])
        if nums[x] > 100:
            limit = 100
        for y in range(limit + 1):
            encounters[y] += 1
    # extra walk to find correct pair
    # limited by 100, or last maximum value met
    if last_value > 100:
        last_value = 100
    for z in range(last_value + 1):
        if z == encounters[z]:
            return z
    return -1


# Time complexity: O(n * n) -> traversing whole input_array with nested loop, in the worst case ->
# n - len of input_array^^| -> there's all values in input_array higher than 100 and len(input_array) == 100,
#                           so we're going to increment every X in encounters for every index in nums => O(n * n) ->
#                           -> extra in this case we're extra traversing whole encounters again => O(n) -> O(n * n).
# Auxiliary space: O(1) -> creating extra array of size == 101, and using 2 extra INTs,
#                          none of these depends on input and will be used everytime -> O(1).
# ------------------
# Ok. Rebuild it ->
# -> First we don't need X's more than 100 and changed dictionary into a list with set indexes.
# -> Second changed filtering, now it's limited to nums[x] and we don't need extra check inside Y loop.
# X2 faster and simplier to read now.
# Extra we can limit Z loop, because if we have only nums[x] < 50, why would I need to check 50 - 100?
# ------------------
# So, make dictionary for 0 -> x and count everything we met in the array.
# Return any x from dictionary where key == value. Should be correct, but how we decide which x to use?
# First, x can't be more than length because x should be equal to encounters of x >= values.
# But I don't want to add everything in length, because if we have length of 1000,
# and only values are 10 and 5 like 500 of 10s and 500 of 5. If we just consider length than,
# we add 1000 keys from 0 to 1000, which is not ok.
# And it fails, cuz there's only 10, and we have 500 10s not 10 as x.
# First encounter? Like we hit 10, we just add 0 -> 10 as keys and count for this, because there's no reason
# to add anything else, cuz value >= x should be encountered 10 times no more no less.
# And we didn't encounter anything more than 10 at this time. Let's test.
# Extra, forgot we x <= length, so we don't need anything more than 100 as keys.


test1 = [3, 5]
test1_out = 2
print(special_array(test1))
assert test1_out == special_array(test1)

test2 = [0, 0]
test2_out = -1
print(special_array(test2))
assert test2_out == special_array(test2)

test3 = [0, 4, 3, 0, 4]
test3_out = 3
print(special_array(test3))
assert test3_out == special_array(test3)

# Testing with leetcode testcases.
# test = []
# for _ in range(100):
#     test.append(randint(0, 1000))
# print(test)
# print(special_array(test))
