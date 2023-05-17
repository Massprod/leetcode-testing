# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# n == nums.length  ,  1 <= n <= 300  ,  nums[i] is either 0, 1, or 2.
# You must solve this problem without using the library's sort function.
# --------------------------------
# ! Follow up: Could you come up with a one-pass algorithm using only constant extra space? !
import copy
from random import randint


def sort_colors(nums: list[int]) -> None:
    # working_sol (29.38%, 19.59%) -> (44ms, 16.1mb)  time: O( ) | space: O(1)
    left: int = 0
    right: int = len(nums) - 1
    for x in range(len(nums)):
        if x > right:
            break
        if nums[x] == 2 and x <= right:
            nums[x], nums[right] = nums[right], nums[x]
            right -= 1
            while nums[x] == 2 and x < right:
                nums[x], nums[right] = nums[right], nums[x]
                right -= 1
        if nums[x] == 0 and x >= left:
            nums[x], nums[left] = nums[left], nums[x]
            left += 1
            while nums[x] == 2 and x < right:
                nums[x], nums[right] = nums[right], nums[x]
                right -= 1
                if nums[x] == 0:
                    left += 1

# Time complexity: O(n) -> worst case, there's no 0 or 2 in array ->
#                          -> so we're looping once through whole input_array without changing anything => O(n)
#                  -------
#                  Ω(n) -> best case, always looping once through every index of input_array => O(n)
#                  -------
#                  Θ(n) -> median case, always looping once through every index of input_array => O(n)
#                  -------
#     ! we're looping once through whole input_array indexes, cuz every time we use while_loop we're changing
#       left and right, and they're index_limits, we will break from loop when we used every index once. !
#
# Space complexity: O(1) -> 2 extra constants => O(1)
# -------------------
# I made it by intuition and started with one-way solution, cuz why not?
# But it was hard to come up with tests cases, as always commit -> fail-> rebuild. Caused me 2 fails.
# -------------------
# It's not actually one-pass solution. Because we're looping once but there's nested loop inside to change blue color.
# But maybe it's one-pass cuz there's no definition of that, and we're looping once through whole input.


test1 = [2, 0, 2, 1, 1, 0]
test1_out = [0, 0, 1, 1, 2, 2]
sort_colors(test1)
print(test1)

test2 = [2, 0, 1]
test2_out = [0, 1, 2]
sort_colors(test2)
print(test2)

test3 = [2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2]
sort_colors(test3)
print(test3)

test4 = [0, 1, 1, 1, 1, 1]
sort_colors(test4)
print(test4)

test5 = [2, 1, 1, 2, 0, 1]
sort_colors(test5)
print(test5)

# test6 - failed -> I knew it's not a working solution, but I could make tests cases on my own and failed to see them.
#                   Cuz im switching 2 -> 0 and failing to see all options.
#                   -> In this one I failed with changing nums[x] == 2, if we're hitting break  x < right
test6 = [2, 0, 2]
sort_colors(test6)
print(test6)

# test7 - failed -> I need to make while loop for 2 to 2 switch.
test7 = [2, 1, 2]
sort_colors(test7)
print(test7)

test8 = [2, 0, 2, 0, 1, 2, 0]
sort_colors(test8)
print(test8)

# Dunno about other cases, but for 1000 random cases it's working.
for test in range(1000):
    test_ = []
    for _ in range(1000):
        test_.append(randint(0, 2))
    test_2 = copy.deepcopy(test_)
    sort_colors(test_)
    test_2.sort()
    assert test_2 == test_
