# You are given a 0-indexed integer array nums.
# The distinct count of a subarray of nums is defined as:
#  - Let nums[i..j] be a subarray of nums consisting of all the indices from i to j
#   such that 0 <= i <= j < nums.length.
#   Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.
# --------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def sum_counts(nums: list[int]) -> int:
    # working_sol (39.94%, 78.03%) -> (155ms, 16.41mb)  time: O(n ** 3) | space: O(n)
    out: int = 0
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            uniques: set[int] = set(nums[start: end + 1])
            out += len(uniques) ** 2
    return out


# Time complexity: O(n ** 3) <- n - length of the input array `nums`.
# Always traversing whole `nums` with nested loop, starting from `0` index => O(n * n).
# And for each iteration we're slicing an original array, and in the worst case, it's whole array size => O(n * n * n).
# --------------------------
# Auxiliary space: O(n)
# `uniques` <- allocates space for each value from `nums` => O(n).


test: list[int] = [1, 2, 1]
test_out: int = 15
assert test_out == sum_counts(test)

test = [1, 1]
test_out = 3
assert test_out == sum_counts(test)
