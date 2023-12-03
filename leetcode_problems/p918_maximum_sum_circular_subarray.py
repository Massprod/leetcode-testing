# Given a circular integer array nums of length n,
#  return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array.
# Formally, the next element of nums[i] is nums[(i + 1) % n]
#  and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once.
# Formally, for a subarray nums[i], nums[i + 1], ..., nums[j],
#  there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
# ---------------------
# n == nums.length
# 1 <= n <= 3 * 10 ** 4
# -3 * 10 ** 4 <= nums[i] <= 3 * 10 ** 4
from random import randint


def max_subarray_sum_circular(nums: list[int]) -> int:
    # working_sol (9.83%, 39.86%) -> (460ms, 21.1mb)  time: O(n) | space: O(n)
    min_value: int = -3 * 10 ** 4  # ! -3 * 10 ** 4 <= nums[i] <= 3 * 10 ** 4 !
    # suffixes[x] == maximum subarray we can have in slice: end -> x, (x not included)
    suffixes: list[int] = [0 for _ in range(len(nums) - 1)] + [min_value]
    max_sub: int = 0
    for x in range(len(nums) - 2, -1, -1):
        max_sub += nums[x + 1]
        suffixes[x] = max(max_sub, suffixes[x + 1])
    # (prefix + suffix) == maximised subarray we can build: 0 -> x <- end (circular)
    pref_suf_sum: int = min_value
    # maximum subarray we can have in slice: 0 -> x, (x not included)
    prefix: int = 0
    # Kadane's for maximized subarray we can build in slice: x -> end, inclusive.
    max_sub_sum: int = min_value
    cur_sub_sum: int = 0
    for x in range(len(nums)):
        cur_sub_sum += nums[x]
        max_sub_sum = max(max_sub_sum, cur_sub_sum)
        if cur_sub_sum < 0:
            cur_sub_sum = 0
        if x > 0:
            prefix += nums[x - 1]
        pref_suf_sum = max(
            pref_suf_sum,
            prefix + nums[x] + suffixes[x],  # max_sub on left side + cur_value + max_sub on right side
        )
    # Either subarray: x -> end, or 0 -> x <- end (circular).
    return max(max_sub_sum, pref_suf_sum)


# Time complexity: O(n) <- n - length of input array 'nums'.
# Recreating original array as 'suffixes' => O(n).
# Traverse of (n - 1) elements to get all suffixes => O(n - 1).
# Traverse of the whole array 'nums' to get Kadane's subarray + circular subarray => O(n).
# Auxiliary space: O(n)
# 6 constant INTs, which doesn't depend on input + array with same size as input array 'nums' => O(n).


test: list[int] = [1, -2, 3, -2]
test_out: int = 3
assert test_out == max_subarray_sum_circular(test)

test = [5, -3, 5]
test_out = 10
assert test_out == max_subarray_sum_circular(test)

test = [-3, -2, -3]
test_out = -2
assert test_out == max_subarray_sum_circular(test)

test = [
    13580, 23627, -6867, 14708, -5581, -24629, -9117, 9199, 4381, -5102, -2279, 593, 4247,
    4277, -6271, 7884, 26802, 3518, 22092, -23358, 9735, 1022, -8707, 14975, -11212, -19740,
    16166, 12465, 5881, -26502
]
test_out = 85114
assert test_out == max_subarray_sum_circular(test)

# test = [randint(-3 * 10 ** 4, 3 * 10 ** 4) for _ in range(3 * 10 ** 4)]
# print(test)
