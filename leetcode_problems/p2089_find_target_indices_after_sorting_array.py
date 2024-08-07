# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order.
# If there are no target indices, return an empty list.
# The returned list must be sorted in increasing order.
# ------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i], target <= 100


def target_indices(nums: list[int], target: int) -> list[int]:
    # working_sol (74.48%, 96.33%) -> (45ms, 16.40mb)  time: O(n * log n) | space: O(n)
    nums.sort()
    out: list[int] = []
    for index, val in enumerate(nums):
        if target == val:
            out.append(index)
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`
# Always sorting with builtin `sort` => O(n * log n).
# Extra traversing whole `nums` to get correct indexes => O(n + n * log n).
# ------------------------
# Auxiliary space: O(n)
# `out` <- can be of size `n` when every `val` == `target` => O(n).
# And `sort` takes O(n) by itself => O(2 * n)


test: list[int] = [1, 2, 5, 2, 3]
test_target: int = 2
test_out: list[int] = [1, 2]
assert test_out == target_indices(test, test_target)

test = [1, 2, 5, 2, 3]
test_target = 3
test_out = [3]
assert test_out == target_indices(test, test_target)

test = [1, 2, 5, 2, 3]
test_target = 5
test_out = [4]
assert test_out == target_indices(test, test_target)
