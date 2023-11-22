# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# -------------------
# 1 <= nums.length <= 10 ** 4
# -10 ** 4 <= nums[i] <= 10 ** 4
# nums contains distinct values sorted in ascending order.
# -10 ** 4 <= target <= 10 ** 4


def search_insert(nums: list[int], target: int) -> int:
    # working_sol (39.71%, 59.38%) -> (57ms, 17mb)  time: O(log n) | space: O(1)
    # Standard BinarySearch.
    left_l: int = 0
    right_l: int = len(nums) - 1
    while left_l <= right_l:
        middle: int = (left_l + right_l) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left_l = middle + 1
        else:
            right_l = middle - 1
    return left_l


# Time complexity: O(log n) -> standard BS on array => O(log n).
# n - length of input array 'nums'^^|
# Space complexity: O(1) -> only 3 constant INTs none of them depends on input => O(1).


test: list[int] = [1, 3, 5, 6]
test_target: int = 5
test_out: int = 2
assert test_out == search_insert(test, test_target)

test = [1, 3, 5, 6]
test_target = 2
test_out = 1
assert test_out == search_insert(test, test_target)
