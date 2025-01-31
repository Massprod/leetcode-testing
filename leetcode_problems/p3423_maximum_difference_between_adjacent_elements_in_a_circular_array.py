# Given a circular array nums, find the maximum absolute difference
#  between adjacent elements.
# Note: In a circular array, the first and last elements are adjacent.
# ---------------------
# 2 <= nums.length <= 100
# -100 <= nums[i] <= 100


def max_adjacent_distance(nums: list[int]) -> int:
    # working_sol (100.00%, 65.68%) -> (0ms, 17.76mb)  time: O(n) | space: O(1)
    out: int = 0

    for index in range(1, len(nums)):
        out = max(out, abs(nums[index] - nums[index - 1]))

    return max(out, abs(nums[-1] - nums[0]))


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ---------------------
# Auxiliary space: O(1)
# Only 1 constant INT is used => O(1).


test: list[int] = [1, 2, 4]
test_out: int = 3
assert test_out == max_adjacent_distance(test)

test = [-5, -10, -5]
test_out = 5
assert test_out == max_adjacent_distance(test)
