# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.

# The idea of Kadane’s algorithm is to maintain a variable max_ending_here that stores the maximum sum
# contiguous subarray ending at current index and a variable max_so_far stores the maximum sum of
# contiguous subarray found so far, Everytime there is a positive-sum value in max_ending_here compare
# it with max_so_far and update max_so_far if it is greater than max_so_far.
# ^^

def max_sub_array(nums: list[int]) -> int:
    # working_sol (94.96%, 12.97%) -> (660ms, 30.8mb)  time: O(n) | space: O(1)
    if len(nums) == 1:
        return nums[0]
    max_sub_sum: int = -10001  # -10**4 <= nums[i] <= 10**4
    max_step_sum: int = 0
    for x in range(0, len(nums)):
        max_step_sum += nums[x]
        if max_step_sum > max_sub_sum:
            max_sub_sum = max_step_sum
        if max_step_sum < 0:
            max_step_sum = 0
    return max_sub_sum

# Time complexity: O(n) -> one whole loop through input array.
# Space complexity: O(1) -> only input used, no extras.

# Googled Kadane's algorithm, which is actually a solution.
# I was trying to use most simple conquer_divide, and it's not a case here. It can be solved with conquer_divide,
# and speed O(log n), but I don't think I'm capable of doing it myself and maybe revisit later.
# Cuz google or gpt can be done anytime. I need to do it myself, otherwise it's pointless.
# Right now is better to move, at least I made it with Kadane.
# (without Kadane it could be done easily with summing every index one_by_one for every slice 100% time_limit tho.)


test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test1_out = 6
assert test1_out == max_sub_array(test1)
print(max_sub_array(test1))

test2 = [1]
test2_out = 1
assert test2_out == max_sub_array(test2)
print(max_sub_array(test2))

test3 = [5, 4, -1, 7, 8]
test3_out = 23
assert test3_out == max_sub_array(test3)
print(max_sub_array(test3))

test4 = [-2, -1]
test4_out = -1
assert test4_out == max_sub_array(test4)
print(max_sub_array(test4))

test5 = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]
test5_out = 6
assert test5_out == max_sub_array(test5)
print(max_sub_array(test5))

test6 = [0, 0, -3, 1]
test6_out = 1
assert test6_out == max_sub_array(test6)
print(max_sub_array(test6))
