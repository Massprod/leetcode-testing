# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k,
#  to get accepted, you need to do the following things:
#  - Change the array nums such that the first k elements
#     of nums contain the elements which are not equal to val.
#  - The remaining elements of nums are not important as well as the size of nums.
# Return k.
# --------------
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100


def remove_element(nums: list[int], val: int) -> int:
    # working_sol (97.92%, 99.94%) -> (30ms, 16mb)  time: O(n) | space: O(1)
    # Essentially rebuilding array 0 -> index,
    #  with everything != val.
    index: int = 0
    for x in range(len(nums)):
        # Skip val.
        if nums[x] == val:
            continue
        nums[index] = nums[x]
        index += 1
    return index


# Time complexity: O(n) -> traverse of the whole input array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 1 constant INT used, nothing depends on input => O(1).


test: list[int] = [3, 2, 2, 3]
test_target: int = 3
remove_element(test, test_target)
test_out: int = 2
assert len(test[:test_out]) == 2
assert test_target not in test[:test_out]

test = [0, 1, 2, 2, 3, 0, 4, 2]
test_target = 2
remove_element(test, test_target)
test_out = 5
assert len(test[:test_out]) == 5
assert test_target not in test[:test_out]
