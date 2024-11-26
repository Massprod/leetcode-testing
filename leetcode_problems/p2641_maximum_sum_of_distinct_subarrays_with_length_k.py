# You are given an integer array nums and an integer k.
# Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
#  - The length of the subarray is k, and
#  - All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions
# If no subarray meets the conditions, return 0.
# A subarray is a contiguous non-empty sequence of elements within an array.
# ------------------------
# 1 <= k <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5
from random import randint


def maximum_subarray_sum(nums: list[int], k: int) -> int:
    # working_sol (43.45%, 6.50%) -> (132ms, 42.7mb)  time: O(n) | space: O(n)
    out: int = 0
    # First window
    uniques_counter: dict[int, int] = {}
    for val in nums[:k]:
        uniques_counter[val] = uniques_counter.get(val, 0) + 1
    uniques: set[int] = set(nums[:k])
    cur_sum: int = sum(nums[:k])
    if k == len(uniques):
        out = cur_sum
    # Standard `sliding_window`.
    left: int = 0
    right: int = k - 1
    while right < len(nums) - 1:
        cur_sum -= nums[left]
        uniques_counter[nums[left]] -= 1
        # Only remove from `uniques` if none present.
        if 0 == uniques_counter[nums[left]]:
            uniques.remove(nums[left])
        left += 1
        right += 1
        uniques.add(nums[right])
        uniques_counter[nums[right]] = uniques_counter.get(nums[right], 0) + 1
        cur_sum += nums[right]
        if k == len(uniques):
            out = max(out, cur_sum)
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# Every index can be used at most 2 times, once to add into uniques and counter and once to delete => O(n).
# ------------------------
# Auxiliary space: O(n)
# In the worst case there's input array `nums` with `k` elements in it, and all of them unique.
# `uniques_counter` <- allocates space for each unique value from `nums` => O(n).
# `uniques` <- allocates space for each unique value from `nums` with limit `k` == len(nums) => O(2 * n).


test: list[int] = [1, 5, 4, 2, 9, 9, 9]
test_k: int = 3
test_out: int = 15
assert test_out == maximum_subarray_sum(test, test_k)

test = [4, 4, 4]
test_k = 3
test_out = 0
assert test_out == maximum_subarray_sum(test, test_k)

test = [1, 1, 1, 7, 8, 9]
test_k = 3
test_out = 24
assert test_out == maximum_subarray_sum(test, test_k)

test = [9, 9, 9, 1, 2, 3]
test_k = 3
test_out = 12
assert test_out == maximum_subarray_sum(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(10 ** 3)]
print(test)
