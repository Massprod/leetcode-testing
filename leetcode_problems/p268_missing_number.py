# Given an array nums containing n distinct numbers in the range [0, n],
#   return the only number in the range that is missing from the array.
# ----------------------
# n == nums.length
# 1 <= n <= 10 ** 4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
# ----------------------
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


def missing_number(nums: list[int]) -> int:
    # working_sol (98.84%, 97.25%) -> (117ms, 17.57mb)  time: O(n) | space: O(1)
    range_sum: int = 0
    # Any range will always give same sum,
    # and we need to find only 1 missing value.
    # So we can just summarize correct range ->
    for digit in range(1, len(nums) + 1):
        range_sum += digit
    # -> and subtract everything from incorrect range.
    for num in nums:
        range_sum -= num
    # What's left is missing value.
    return range_sum


# Time complexity: O(n) -> summarizing correct range with the same size as input_array => O(n) ->
# n - len of input_array^^| -> extra to this traversing input_array and subtract everything from summ => O(n) ->
#                           -> O(n + n) => O(2n) => O(n).
# Auxiliary space: O(1) -> only 1 extra INT is used, doesn't depend on input => O(1).
# ----------------------
# Ok. For the follow_up it should be correct to do in O(2n) ->
# -> summarize everything in 1 -> len(nums) + 1, it's the same as range(0, n) and just subtract everything from input.


test: list[int] = [3, 0, 1]
test_out: int = 2
assert test_out == missing_number(test)

test = [0, 1]
test_out = 2
assert test_out == missing_number(test)

test = [9, 6, 4, 2, 3, 5, 7, 0, 1]
test_out = 8
assert test_out == missing_number(test)
