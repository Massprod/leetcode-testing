# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.
# ^^^^
# Already been solving tasks with max_sum but for 3 nums, there's used all nums in some range.
# Because of that, we can't skip values and need to check every possible index.
# 100% sure I need to use conquer and divide but with recursion or just while loop?
# Time limit or not, first going to try loop.

def max_sub_array(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    left_cursor = 0
    right_cursor = len(nums) - 1
    max_sum = 0
    while left_cursor <= right_cursor:
        temp_sum = sum(nums[left_cursor: right_cursor + 1])
        if max_sum == 0 and temp_sum != 0:
            max_sum = temp_sum
        if temp_sum > max_sum:
            max_sum = temp_sum
        if left_cursor == right_cursor:
            break
        left_sum = sum(nums[left_cursor: right_cursor])
        right_sum = sum(nums[left_cursor + 1: right_cursor + 1])
        if left_sum > right_sum:
            right_cursor -= 1
        if left_sum < right_sum:
            left_cursor += 1
        if left_sum == right_sum:
            if nums[left_cursor + 1] > nums[right_cursor - 1]:
                right_cursor -= 1
            else:
                left_cursor += 1
    return max_sum


test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test1_out = 6
print(max_sub_array(test1))

test2 = [1]
test2_out = 1
print(max_sub_array(test2))

test3 = [5, 4, -1, 7, 8]
test3_out = 23
print(max_sub_array(test3))

# test4 - failed -> I made default max_sum as 0, either I should have used minimum value -10^4 or ???
test4 = [-2, -1]
test4_out = -1
print(max_sub_array(test4))

# test5 - failed -> max_value on one side which I wanted to skip with checking (-+1) indexes, but it's not working.
test5 = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]
test5_out = 6
print(max_sub_array(test5))
