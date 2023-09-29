# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
# ------------------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 5 <= nums[i] <= 10 ** 5


def is_monotonic(nums: list[int]) -> bool:
    # working_sol (90.78%, 57.79%) -> (799ms, 30.6mb)  time: O(n) | space: O(1)
    if len(nums) == 1:
        return True
    index: int = 1
    ascending: bool = False
    descending: bool = False
    while index != len(nums):
        # Starts in ascending.
        if nums[index] < nums[index - 1]:
            descending = True
            index += 1
            break
        # Starts in descending.
        elif nums[index] > nums[index - 1]:
            ascending = True
            index += 1
            break
        # Otherwise, all value are equal == True.
        index += 1
    # Confirm that whole array is in ascending|descending order.
    if ascending:
        while index != len(nums):
            if not nums[index] >= nums[index - 1]:
                return False
            index += 1
    elif descending:
        while index != len(nums):
            if not nums[index] <= nums[index - 1]:
                return False
            index += 1
    return True


# Time complexity: O(n) -> traver of whole input array, once => O(n).
# n - len of input array^^|
# Auxiliary space: O(1) -> only 3 extra constants used: INT + 2#BOOLeans, none of them depends on input => O(1).
# ------------------------
# Essentially jus decide if it's ascending or descending.
# Only question how to do this in 1 traverse?
# Check first values? Like [0] > [1] or [0] < [1] and then we check rest to be ascending or descending.
# What if they're equal? Skip them until there's something different or end of the array == True.
# Should be correct.


test: list[int] = [1, 2, 2, 3]
test_out: bool = True
assert test_out == is_monotonic(test)

test = [6, 5, 4, 4]
test_out = True
assert test_out == is_monotonic(test)

test = [1, 3, 2]
test_out = False
assert test_out == is_monotonic(test)
