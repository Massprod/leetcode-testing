# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    merge = nums1 + nums2
    merge.sort()
    length = len(merge)
    median = 0
    if length == 0:
        return median
    if length % 2 == 0:
        median = (merge[int(length / 2)] + merge[int((length / 2) - 1)]) / 2
    elif length % 2 != 0:
        median = merge[int(length / 2)]
    return median



test1 = [1, 3]
test2 = [2]
test3 = [3, 4]
test4 = []
test5 = []
print(findMedianSortedArrays(test1, test2))
print(findMedianSortedArrays(test1, test3))
print(findMedianSortedArrays(test4, test5))