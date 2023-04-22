# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Add metrics in a future % is good but numbers should be here. Maybe revisit other's will see.

def first_positive_const(nums: list[int]) -> int:
    # working_sol (26.1%, 64.75%) time: O(n) | space: O(1)
    max_pos = len(nums)  # max_positive_integer which can be placed into only_positive_list
    for x in range(max_pos):
        if nums[x] <= 0:
            nums[x] = max_pos + 10
        elif nums[x] > max_pos:
            nums[x] = max_pos + 10
    for x in range(max_pos):
        cursor = abs(nums[x])
        if cursor > max_pos:
            continue
        if nums[cursor - 1] < 0:  # ignoring already busy indexes for duplicated values
            continue
        nums[cursor - 1] = -1 * nums[cursor - 1]
    for x in range(max_pos):
        if nums[x] > 0:
            return x + 1
    return max_pos + 1

# Time complexity: O(n) -> 1 + 1 + 1 - 3 loops == 3n, worst case looping through n elements of input.
# Space complexity: O(1) -> no extra space used.

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
# -----------------------------
# Well now, it's HARD problem.


def first_positive(nums: list[int]) -> int:
    # working_sol (52.42%, 46.58%) -> (372ms, 27.9mb) time: O(n * log n) | space O(n)
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

# Time complexity: O(n * log n) -> worst case we loop through whole list of nums and min_pos will be (nums[-1] + 1)
# Space complexity: O(n) -> one constant min_pos, and doesn't depend on input, and O(n) for sort()
#
# Ok. Python sort() takes at lowest Ω(n), violating the rule with memory. Found the catch.
# -----------------------------
# ! "No extra space" implies some amount of space,
# usually exactly n, is available via the input, and no more should be used !
# -> Ok. That's a catch I guess, not available to use min_pos as a constant.
# -----------------------------
# ! a space complexity of O(1) means that the space required by the algorithm to process data is constant;
# it does not grow with the size of the data on which the algorithm is operating. !
# -----------------------------
# ! For an algorithm to take constant extra space,
# the extra variables used to solve it should not change with the input size !
# But all googled solution's at least uses LEN(NUMS) as constant n, which depends on input size. Hmm
# -----------------------------
# Where's the catch? Hard problem, can't be so easy...
# We allowed to sort, and minimal positive int is 1
# If there's not presented any value equal to 1 it's always return 1,
# and if there's 1, next 2 with same logic. Hmm


test1 = [1, 2, 0]
test1_out = 3
# print(first_positive(test1))
print(first_positive_const(test1))

test2 = [3, 4, -1, 1]
test2_out = 2
# print(first_positive(test2))
print(first_positive_const(test2))

test3 = [7, 8, 9, 11, 12]
test3_out = 1
# print(first_positive(test3))
print(first_positive_const(test3))

test4 = [1, 1]
test4_out = 2
print(first_positive_const(test4))

test5 = [1, 2, 3, 4, 5]
print(first_positive_const(test5))
