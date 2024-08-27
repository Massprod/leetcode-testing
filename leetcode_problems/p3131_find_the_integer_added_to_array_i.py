# You are given two arrays of equal length, nums1 and nums2.
# Each element in nums1 has been increased (or decreased in the case of negative) by an integer,
#  represented by the variable x.
# As a result, nums1 becomes equal to nums2.
# Two arrays are considered equal when they contain the same integers with the same frequencies.
# Return the integer x.
# -----------------------------
# 1 <= nums1.length == nums2.length <= 100
# 0 <= nums1[i], nums2[i] <= 1000
# The test cases are generated in a way that there is an integer x such that nums1
#  can become equal to nums2 by adding x to each element of nums1.


def added_integer(nums1: list[int], nums2: list[int]) -> int:
    # working_sol (94.38%, 81.53%) -> (42ms, 16.40mb)  time: O(n) | space: O(1)
    # equal == equal in sorted == we can take min|max diff
    # And we need to reverse value:
    #  nums1_max < nums2_max if `out` positive == we need to reverse diff.
    #  nums1_max > nums2_max if `out` negative == we need to reverse diff.
    return (max(nums1) - max(nums2)) * -1


# Time complexity: O(n) <- n - length of the input array `nums1` | `nums2`.
# We always traverse both input arrays to get `max()` => O(2 * n).
# -----------------------------
# Auxiliary space: O(1)


test_1: list[int] = [2, 6, 4]
test_2: list[int] = [9, 7, 5]
test_out: int = 3
assert test_out == added_integer(test_1, test_2)

test_1 = [10]
test_2 = [5]
test_out = -5
assert test_out == added_integer(test_1, test_2)

test_1 = [1, 1, 1, 1]
test_2 = [1, 1, 1, 1]
test_out = 0
assert test_out == added_integer(test_1, test_2)
