# You are given a 0-indexed integer array nums having length n,
#  an integer indexDifference, and an integer valueDifference.
# Your task is to find two indices i and j, both in the range [0, n - 1],
#  that satisfy the following conditions:
#  - abs(i - j) >= indexDifference, and
#  - abs(nums[i] - nums[j]) >= valueDifference
# Return an integer array answer, where answer = [i, j] if there are two such indices,
#  and answer = [-1, -1] otherwise.
# If there are multiple choices for the two indices, return any of them.
# Note: i and j may be equal.
# -----------------------
# 1 <= n == nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= indexDifference <= 100
# 0 <= valueDifference <= 50


def find_indices(
    nums: list[int],
    indexDifference: int,
    valueDifference: int,
) -> list[int]:
    # working_sol (100.00%, 63.33%) -> (0ms, 17.78mb)  time: O(n * n) | space: O(1)
    for first in range(0, len(nums) - indexDifference):
        for second in range(first + indexDifference, len(nums)):
            if abs(nums[first] - nums[second]) >= valueDifference:
                return [first, second]
            
    return [-1, -1]


# Time complexity: O(n * n) <- n - length of the input array `nums`.
# In the worst case `indexDifference` == 0 and none of the indexes
#  will give as `valueDifference`.
# In that case, we're going to check all of the index pairs => O(n * n).
# -----------------------
# Auxiliary space: O(1)
# Nothing extra is used.


test: list[int] = [5, 1, 4, 1]
test_ind_diff: int = 2
test_val_diff: int = 4
test_out: list[int] = [0, 3]
assert test_out == find_indices(test, test_ind_diff, test_val_diff)

test = [2, 1]
test_ind_diff = 0
test_val_diff = 0
test_out = [0, 0]
assert test_out == find_indices(test, test_ind_diff, test_val_diff)

test = [1, 2, 3]
test_ind_diff = 2
test_val_diff = 4
test_out = [-1, -1]
assert test_out == find_indices(test, test_ind_diff, test_val_diff)
