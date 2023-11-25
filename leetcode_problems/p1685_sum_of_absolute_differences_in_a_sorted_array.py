# You are given an integer array nums sorted in non-decreasing order.
# Build and return an integer array result with the same length as nums
#  such that result[i] is equal to the summation of absolute differences between nums[i]
#  and all the other elements in the array.
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|)
#  where 0 <= j < nums.length and j != i (0-indexed).
# --------------------
# 2 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= nums[i + 1] <= 10 ** 4
from random import randint


def get_sum_abs_diff(nums: list[int]) -> list[int]:
    # working_sol (74.68%, 30.45%) -> (715ms, 31.8mb)  time: O(n) | space: O(n)
    # abs(a, b) == max(a, b) - min(a, b)
    # result[x] == (nums[x] * count(everyth_lower) - sum(everyth_lower)) +
    #              + (sum(everyth_higher) - nums[x] * count(everyth_higher))
    # `nums` already sorted, all we need is (prefix and suffix) of every index.
    # OR we can just use sum(nums) and calc suffix and suffix on the way.
    #   suffix[x] == sum(nums) - (nums[x] for every x step)
    prefix: int = 0
    suffix: int = sum(nums)
    out: list[int] = []
    for x in range(len(nums)):
        out.append(
            (nums[x] * x - prefix) + (suffix - nums[x] - nums[x] * (len(nums) - 1 - x))  # -1 for 0-indexed.
        )
        prefix += nums[x]
        suffix -= nums[x]
    return out


# Time complexity: O(n) -> traversing once to get sum(nums) + extra traverse to get all results => O(n).
# n - len of input array 'nums'^^|
# Auxiliary space: O(n) -> list with size of original input array + 2 constant INTs => O(n).


test: list[int] = [2, 3, 5]
test_out: list[int] = [4, 3, 5]
assert test_out == get_sum_abs_diff(test)

test = [1, 4, 6, 8, 10]
test_out = [24, 15, 13, 15, 21]
assert test_out == get_sum_abs_diff(test)

test = sorted([randint(1, 10 ** 4) for _ in range(10 ** 4)])
# print(test)
