# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements
# in the order they were present in nums initially. The remaining elements of nums are not
# important as well as the size of nums.
# Return k.

def remove_duplicates(nums: list[int]) -> int:
    # working_sol (5.7% , 48.90%)
    for _ in nums:
        if nums.count(_) > 1:
            for x in range(nums.count(_) - 1):
                nums.remove(_)
    return len(nums)

# 5.7%?? Rebuild later

test1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
test1_out = 5
test1_changed = [0, 1, 2, 3, 4, "_", "_", "_", "_", "_"]
print(remove_duplicates(test1))