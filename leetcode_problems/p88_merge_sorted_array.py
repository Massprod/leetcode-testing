# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# ---------------------------------
# nums1.length == m + n  ,  nums2.length == n
# 0 <= m, n <= 200  ,  1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    pass


test1_nums1 = [1, 2, 3, 0, 0, 0]
test1_m = 3
test1_nums2 = [2, 5, 6]
test1_n = 3

test2_nums1 = [1]
test2_m = 1
test2_nums2 = []
test2_n = 0

test3_nums1 = [0]
test3_m = 0
test3_nums2 = [1]
test3_n = 1
