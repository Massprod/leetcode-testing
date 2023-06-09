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
    # working_sol (33.23%, 10.94%) time O(log n) | space O(1)
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
    return -1


# Failed 2 attempts, cuz rushed and didn't think about simple options:
#   1 fail - if we didn't find any target in not rotated list | simple return of -1
#   2 fail - if len(nums) == 1 no reasons to use loop | return -1 at start
#   3 could be fail - len(nums) == 0. we can't loop through | return -1 at start
# Always check pre commit. Even when it's look ultra simple.
# Time complexity O(log n): worst case we loop through 3/4 of input array.
#   as I understood: O(n) -> one loop, O(n**2) -> loop in loop, O(log n) -> not full loop with conditions
# Space complexity O(1): we're not creating anything new or changing input.
#   as I  understood: O(n) -> creating new array, O(1) -> not creating any new arrays, but only simple values.
# Not 100% sure about time, space complexity and I need to learn more about that formula not just most_popular cases.

tests = {}
# if rotated -> nums[-1] always lower than nums[0]
# else nums[0] always lower than nums[-1]
test1 = [4, 5, 6, 7, 0, 1, 2]
test1_target = 0
test1_out = 4
tests[(test1_out, test1_target)] = test1
print(search_rotated(test1, test1_target))

test2 = [1]
test2_target = 1
test2_out = 0
tests[(test2_out, test2_target)] = test2
print(search_rotated(test2, test2_target))

test3 = []
test3_target = 5
test3_out = -1
tests[(test3_out, test3_target)] = test3
print(search_rotated(test3, test3_target))

test4 = [1, 2, 3, 4, 5, 6, 7]
test4_target = 4
test4_out = 3
tests[(test4_out, test4_target)] = test4
print(search_rotated(test4, test4_target))

test5 = [4, 5, 6, 7, 0, 1, 2]
test5_target = 0
test5_out = 4
tests[(test5_out, test5_target)] = test5
print(search_rotated(test5, test5_target))

for key, value in tests.items():
    assert search_rotated(value, key[1]) == key[0]
