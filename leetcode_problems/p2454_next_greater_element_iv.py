# You are given a 0-indexed array of non-negative integers nums.
# For each integer in nums, you must find its respective second greater integer.
# The second greater integer of nums[i] is nums[j] such that:
#   - j > i
#   - nums[j] > nums[i]
#   - There exists exactly one index k such that nums[k] > nums[i] and i < k < j.
# If there is no such nums[j], the second greater integer is considered to be -1.
# For example, in the array [1, 2, 4, 3], the second greater integer of 1 is 4, 2 is 3, and that of 3 and 4 is -1.
# Return an integer array answer, where answer[i] is the second greater integer of nums[i].
# -------------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 10 ** 9
from random import randint


def second_greater(nums: list[int]) -> list[int]:
    # working_sol (89.69%, 100%) -> (840ms, 29.3mb)  time: O(n) | space: O(n)
    # Indexes for which we didn't find any greater yet.
    f_first: list[int] = []
    # Indexes for which we found FIRST greater value.
    f_second: list[int] = []
    for x in range(len(nums)):
        # Everything added in descending order.
        # Which allow us to always correctly remove LOWEST values first.
        # When we find anything greater than value stored, it's SECOND greater.
        # Cuz values stored already found their FIRST greater value.
        while f_second and nums[f_second[-1]] < nums[x]:
            nums[f_second.pop()] = nums[x]
        ascending: list[int] = []
        # If we find something greater, relocate lower value indexes into
        #  another stack, with values having at least 1 value greater than them.
        while f_first and nums[f_first[-1]] < nums[x]:
            ascending.append(f_first.pop())
        # Cuz we're maintaining decreasing order,
        #  when taking [-1] we're actually building ascending array.
        # And we need this values in descending order,
        #  otherwise we will not process LOWEST values first.
        f_second += ascending[::-1]
        # ! Move forward in nums and store the value
        #   in a non-increasing stack for the first greater value. !
        f_first.append(x)
    # Unprocessed indexes:
    # Don't have anything greater.
    for _ in f_first:
        nums[_] = -1
    # Don't have any SECOND greater.
    for _ in f_second:
        nums[_] = -1
    return nums


# Time complexity: O(n) -> worst case should be something like, [7,7,7,7,7,7....9,10] ->
# n - len of input_array^^| -> so we will traverse (n - 2) indexes and add everything into a first_found stack O(n - 2),
#                           and on pre_last index (n - 2) indexes will be added into ascending O(n - 2), then
#                           reversed, again O(n - 2) and on last index again (n - 2) values will be used to replace
#                           indexes with SECOND greater O(n - 2) => O(4 * (n - 2)) -> still linear => O(n).
# Auxiliary space: O(n) -> worst case, there's all equal values, so we will have first_found stack
#                          with all indexes stored => O(n).
#                          If something deletes from first_found it's stored in second_found, so it's still maximum
#                          n indexes stored in both arrays at once => O(n).
# -------------------
# Hints:
# ! Move forward in nums and store the value in a non-increasing stack for the first greater value. !
# Ok. So we're saving everything in a stack, and then relocate this into another stack when find something bigger.
# ! Move the value in the stack to an ordered data structure for the second greater value. !
# If we already stored everything in non-increasing == decreasing, we can just reverse it.
# ! Move value from the ordered data structure for the answer. !
# Ok. Essentially we're just using 2 stacks to store values for which we didn't find anything GREATER == f_first.
# Then after finding first value greater than anything stored, we relocate it into f_second stack. # found_first|second
# And finally when we meet something bigger than values stored in f_second, means we found second greater for them.
# So we can just use this indexes to replace with that second greater value.


test: list[int] = [2, 4, 0, 9, 6]
test_out: list[int] = [9, 6, 6, -1, -1]
assert test_out == second_greater(test)

test = [3, 3]
test_out = [-1, -1]
assert test_out == second_greater(test)

test = [
    948041193, 956656781, 600811962, 61743668, 90683247, 887695757,
    994317126, 738692205, 448632428, 665842111, 688175089, 203233944
]
test_out = [994317126, -1, 994317126, 887695757, 994317126, -1, -1, -1, 688175089, -1, -1, -1]
assert test_out == second_greater(test)

test = [randint(0, 10 ** 9) for _ in range(10 ** 4)]
print(test)
