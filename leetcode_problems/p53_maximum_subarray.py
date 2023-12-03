# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# -------------------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 4 <= nums[i] <= 10 ** 4


def max_sub_array(nums: list[int]) -> int:
    # working_sol (93.10%, 88.7%) -> (561ms, 30.4mb)  time: O(n) | space: O(1)
    # Standard Kadane's algorithm.
    # Build maximum possible subarray with positive summ.
    # If it goes to negative, start a new subarray from the next value.
    max_sub_sum: int = -10000  # -10 ** 4 <- minimum possible.
    current_sub_sum: int = 0
    for x in range(len(nums)):
        current_sub_sum += nums[x]
        max_sub_sum = max(current_sub_sum, max_sub_sum)
        if current_sub_sum < 0:
            current_sub_sum = 0
    return max_sub_sum


# Time complexity: O(n) -> single traverse of whole input array 'nums' => O(n).
# n - length of input array 'nums'^^|
# Space complexity: O(1) -> only 2 extra INTs used, none of them depends on input => O(1).
# -------------------------
# The idea of Kadane’s algorithm is to maintain a variable max_ending_here that stores the maximum sum.
# Contiguous subarray ending at current index and a variable max_so_far stores the maximum sum of
# contiguous subarray found so far. Everytime there is a positive-sum value in max_ending_here compare
# it with max_so_far and update max_so_far if it is greater than max_so_far.
# ^^


test: list[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test_out: int = 6
assert test_out == max_sub_array(test)

test = [1]
test_out = 1
assert test_out == max_sub_array(test)

test = [5, 4, -1, 7, 8]
test_out = 23
assert test_out == max_sub_array(test)

test = [-2, -1]
test_out = -1
assert test_out == max_sub_array(test)

test = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]
test_out = 6
assert test_out == max_sub_array(test)

test = [0, 0, -3, 1]
test_out = 1
assert test_out == max_sub_array(test)
