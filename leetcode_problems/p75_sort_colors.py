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

def sort_colors(nums: list[int]) -> None:
    pass


test1 = [2, 0, 2, 1, 1, 0]
test1_out = [0, 0, 1, 1, 2, 2]
print(sort_colors(test1))

test2 = [2, 0, 1]
test2_out = [0, 1, 2]
