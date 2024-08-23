# You are given a 0-indexed integer array nums.
# You are also given an integer key, which is present in nums.
# For every unique integer target in nums, count the number of times target
#  immediately follows an occurrence of key in nums.
# In other words, count the number of indices i such that:
#  - 0 <= i <= nums.length - 2,
#  - nums[i] == key and,
#  - nums[i + 1] == target.
# Return the target with the maximum count.
# The test cases will be generated such that the target with maximum count is unique.
# ----------------------
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# The test cases will be generated such that the answer is unique.
from collections import defaultdict


def most_frequent(nums: list[int], key: int) -> int:
    # working_sol (60.11%, 41.21%) -> (74ms, 16.77mb)  time: O(n) | space: O(n)
    targets: dict[int, int] = defaultdict(int)
    for index in range(1, len(nums)):
        if nums[index - 1] == key:
            targets[nums[index]] += 1
    out: int = 0
    cur_count: int = 0
    for target, count in targets.items():
        if count > cur_count:
            cur_count = count
            out = target
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums`, once => O(n).
# In the worst case there's only unique targets and every single one of them positioned after `key`.
# Extra traversing `n / 2` targets in `targets` => O(n + n / 2).
# ----------------------
# Auxiliary space: O(n)
# `targets` <- allocates space for all of these targets => O(n).


test: list[int] = [1, 100, 200, 1, 100]
test_key: int = 1
test_out: int = 100
assert test_out == most_frequent(test, test_key)

test = [2, 2, 2, 2, 3]
test_key = 2
test_out = 2
assert test_out == most_frequent(test, test_key)
