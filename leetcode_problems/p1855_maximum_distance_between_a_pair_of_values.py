# You are given two non-increasing 0-indexed integer arrays nums1 and nums2.
# A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length,
#  is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i.
# Return the maximum distance of any valid pair (i, j).
# If there are no valid pairs, return 0.
# An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.
# --------------
# 1 <= nums1.length, nums2.length <= 10 ** 5
# 1 <= nums1[i], nums2[j] <= 10 ** 5
# Both nums1 and nums2 are non-increasing.
from random import randint


def max_distance(nums1: list[int], nums2: list[int]) -> int:
    # working_sol (99.2%, 42.62%) -> (888ms, 35.3mb)  time: O(m + n) | space: O(1)
    # index of nums1
    index_1: int = 0
    # index of nums2
    index_2: int = 0
    # Is last value in nums2 checked.
    last_checked: bool = False
    max_dist: int = 0
    while index_1 != len(nums1):
        if last_checked:
            break
        # ! pair is valid if both i <= j and nums1[i] <= nums2[j] !
        # Starting from 0 in nums1, and adjust it to nums2 index.
        while nums1[index_1] <= nums2[index_2]:
            # ! The distance of the pair is j - i !
            max_dist = max(max_dist, index_2 - index_1)
            # We can use everything until num in nums2 is higher.
            index_2 += 1
            # And because we need Maximum distance we always maintain
            #  the lower index in nums1 and use everything we can in nums2.
            # So if we used last index of nums2, we can't get Higher distance,
            #  cuz nums1 index will only go Higher and will lower the distance.
            if index_2 == len(nums2):
                last_checked = True
                break
        # We can return it instantly.
        # Just breaking, cuz it's better looking than 4 returns.
        if last_checked:
            break
        # Find next correct pair:
        while nums1[index_1] > nums2[index_2]:
            # We always need ->
            # -> ! both i <= j and nums1[i] <= nums2[j] !
            # So index of nums2 is either higher or equal.
            # Arrays can be a different sizes, so we need to maintain
            #  nums we can use.
            if index_1 == index_2:
                index_2 += 1
                # If nums2 is exhausted and last value was incorrect,
                #  we can't use anything more.
                if index_2 == len(nums2):
                    last_checked = True
                    break
            index_1 += 1
            # Same goes for nums1, we can't use anything more.
            if index_1 == len(nums1):
                break

    return max_dist


# Time complexity: O(m + n) -> essentially we're just checking all indexes from nums1 and nums2 => O(m + n) ->
# m - len of input_nums1^^| -> not their pairs, but only indexes. So every index will be used once.
# n - len of input_nums2^^|
# Auxiliary space: O(1) -> 4 constants used: 3 INTs + 1 BOOL, none of them depends on input => O(1).
# --------------
# Failed first commit, didn't notice array can be different size.
# And my tests were equal size.


test_1: list[int] = [55, 30, 5, 4, 2]
test_2: list[int] = [100, 20, 10, 10, 5]
test_out: int = 2
assert test_out == max_distance(test_1, test_2)

test_1 = [2, 2, 2]
test_2 = [10, 10, 1]
test_out = 1
assert test_out == max_distance(test_1, test_2)

test_1 = [30, 29, 19, 5]
test_2 = [25, 25, 25, 25, 25]
test_out = 2
assert test_out == max_distance(test_1, test_2)

test_1 = sorted([randint(1, 10 ** 5) for _ in range(10 ** 3)], reverse=True)
test_2 = sorted([randint(1, 10 ** 5) for _ in range(10 ** 3)], reverse=True)
print(test_1)
print('-------------!')
print(test_2)
