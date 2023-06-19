# You are given an integer array nums and an integer x.
# In one operation, you can either remove the leftmost or the rightmost element from the array nums
#   and subtract its value from x. Note that this modifies the array for future operations.
#
# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
# ---------------------------------
# 1 <= nums.length <= 10 ** 5  ,  1 <= nums[i] <= 10 ** 4  ,  1 <= x <= 10 ** 9


def min_operations(nums: list[int], x: int) -> int:
    # working_sol (98.2%, 38.34%) -> (1072ms, 31.1mb)  time: O(n + (log n)) | space: O(1)
    if nums[0] > x and nums[-1] > x:
        return -1
    if nums[0] == x or nums[-1] == x:
        return 1
    length: int = len(nums)
    max_sub_target: int = sum(nums) - x
    # whole array gives sum of x
    if max_sub_target == 0:
        return length
    # whole array gives less than x
    elif max_sub_target < 0:
        return -1
    # assume it's whole array to use
    minimum_operations: int = length
    sub_sum: int = 0
    start_x: int = 0
    for y in range(len(nums)):
        sub_sum += nums[y]
        if sub_sum > max_sub_target:
            # change array_window to continue search
            while start_x <= y and sub_sum > max_sub_target:
                sub_sum -= nums[start_x]
                start_x += 1
        if sub_sum == max_sub_target:
            # remove subarray with max_sub_target in it
            operations: int = length - (y + 1 - start_x)
            minimum_operations = min(operations, minimum_operations)
    return minimum_operations


# Time complexity: O(n + (log n)) -> traversing whole input_list once => O(n) ->
# n - len of input_list^^|  -> but on the way we're creating window, on encounter of window_sum > max_sub_target
#                           changing its size until we hit correct window_sum < max_sub_target ->
#                           -> like in this case [1, 1, 1, 1, 1, 1], x = 2 =>
#                           => we're going to check every index in input_list and 2 extras
#                           due to a change of window size => O(log n) -> O(n + log n).
# Auxiliary space: O(1) -> only extra constants created, creation of them doesn't depends on input => O(1).
# ---------------------------------
# Failed to see that we can't insta return is operations < half, because there can be
# even bigger subarray further to the right to exclude.
# Failed to see solution without hints.
# Failed 3 times before made correct update of an array_window.
# Even Failed to comment correctly !WHORE instead of WHOLE!, what a day...mondays.
# ---------------------------------
# Obviously can be solved with recursion but 99% there's TimeLimit, so how we can decide what to delete?
# Hint is to find max_subarray_sum(window).


test1 = [1, 1, 4, 2, 3]
test1_x = 5
test1_out = 2
print(min_operations(test1, test1_x))
assert test1_out == min_operations(test1, test1_x)

test2 = [5, 6, 7, 8, 9]
test2_x = 4
test2_out = -1
print(min_operations(test2, test2_x))
assert test2_out == min_operations(test2, test2_x)

test3 = [3, 2, 20, 1, 1, 3]
test3_x = 10
test3_out = 5
print(min_operations(test3, test3_x))
assert test3_out == min_operations(test3, test3_x)

test4 = [3, 2, 10, 10, 10, 10, 1, 1, 3]
test4_x = 20
test4_out = 6
print(min_operations(test4, test4_x))
assert test4_out == min_operations(test4, test4_x)

test5 = [5, 4, 3, 3, 3]
test5_x = 9
test5_out = 2
print(min_operations(test5, test5_x))
assert test5_out == min_operations(test5, test5_x)

test6 = [1, 1]
test6_x = 3
test6_out = -1
print(min_operations(test6, test6_x))
assert test6_out == min_operations(test6, test6_x)

test7 = [2, 3, 1, 1, 1]
test7_x = 5
test7_out = 2
print(min_operations(test7, test7_x))
assert test7_out == min_operations(test7, test7_x)
