# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
#   find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where
#   1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2,
#   added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
# Your solution must use only constant extra space.
# -------------------
# 2 <= numbers.length <= 3 * 10 ** 4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
from random import randint


def two_sum(numbers: list[int], target: int) -> list[int]:
    # working_sol (7.33%, 94.99%) -> (188ms, 17.1mb)  time: O(n * log n) | space: O(1)
    for x in range(len(numbers)):
        to_find: int = target - numbers[x]
        left: int = 0
        right: int = len(numbers) - 1
        # lower than lowest, higher than highest
        if not numbers[left] <= to_find <= numbers[right]:
            continue
        # standard binary search
        while right >= left:
            middle: int = (left + right) // 2
            # [index1, index2] left to right
            # and zero_indexed by default, we need to return 1 indexed
            if to_find == numbers[left]:
                if left != x:
                    return sorted([x + 1, left + 1])
                break
            if to_find == numbers[right]:
                if right != x:
                    return sorted([x + 1, right + 1])
                break
            if to_find == numbers[middle]:
                if middle != x:
                    return sorted([x + 1, middle + 1])
                break
            if to_find < numbers[middle]:
                right = middle - 1
                continue
            if to_find > numbers[middle]:
                left = middle + 1
                continue


# Time complexity: O(n * log n) -> for every index(value) in input_array we're going to perform binary_search in
# n - len of input_array^^|        this array, standard binary search is O(log n) => O(n * log n).
# Auxiliary space: O(1) -> using 4 extra INTs, none of them depends on input => O(1).
# -------------------
# Rushed and didn't take a break after BT task, failed 2 commits and missed most basic parts.
# Like middle and break when found index is same as x...
# -------------------
# Before I just stored every possible numbers[x] - target and just searched for this.
# Now we can't use any storage, so it's should be binary search.


test1 = [2, 7, 11, 15]
test1_t = 9
test1_out = [1, 2]
print(two_sum(test1, test1_t))
assert test1_out == two_sum(test1, test1_t)

test2 = [2, 3, 4]
test2_t = 6
test2_out = [1, 3]
print(two_sum(test2, test2_t))
assert test2_out == two_sum(test2, test2_t)

test3 = [-1, 0]
test3_t = -1
test3_out = [1, 2]
print(two_sum(test3, test3_t))
assert test3_out == two_sum(test3, test3_t)

# test4 -> failed -> I forgot to ignore duplicated indexes...
test4 = [0, 0, 3, 4]
test4_t = 0
test4_out = [1, 2]
print(two_sum(test4, test4_t))
assert test4_out == two_sum(test4, test4_t)

# test5 -> failed -> Always take a break after hard tasks, forgot to add correct calc for the  middle
#                    and just used -> len(numbers) // 2  ...
test5 = [3, 24, 50, 79, 88, 150, 345]
test5_t = 200
test5_out = [3, 6]
print(two_sum(test5, test5_t))
assert test5_out == two_sum(test5, test5_t)
