# Given an unsorted array of integers nums,
#  return the length of the longest continuous increasing subsequence (i.e. subarray).
# The subsequence must be strictly increasing.
# A continuous increasing subsequence is defined by two indices l and r (l < r)
#  such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]
#  and for each l <= i < r, nums[i] < nums[i + 1].
# ----------------------
# 1 <= nums.length <= 10 ** 4
# -10 ** 9 <= nums[i] <= 10 ** 9
from random import randint


def find_length_of_lcis(nums: list[int]) -> int:
    # working_sol (66.21%, 68.40%) -> (66ms, 17.90mb)  time: O(n) | space: O(1)
    out: int = 1
    cur_seq: int = 1
    # Start from `1`, because we always start with at least 1 value used.
    for index in range(1, len(nums)):
        if nums[index - 1] < nums[index]:
            cur_seq += 1
        else:
            out = max(cur_seq, out)
            cur_seq = 1
    # The Sequence may not be broken, extra check.
    return max(out, cur_seq)

# Time complexity: O(n) <- n - length of the input array `nums`.
# We're always traversing whole input array `nums`, once => O(n).
# ----------------------
# Auxiliary space: O(1).
# Only 2 constant INT's used, none of them depends on input => O(1).


test: list[int] = [1, 3, 5, 4, 7]
test_out: int = 3
assert test_out == find_length_of_lcis(test)

test = [2, 2, 2, 2, 2]
test_out = 1
assert test_out == find_length_of_lcis(test)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 4)]
print(test)
