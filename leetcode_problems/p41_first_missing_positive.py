# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

def first_positive(nums: list[int]) -> int:
    min_pos = 1
    nums.sort()
    for x in range(len(nums)):
        if nums[x] <= 0:
            continue
        if nums[x] == min_pos:
            min_pos += 1
            continue
        if nums[x] > min_pos:
            return min_pos
    return min_pos


# Where's the catch? Hard problem, can't be so easy...
# We allowed to sort, and minimal positive int is 1
# If there's not presented any value equal to 1 it's always return 1,
# and if there's 1, next 2 with same logic. Hmm

test1 = [1, 2, 0]
test1_out = 3
print(first_positive(test1))

test2 = [3, 4, -1, 1]
test2_out = 2
print(first_positive(test2))

test3 = [7, 8, 9, 11, 12]
test3_out = 1
print(first_positive(test3))
