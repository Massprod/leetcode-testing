# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index
#   is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.
# --------------------
# 1 <= nums.length <= 10 ** 4
# -1000 <= nums[i] <= 1000


def pivot_index(nums: list[int]) -> int:
    # working_sol (95.08%, 96.62%) -> (132ms, 17.42mb)  time: O(n) | space: O(1)
    # Going from left -> right.
    # [0] start, prefix == 0 always.
    prefix: int = 0
    # Suffix for [0] sum() of everything else.
    suffix: int = sum(nums[1:])
    # Unique check for [0]
    if prefix == suffix:
        return 0
    for x in range(1, len(nums)):
        # Every step its increase of prefix,
        # and decrease of suffix.
        prefix += nums[x - 1]
        suffix -= nums[x]
        # Same check.
        # We can insta return, cuz left -> right.
        if prefix == suffix:
            return x
    return -1


# Time complexity: O(n) -> traversing input_array for n - 1 indexes, twice => O(2 * (n - 1)) => O(n).
# Auxiliary space: O(1) -> only 2 constant INTs used, none of them depends on input => O(1).
# --------------------
# Check suffix|prefix and return first occurrence, starting from left -> right with suffix taken first.


test: list[int] = [1, 7, 3, 6, 5, 6]
test_out: int = 3
assert test_out == pivot_index(test)

test = [1, 2, 3]
test_out = -1
assert test_out == pivot_index(test)

test = [2, 1, -1]
test_out = 0
assert test_out == pivot_index(test)
