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
    # for _ in nums:
    #     if nums.count(_) > 1:
    #         for x in range(nums.count(_) - 1):
    #             nums.remove(_)
    # return len(nums)
    # ----------------------
    # working_sol (60.59%, 9.21%)
    # uniques = set()
    # for _ in nums:
    #     uniques.add(_)
    # x = 0
    # uniques = sorted(uniques)
    # for _ in uniques:
    #     nums[x] = _
    #     x += 1
    # return len(uniques)
    # ----------------------
    # working_sol (32.8%, 48.90%)
    pos = 1
    for x in range(0, len(nums)):
        if x == len(nums) - 1 and nums[x] != nums[x - 1]:
            nums[pos - 1] = nums[x]
        elif x == len(nums) - 1 and nums[x] == nums[x - 1]:
            nums[pos - 1] = nums[x]
        elif nums[x] != nums[x + 1]:
            nums[pos - 1] = nums[x]
            pos += 1
    return pos
    # ----------------------
    # working_sol (41.81%, 94%) - semi_googled solution, cuz I was checking other ways after 3 of mine.
    # and it's actually pretty close to mine #3. But I failed to count more pretty :) 0.1 mb memory-diff.
    # pos = 1
    # length = len(nums)
    # for x in range(1, length):
    #     if nums[x - 1] != nums[x]:
    #         nums[pos] = nums[x]
    #         pos += 1
    # return pos

# Both solutions work and I might find another, if revisit :)
# If I understand correctly *in-place* means I can't create another list.
# But I can change existing by either indexing or removing values.
# !The remaining elements of nums are not important as well as the size of nums.!
# !The input is usually overwritten by the output as the algorithm executes.
# An in-place algorithm updates its input sequence only through replacement or swapping of elements.!


test1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
test1_out = 5
test1_changed = [0, 1, 2, 3, 4, "_", "_", "_", "_", "_"]
print(remove_duplicates(test1))
test2 = [-1, 0, 0, 0, 0, 3, 3]
test2_out = 3
test2_changed = [-1, 0, 3]
print(remove_duplicates(test2))
