# Given an integer array nums sorted in non-decreasing order,
#  remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
# Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:
#  - Change the array nums such that the first k elements of nums contain the unique elements
#    in the order they were present in nums initially. The remaining elements of nums are not
#    important as well as the size of nums.
#  - Return k.
# -------------------
# 1 <= nums.length <= 3 * 10 ** 4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.


def remove_duplicates(nums: list[int]) -> int:
    # working_sol (98.66%, 81.38%) -> (71ms, 17.9mb)  time: O(n) | space: O(1)
    index: int = 1
    for x in range(1, len(nums)):
        # Ascending, only change is something higher.
        if nums[index - 1] < nums[x]:
            nums[index] = nums[x]
            index += 1
    return index


# Time complexity: O(n) -> every index will be used once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 1 extra INT used, doesn't depend on input => O(1).


test: list[int] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
test_out_list: list[int] = [0, 1, 2, 3, 4]
test_out: int = 5
remove_duplicates(test)
assert test_out_list == test[:test_out]

test = [-1, 0, 0, 0, 0, 3, 3]
test_out = 3
test_out_list = [-1, 0, 3]
remove_duplicates(test)
assert test_out_list == test[:test_out]
