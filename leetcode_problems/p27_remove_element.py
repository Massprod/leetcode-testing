# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.


def remove_element(nums: list[int], val: int) -> int:
    # working_sol (40.32%, 94.31%)
    pos = 0
    length = len(nums)
    for x in range(length):
        if nums[x] == val:
            continue
        nums[pos] = nums[x]
        pos += 1
    return pos


test1 = [3, 2, 2, 3]
test1_out = 2
test1_target = 3
print(remove_element(test1, val=test1_target))
print(test1)
test2 = [0, 1, 2, 2, 3, 0, 4, 2]
test2_out = 5
test2_target = 2
print(remove_element(test2, test2_target))
print(test2)
