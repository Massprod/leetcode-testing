# Given an array of positive integers nums and a positive integer target,
#  return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
# --------------------
# Follow up: If you have figured out the O(n) solution,
#  try coding another solution of which the time complexity is O(n log(n)).
# --------------------
# 1 <= target <= 10 ** 9
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 4


def min_subarray_len(target: int, nums: list[int]) -> int:
    # working_sol (86.32%, 41.5%) -> (254ms, 29.1mb)  time: O(n) | space: O(1)
    length: int = len(nums)
    # unique case with len == 1
    if length == 1:
        if target <= nums[0]:
            return 1
        return 0
    # set as 0, to easier return of len(sub) == 0
    min_sub: int = 0
    left: int = 0
    right: int = 0
    min_sum: int = 0
    while right != length:
        # expand
        min_sum += nums[right]
        # shrink
        while min_sum >= target:
            # because I set as 0, it's necessary check
            if min_sub == 0:
                min_sub = (right - left) + 1
            else:
                min_sub = min(min_sub, (right - left) + 1)
            min_sum -= nums[left]
            left += 1
        right += 1
    return min_sub


# Time complexity: O(n) -> standard sliding window approach with traversing whole input_array once => O(n) ->
# n - len of nums^^|      -> and shrinking that window with extra steps of (n - 2), in the worst case => O(n - 2) ->
#                         -> O(n) + O(n - 2) ~= O(2n) => O(n).
# Auxiliary space: O(1) -> using only constants, none of them depends on input => O(1).
# --------------------
# Window problem with easy solution of O(n), but what is solution for O(n * (log n))?
# It should something like: summarize every index with part of the input array
#  and choose min() of all that sum() actions.
# Strange, if there's no TLE for that approach than it should be it, but I doubt.
# It's going to be almost like O(n * n), but we exclude only indexes we already checked.
# W.e doing O(n) and extra search for follow_up.


test1 = [2, 3, 1, 2, 4, 3]
test1_target = 7
test1_out = 2
print(min_subarray_len(test1_target, test1))
assert test1_out == min_subarray_len(test1_target, test1)

test2 = [1, 4, 4]
test2_target = 4
test2_out = 1
print(min_subarray_len(test2_target, test2))
assert test2_out == min_subarray_len(test2_target, test2)

test3 = [1, 1, 1, 1, 1, 1, 1, 1]
test3_target = 11
test3_out = 0
print(min_subarray_len(test3_target, test3))
assert test3_out == min_subarray_len(test3_target, test3)

test4 = [1]
test4_target = 1
test4_out = 1
print(min_subarray_len(test4_target, test4))
assert test4_out == min_subarray_len(test4_target, test4)

test5 = [0]
test5_target = 1
test5_out = 0
print(min_subarray_len(test5_target, test5))
assert test5_out == min_subarray_len(test5_target, test5)
