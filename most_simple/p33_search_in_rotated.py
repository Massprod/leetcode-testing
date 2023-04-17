# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index
# k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.


def search_rotated(nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    elif len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    # if rotated
    elif nums[-1] < nums[0]:
        if nums[-1] < target < nums[0]:
            return -1
        elif target >= nums[0]:
            for x in range(len(nums)):
                if nums[x] == target:
                    return x
                elif nums[x] > nums[x + 1]:
                    return -1
        elif target <= nums[-1]:
            for x in range(len(nums) - 1, -1, -1):
                if nums[x] == target:
                    return x
                elif nums[x] < nums[x - 1]:
                    return -1
    # if not rotated
    elif target > nums[-1]:
        return -1
    elif target < nums[0]:
        return -1
    elif nums[0] <= target <= nums[-1]:
        for x in range(len(nums)):
            if nums[x] == target:
                return x


# if rotated -> nums[-1] always lower than nums[0]
# else nums[0] always lower than nums[-1]
test1 = [4, 5, 6, 7, 0, 1, 2]
test1_target = 0
test1_out = 4
print(search_rotated(test1, test1_target))

test2 = [1]
test2_target = 1
test2_out = 0
print(search_rotated(test2, test2_target))

test3 = []
test3_target = 5
test3_out = -1
print(search_rotated(test3, test3_target))

test4 = [1, 2, 3, 4, 5, 6, 7]
test4_target = 4
test4_out = 3
print(search_rotated(test4, test4_target))

test5 = [4, 5, 6, 7, 0, 1, 2]
test5_target = 0
test5_out = 4
print(search_rotated(test5, test5_target))
