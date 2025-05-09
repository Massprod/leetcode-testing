# You are given an integer array nums.
# You are allowed to delete any number of elements from nums without making it empty.
# After performing the deletions, select a subarray of nums such that:
#  1. All elements in the subarray are unique.
#  2. The sum of the elements in the subarray is maximized.
# Return the maximum sum of such a subarray.
# -----------------------------
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100


def max_sum(nums: list[int]) -> int:
    # working_sol (100.00%, 17.65%) -> (0ms, 17.94mb)  time: O(n) | space: O(n)
    # We don't have any deletion limits.
    # We can just remove everything and take the highest sum without duplicates.
    out: set[int] = {
        val for val in nums if val > 0
    }
    if 0 == len(out):
        return max(nums)
    return sum(out)


# Time complexity: O(n) <- n - length of the input array `nums`.
# In the worst case, if there's only negative values.
# We're going to traverse the input array `nums`, twice => O(2 * n).
# -----------------------------
# Auxiliary space: O(n)
# In the worst case every value in `nums` is unique and positive.
# `out` <- allocates space for each of this value => O(n).


test: list[int] = [1, 2, 3, 4, 5]
test_out: int = 15
assert test_out == max_sum(test)

test = [1, 1, 0, 1, 1]
test_out = 1
assert test_out == max_sum(test)

test = [1, 2, -1, -2, 1, 0, -1]
test_out = 3
assert test_out == max_sum(test)
