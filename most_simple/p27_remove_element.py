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
    pos = -1
    for x in range(len(nums)):
        if nums[x] == val:
            nums[x], nums[pos] = nums[pos], nums[x]
            pos -= 1
    return (pos * -1) - 1


test1 = [3,2,2,3]
test1_out = 2
test1[-2], test1[0] = test1[0], test1[-2]
print(remove_element(test1, val=3))
