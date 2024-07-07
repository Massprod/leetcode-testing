# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice
#  as much as every other number in the array.
# If it is, return the index of the largest element, or return -1 otherwise.
# -------------------------
# 2 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.


def dominant_index(nums: list[int]) -> int:
    # working_sol (98.23%, 63.64%) -> (28ms, 16.44mb)  time: O(n) | space: O(n)
    out: int = -1
    highest: int = -1
    second_highest: int = -1
    for index, num in enumerate(nums):
        if num > highest:
            highest, second_highest = num, highest
            out = index
        elif num > second_highest:
            second_highest = num
    return out if (highest >= second_highest * 2) else -1


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing input array `nums`, once => O(n).
# -------------------------
# Auxiliary space: O(n)
# Everything is constant, except `enumerate` it will create an extra with `n` size => O(n)


test: list[int] = [3, 6, 1, 0]
test_out: int = 1
assert test_out == dominant_index(test)

test = [1, 2, 3, 4]
test_out = -1
assert test_out == dominant_index(test)
