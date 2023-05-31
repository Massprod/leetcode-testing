# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#   answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#   answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
# -----------------------
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000


def find_difference(nums: list[int], nums2: list[int]) -> list[list[int]]:
    pass


test1_nums1 = [1, 2, 3]
test1_nums2 = [2, 4, 6]
test1_out = [[1, 3], [4, 6]]

test2_nums1 = [1, 2, 3, 3]
test2_nums2 = [1, 1, 2, 2]
test2_out = [[3], []]
