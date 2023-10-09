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
    # working_sol (91.12%, 50.97%) -> (77ms, 17.72mb)  time: O(log n) | space: O(1)
    if not nums:
        return [-1, -1]
    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        return [-1, -1]
    if nums[0] == nums[-1] == target:
        return [0, len(nums) - 1]

    def bs(left_l: int, right_l: int, first: bool) -> int:
        out: int = -1
        while left_l <= right_l:
            middle: int = (left_l + right_l) // 2
            if nums[middle] == target:
                out = middle
                # Shift to left side for most_left(first) index.
                if first:
                    right_l = middle - 1
                # Shift to right side for most_right(last) index.
                else:
                    left_l = middle + 1
            # Need higher.
            elif nums[middle] < target:
                left_l = middle + 1
            # Need lower.
            elif nums[middle] > target:
                right_l = middle - 1
        return out

    left_index: int = bs(0, len(nums) - 1, True)
    right_index: int = left_index
    # If there's no target, no reasons to search last_index.
    if left_index >= 0:
        right_index = bs(0, len(nums) - 1, False)
    return [left_index, right_index]


# Time complexity: O(log n) -> worst case == 2 indexes to find -> we will use BS on array twice => O(2 * log n).
# n - len of input array^^|
# Auxiliary space: O(1) -> always constant INTs used, none of them depends on input => O(1).
# --------------------
# Before it was O(n), and for O(log n) it's always BS in such cases.
# But we can't just find 1 element, so it should continue until we choose most_left|right elements.
# Shift search into left side when we search for a left_element, and right side for right_element.
# Like: left_element => right = middle - 1, right_element => left = middle + 1.
# Everything else should be ok. Only problem is that we need to BSearch twice, for left and right.


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
