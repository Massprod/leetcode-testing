# Given an array of integers nums sorted in non-decreasing order,
#  find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# --------------------
# 0 <= nums.length <= 10 ** 5
# -10 ** 9 <= nums[i] <= 10 ** 9
# nums is a non-decreasing array.
# -10 ** 9 <= target <= 10 ** 9
from random import randint


def search_range(nums: list[int], target: int) -> list[int]:
    # working_sol (90.90%, 35.88%) -> (77ms, 17.74mb)  time: O(log n) | space: O(1)
    if not nums:
        return [-1, -1]
    # All values duplicates and equal to 'target'.
    if nums[0] == nums[-1] == target:
        return [0, len(nums) - 1]

    def binary_search(left: int, right: int, first: bool) -> int:
        if first:
            while left < right:
                middle: int = (left + right) // 2
                if nums[middle] >= target:
                    right = middle
                else:
                    left = middle + 1
        else:
            while left < right:
                # To find most right_index we need round 'middle' for higher int, or +1.
                # Then we can always make +1 step on 'left == middle' until reaching the 'right'.
                middle = (left + right) // 2 + 1
                if nums[middle] <= target:
                    left = middle
                else:
                    right = middle - 1
        return left

    left_index: int = binary_search(0, len(nums) - 1, True)
    # If there's no 'target' in the array 'nums', no reasons to search for other index.
    if nums[left_index] == target:
        right_index: int = binary_search(left_index, len(nums) - 1, False)
    else:
        return [-1, -1]
    return [left_index, right_index]


# Time complexity: O(log n) <- n length of input array 'nums'.
# BinarySearch on whole array 'nums' first.
# And if we found 'target', extra search for the rightmost index.
# Worst case == [1,1,1,1,1,1 ... 1, 2], target == 1.
# We will find [0] index of leftmost, and we will BS again to get rightmost index.
# And limits to search in both cases will be 0 -> len(nums) - 1.
# O(2 * log n).
# --------------------
# Auxiliary space: O(1)
# Only constants used, none of them depends on input.


test: list[int] = [5, 7, 7, 8, 8, 10]
test_target: int = 8
test_out: list[int] = [3, 4]
assert test_out == search_range(test, test_target)

test = [5, 7, 7, 8, 8, 10]
test_target = 6
test_out = [-1, -1]
assert test_out == search_range(test, test_target)

test = []
test_target = 0
test_out = [-1, -1]
assert test_out == search_range(test, test_target)

test = [1]
test_target = 1
test_out = [0, 0]
assert test_out == search_range(test, test_target)

test = [1, 10]
test_target = 1
test_out = [0, 0]
assert test_out == search_range(test, test_target)

test = [1, 2, 3]
test_target = 2
test_out = [1, 1]
assert test_out == search_range(test, test_target)

test = [2, 2]
test_target = 1
test_out = [-1, -1]
assert test_out == search_range(test, test_target)

test = [1, 2, 2]
test_target = 2
test_out = [1, 2]
assert test_out == search_range(test, test_target)

test = sorted([randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 4)])
print(test)
