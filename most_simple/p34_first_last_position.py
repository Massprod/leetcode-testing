# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.


def first_last(nums: list[int], target: int) -> list[int]:
    if len(nums) == 0:
        return [-1, -1]
    if nums[-1] < target:
        return [-1, -1]
    if nums[0] > target:
        return [-1, -1]
    x, y = 0, (len(nums) - 1)
    start, end = -1, -1
    while x < y and (start == -1 or end == -1):
        if nums[x] == target and start == -1:
            start = x
            continue
        if nums[y] == target and end == -1:
            end = y
            continue
        if nums[x] < target:
            x += 1
        if nums[y] > target:
            y -= 1
        if nums[x] == target and start != -1:
            if nums[x] != nums[x + 1]:
                end = x
            x += 1
        if nums[y] == target and end != -1:
            if nums[y] != nums[y - 1]:
                start = y
            y -= 1
    return [start, end]


# Is this even correct task description?
# What if we have only ONE index for a target, can a START index and END index be the same,
# or we should return something like [START, -1] | [-1, END] ????
# What to return when len(nums) == 1? Guess I need to fail commit to find out.

test1 = [5, 7, 7, 8, 8, 10]
test1_target = 8
test1_out = [3, 4]
print(first_last(test1, test1_target))

test2 = [5, 7, 7, 8, 8, 10]
test2_target = 6
test2_out = [-1, -1]
print(first_last(test2, test2_target))

test3 = []
test3_target = 0
test3_out = [-1, -3]
print(first_last(test3, test3_target))
