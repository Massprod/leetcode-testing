# Given an integer array nums sorted in non-decreasing order,
#  remove some duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages,
#  you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
#  then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
# -----------------------
# 1 <= nums.length <= 3 * 10 ** 4
# -10 ** 4 <= nums[i] <= 10 ** 4
# nums is sorted in non-decreasing order.
from random import randint


def remove_duplicates(nums: list[int]) -> int:
    # working_sol (86.85%, 79.1%) -> (52ms, 16.2mb)  time: O(n) | space: O(1)
    # Essentially building array inside array.
    index: int = 1
    count: int = 1
    for x in range(1, len(nums)):
        # Given ascending order, only diff is higher.
        # Place new value.
        if nums[index - 1] < nums[x]:
            nums[index] = nums[x]
            index += 1
            count = 1
        # Place duplicate, if not already placed.
        elif count < 2 and nums[index - 1] == nums[x]:
            nums[index] = nums[x]
            index += 1
            count += 1
    return index


# Time complexity: O(n) -> traversing whole input array once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 extra constant INTs used, none of them depends on input => O(1).


test: list[int] = [1, 1, 1, 2, 2, 3]
test_out: int = 5
test_out_list: list[int] = [1, 1, 2, 2, 3]
remove_duplicates(test)
assert test_out_list == test[:test_out]

test = [0, 0, 1, 1, 1, 1, 2, 3, 3]
test_out = 7
test_out_list = [0, 0, 1, 1, 2, 3, 3]
remove_duplicates(test)
assert test_out_list == test[:test_out]

test = [0, 0, 1, 1, 1, 1, 2, 2, 2, 4]
test_k = 7
test_out_list = [0, 0, 1, 1, 2, 2, 4]
remove_duplicates(test)
assert test_out_list == test[:test_out]

test = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_out = 2
test_out_list = [1, 1]
remove_duplicates(test)
assert test_out_list == test[:test_out]

test = sorted([randint(-10, 10) for _ in range(10 ** 3)])
print(test)
