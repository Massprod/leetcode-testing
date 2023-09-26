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


def two_sum(numbers: list[int], target: int) -> list[int]:
    # working_sol (69.93%, 85.26%) -> (117ms, 17.14mb)  time: O(n) | space: O(1)
    left: int = 0
    right: int = len(numbers) - 1
    while left < right:
        cur_sum: int = numbers[left] + numbers[right]
        if cur_sum == target:
            # zero_indexed -> 1_indexed
            return [left + 1, right + 1]
        # ! already sorted in non-decreasing order !
        # Make second value lower.
        if cur_sum > target:
            right -= 1
        # Make first value higher.
        if cur_sum < target:
            left += 1


# Time complexity: O(n) -> in the worst_case answer is indexes: first = (len(numbers) // 2) and sec = first + 1 ->
# n - len of input_array^^| -> then we need to travel whole input_array until we find it => O(n).
# Auxiliary space: O(1) -> using 3 extra INTs, none of them depends on input => O(1).


test: list[int] = [2, 7, 11, 15]
test_t: int = 9
test_out: list[int] = [1, 2]
assert test_out == two_sum(test, test_t)

test = [2, 3, 4]
test_t = 6
test_out = [1, 3]
assert test_out == two_sum(test, test_t)

test = [-1, 0]
test_t = -1
test_out = [1, 2]
assert test_out == two_sum(test, test_t)

test = [0, 0, 3, 4]
test_t = 0
test_out = [1, 2]
assert test_out == two_sum(test, test_t)

test = [3, 24, 50, 79, 88, 150, 345]
test_t = 200
test_out = [3, 6]
assert test_out == two_sum(test, test_t)
