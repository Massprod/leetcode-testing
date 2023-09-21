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
    # working_sol (86.87%, 99.3%) -> (84ms, 16.4mb)  time: O((m + n) * log(m + n))
    # Not correct solution O((m + n) * log(m + n))
    merge: list[int] = sorted(nums1 + nums2)
    median: float = 0
    if not merge:
        return median
    middle: int = len(merge) // 2
    if len(merge) % 2 == 0:
        median = (merge[middle] + merge[middle - 1]) / 2
    elif len(merge) % 2 != 0:
        median = merge[middle]
    return median


# Time complexity: O((m + n) * log(m + n) -> merging and sorting combined arrays.
# Auxiliary space: O(m + n) -> extra merged array.
# -----------------
# !
# The overall run time complexity should be O(log (m+n))
# !
# To do this, I need to google or steal from editorial. Which can be done anytime.
# So, leaving it for daily maybe learn BS solution later.


test1: list[int] = [1, 3]
test2: list[int] = [2]
test_out: float = 2.0
assert test_out == find_median_arrays(test1, test2)

test1 = [1, 2]
test2 = [3, 4]
test_out = 2.5
assert test_out == find_median_arrays(test1, test2)
