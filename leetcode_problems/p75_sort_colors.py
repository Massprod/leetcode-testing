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
    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        for x in range(len(nums)):
            if nums[x] == 2 and x <= right:
                nums[x], nums[right] = nums[right], nums[x]
                right -= 1
            if nums[x] == 0 and x >= left:
                nums[x], nums[left] = nums[left], nums[x]
                left += 1
                while nums[x] == 2:
                    nums[x], nums[right] = nums[right], nums[x]
                    right -= 1
                    if nums[x] == 0:
                        left += 1
        break


# It's not actually one-pass solution. Because we're looping once but there's neste loop inside to change blue color.
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
