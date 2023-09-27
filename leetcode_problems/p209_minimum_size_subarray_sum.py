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
    # working_sol (72.34%, 78.89%) -> (218ms, 29.5mb)  time: O(n) | space: O(1)
    # Unique case with len == 1.
    if len(nums) == 1:
        if target <= nums[0]:
            return 1
        return 0
    # ! If there is no such subarray, return 0 instead. !
    min_sub: int = 0
    left: int = 0
    right: int = 0
    min_sum: int = 0
    # Standard sliding window.
    while right != len(nums):
        # Expand.
        min_sum += nums[right]
        # Shrink.
        while min_sum >= target:
            # Because default == 0, it's necessary for 1 option.
            if not min_sub:
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


test: list[int] = [2, 3, 1, 2, 4, 3]
test_target: int = 7
test_out: int = 2
assert test_out == min_subarray_len(test_target, test)

test = [1, 4, 4]
test_target = 4
test_out = 1
assert test_out == min_subarray_len(test_target, test)

test = [1, 1, 1, 1, 1, 1, 1, 1]
test_target = 11
test_out = 0
assert test_out == min_subarray_len(test_target, test)

test = [1]
test_target = 1
test_out = 1
assert test_out == min_subarray_len(test_target, test)

test = [0]
test_target = 1
test_out = 0
assert test_out == min_subarray_len(test_target, test)
