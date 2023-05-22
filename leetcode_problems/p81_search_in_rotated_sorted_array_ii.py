# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
#
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
#
# Given the array nums after the rotation and an integer target,
# return true if target is in nums, or false if it is not in nums.
#
# You must decrease the overall operation steps as much as possible.
# ---------------------------
# 1 <= nums.length <= 5000  ,  -104 <= nums[i] <= 104  ,  -104 <= target <= 104
# nums is guaranteed to be rotated at some pivot.


def search(nums: list[int], target: int) -> bool:
    # working_sol (48.1%, 11.68%) -> (60ms, 16.9mb)  time: O(n) | space: O(1)
    if len(nums) == 0:
        return False
    elif len(nums) == 1:
        if nums[0] == target:
            return True
        else:
            return False
    # if rotated
    elif nums[-1] <= nums[0]:
        if nums[-1] < target < nums[0]:
            return False
        elif target >= nums[0]:
            for x in range(len(nums)):
                if nums[x] == target:
                    return True
                elif nums[x] < nums[x - 1] and x > 0:
                    return False
        elif target <= nums[-1]:
            for x in range(len(nums) - 1, -1, -1):
                if nums[x] == target:
                    return True
                elif nums[x] < nums[x - 1]:
                    return False
    # if not rotated
    elif target > nums[-1]:
        return False
    elif target < nums[0]:
        return False
    elif nums[0] <= target <= nums[-1]:
        for x in range(len(nums)):
            if nums[x] == target:
                return True
    return False


# Time complexity: O(n) -> without duplicates, it was O(log n) -> because we always could break at some part of array,
# n -> length of input^^   now we can't break that easily and in the worst case going to check whole array => O(n)
#                          ! case == [1, 1, 1, 1, 1, 1, 1, 1, 1] -> any part of array we're starting, we can't stop
#                            until we reach lower or higher values, or simply out of indexes. !
# Space complexity: O(1) -> no extra space.
# --------------------------------
# ! nums is guaranteed to be rotated at some pivot. ! <- lies, deleted part with not rotated to check this.
# and what I get [1,3] -> how is it rotated?
# --------------------------------
# Follow up: This problem is similar to Search in Rotated Sorted Array,
# but nums may contain duplicates.
# Would this affect the runtime complexity? How and why?
# ^^Extra indexes to check, and we can't skip them cuz, we're not having data on what max_min values is.
#   Only pivot point values nums[-1] -> left side of a pivot point
#   and nums[0] -> right side of a pivot point.
#   But they don't really matter, because we always break from loop at values higher or lesser than target,
#   depends on - in what half we're searching. Because now, we're going to have duplicates, we can't break that easily,
#   and in worst case [1, 1, 1, 1, 1, 1, 1, 1, 0] - target = 2 -> it's rotated list,
#   and we will check every index with 1 value, before we had no duplicates and could break at 1 index.
#   Only way I see to speed this up is to check whole list for correct_values and break without starting search,
#   But it's conflicts with whole idea, we could make this from a start and hit time_limit.
#   ! You must decrease the overall operation steps as much as possible. ! <- this
#   Another way is to add middle point check, but it's hard, and we're still going to check every index,
#   at least in this case.^^


test1 = [2, 5, 6, 0, 0, 1, 2]
test1_target = 0
test1_out = True
print(search(test1, test1_target))

test2 = [2, 5, 6, 0, 0, 1, 2]
test2_target = 3
test2_out = False
print(search(test2, test2_target))

test3 = [1, 1, 1, 1, 1, 1, 1, 1, 0]
test3_target = 2
test3_out = False
print(search(test3, test3_target))

# test4 - failed -> failed to consider we can have not rotated list, but with same values on start and end,
#                   main reason for that I didn't rebuild p33, and just made it work for same start_end values.
#                   Problem with that, we had only uniques, so there was no way to encounter duplicate.
#                   [1, 1] -> won't be possible and index[x + 1] will always be presented, if it's rotated.
#                   Btw, bad practice to used for loops in [x + 1] way, but in this case, it's ok,
#                   but still can be changed to [x - 1] -> better to always do this.
test4 = [1, 1]
test4_target = 2
test4_out = False
print(search(test4, test4_target))
