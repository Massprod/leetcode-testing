# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique, and you may return the result in any order.
# ----------------
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


def intersection(nums1: list[int], nums2: list[int]) -> set[int]:
    # working_sol (90.29%, 91.23%) -> (47ms, 16.37mb)  time: O(n + m) | space: O(n + m)
    # ! The intersection of two arrays is a list of distinct
    #   numbers which are present in both the arrays. !
    fast_nums2: set[int] = set(nums2)
    intersect: set[int] = set()
    for num in nums1:
        if num in fast_nums2:
            intersect.add(num)
    return intersect


# Time complexity: O(n + m) -> traversing nums2 once to recreate as set => O(n) -> check every num in nums1 => O(m).
# m - len of input_nums1^^|
# n - len of input_nums2^^|
# Auxiliary space: O(n + m) -> always recreating set(nums2) => O(n) -> worst case, every number from nums1 is
#                              intersecting with nums2 == extra set of m size => O(m).


test_1: list[int] = [1, 2, 2, 1]
test_2: list[int] = [2, 2]
test_out: set[int] = {2}
assert test_out == intersection(test_1, test_2)

test_1 = [4, 9, 5]
test_2 = [9, 4, 9, 8, 4]
test_out = {4, 9}
assert test_out == intersection(test_1, test_2)
