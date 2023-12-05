# Given two sorted arrays nums1 and nums2 of size m and n respectively,
#  return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# -----------------
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10 ** 6 <= nums1[i], nums2[i] <= 10 ** 6


def find_median_arrays(nums1: list[int], nums2: list[int]) -> float:
    # working_sol (69.58%, 54.26%) -> (88ms, 16.59mb)  time: O(m + n)) | space: O(1)
    # Essentially without BinarySearch.
    # We need to merge them and find (len(sorted(nums1 + nums2)) // 2) elements.
    # But they're already sorted in ascending order.
    # So, we can just take minimum value from both of them, until we hit correct index.
    point1: int = 0
    point2: int = 0
    taken: int = -1
    previous: int = 0
    middle_val: int = 0
    middle_ind: int = (len(nums1) + len(nums2)) // 2
    while taken != middle_ind:
        previous = middle_val
        if point1 < len(nums1) and point2 < len(nums2):
            if nums1[point1] < nums2[point2]:
                middle_val = nums1[point1]
                point1 += 1
            else:
                middle_val = nums2[point2]
                point2 += 1
        elif point1 < len(nums1):
            middle_val = nums1[point1]
            point1 += 1
        elif point2 < len(nums2):
            middle_val = nums2[point2]
            point2 += 1
        taken += 1
    if (len(nums1) + len(nums2)) % 2:
        return middle_val
    return (previous + middle_val) / 2


# Time complexity: O(m + n) <- m - length of input array 'nums1',
#                              n - length of input array 'nums2'.
# We're only traversing half of the merged array indexes, on Median.
# But worst case == [1] [2] => we're using every index => O(m + n).
# -----------------
# Auxiliary space: O(1).
# Only 6 constant INTs used, none of them depends on input.
# -----------------
# !
# The overall run time complexity should be O(log (m+n))
# !
# To do this, I need to google or steal from editorial. Which can be done anytime.
# So, leaving it for daily maybe learn BS solution later.


test_nums1: list[int] = [1, 3]
test_nums2: list[int] = [2]
test_out: float = 2.0
assert test_out == find_median_arrays(test_nums1, test_nums2)

test_nums1 = [1, 2]
test_nums2 = [3, 4]
test_out = 2.5
assert test_out == find_median_arrays(test_nums1, test_nums2)
