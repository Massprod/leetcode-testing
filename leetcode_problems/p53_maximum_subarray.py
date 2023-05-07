# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.

def max_sub_array(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    left_cursor = 0
    right_cursor = len(nums) - 1
    max_sum = 0
    while left_cursor <= right_cursor:
        temp_sum = sum(nums[left_cursor: right_cursor + 1])
        if temp_sum > max_sum:
            max_sum = temp_sum
        elif nums[left_cursor] < nums[right_cursor]:
            left_cursor += 1
        elif nums[left_cursor] > nums[right_cursor]:
            right_cursor -= 1
        elif nums[left_cursor] == nums[right_cursor]:
            right_cursor -= 1
    return max_sum

# Already been solving tasks with max_sum but for 3 nums, there's used all nums in some range.
# Because of that, we can't skip values and need to check every possible index.
# 100% sure I need to use conquer and divide but with recursion or just while loop?
# Time limit or not, first going to try loop.


test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test1_out = 6
print(max_sub_array(test1))

test2 = [1]
test2_out = 1
print(max_sub_array(test2))

test3 = [5, 4, -1, 7, 8]
test3_out = 23
print(max_sub_array(test3))
