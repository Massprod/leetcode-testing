# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color
#  red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# --------------------------------
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
# --------------------------------
# ! Follow up: Could you come up with a one-pass algorithm using only constant extra space? !
from random import randint


def sort_colors(nums: list[int]) -> None:
    # working_sol (51.67%, 79.02%) -> (38ms, 16.47mb)  time: O(n) | space: O(1)
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


# Time complexity: O(n) <- n - length of an input array `nums`
# Essentially we're always using every index, only once => O(n)
# --------------------------------
# Auxiliary space: O(1).
# Only 2 INT's used, none of them depends on input => O(1).


test: list[int] = [2, 0, 2, 1, 1, 0]
test_out: list[int] = [0, 0, 1, 1, 2, 2]
sort_colors(test)
assert test_out == test

test = [2, 0, 1]
test_out = [0, 1, 2]
sort_colors(test)
assert test_out == test

test = [2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2]
test_out = sorted(test)
sort_colors(test)
assert test_out == test

test = [0, 1, 1, 1, 1, 1]
test_out = [0, 1, 1, 1, 1, 1]
sort_colors(test)
assert test_out == test

test = [randint(0, 2) for _ in range(300)]
test_out = sorted(test)
sort_colors(test)
assert test_out == test
