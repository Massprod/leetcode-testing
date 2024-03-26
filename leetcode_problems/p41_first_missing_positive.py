# Given an unsorted integer array nums.
# Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
# -----------------------
# 1 <= nums.length <= 10 ** 5
# -2 ** 31 <= nums[i] <= 2 ** 31 - 1
from random import randint


def first_positive_const(nums: list[int]) -> int:
    # working_sol (38.23%, 55.57%) -> (304ms, 30.30mb)  time: O(n) | space: O(1)
    # max_pos == integer which can be placed into only_positive_list
    max_pos = len(nums)
    mark: int = 100
    for x in range(max_pos):
        if nums[x] <= 0:
            nums[x] = max_pos + mark
        elif nums[x] > max_pos:
            nums[x] = max_pos + mark
    for x in range(max_pos):
        index: int = abs(nums[x]) - 1
        if index >= max_pos:
            continue
        if nums[index] < 0:  # ignoring already busy indexes for duplicated values
            continue
        nums[index] = -1 * nums[index]
    for x in range(max_pos):
        if nums[x] > 0:
            return x + 1
    return max_pos + 1


# Time complexity: O(n) -> 1 + 1 + 1 - 3 loops == 3n, worst case looping through n elements of input.
# Space complexity: O(1) -> no extra space used.
# -----------------------------
# First of all we need to change our list to a type of 1.......n only positive values.
# It's cant be done without sorting which takes extra space. Python sort() is at lowest (n * log n).
# List need's to be changed inplace without using anything extra.
# Instead of sorting, we're marking every negative value with something more than max_pos (length(list)).
# Now we can ignore all negatives as marked.
# Changing every value which more than max_pos to (max_pos + any) -> cuz by logic of a 1.......n list ->
# value equal to n + 1, can't have index inside of this list. Making this value non_placeable.
# Next, filtering out values which can be placed inside all positive list. Ignoring marked as (max_pos + any).
# If value can be placed in all_positive list than it's index will be (value - 1) -> 1 = [0], 2 = [1] etc.
# That's why we're taking value which is not marked as negative or non_placeable,
# and allocating its index by (value - 1) -> changing  value at this index to negative (marked).
# After we marked every value there's going to be positive values only on missing indexes.
# [0]mark-[1]mark-[2]mark-[3]mark-[4]pos-[5]mark-...etc
# Simply scrolling through this list and finding the lowest index, will give as missing minimal positive.
# If there's no positive values in a list than it's out of the LENGTH bound and equal to (LENGTH + 1).
# All values > LENGTH is non_placeable.
# Returning max_pos + 1 as highest integer -> length == last_index - 1 ->
# integer which can be placed at this index in only positive list 1......n -> last_index + 1 == length ->
# which leave us with next integer last_index + 1 + 1 == length + 1


test: list[int] = [1, 2, 0]
test_out: int = 3
assert test_out == first_positive_const(test)

test = [3, 4, -1, 1]
test_out = 2
assert test_out == first_positive_const(test)

test = [7, 8, 9, 11, 12]
test_out = 1
assert test_out == first_positive_const(test)

test = [1, 1]
test_out = 2
assert test_out == first_positive_const(test)

test = [1, 2, 3, 4, 5]
test_out = 6
assert test_out == first_positive_const(test)

test = [randint(-2 ** 31, 2 ** 31 - 1) for _ in range(10 ** 3)]
print(test)
