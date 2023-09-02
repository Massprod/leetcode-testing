# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays,
#  and you may return the result in any order.
# ----------------
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    # working_sol (74.81%, 88.06%) -> (53ms, 16.39mb)  time: O(n + m) | space: O(m + n)
    # Count occurrences.
    fast_nums2: dict[int, int] = {}
    for num in nums2:
        if num not in fast_nums2:
            fast_nums2[num] = 1
            continue
        fast_nums2[num] += 1
    intersects: list[int] = []
    for num in nums1:
        if num in fast_nums2:
            # Exhaust every number we can take.
            if fast_nums2[num] > 0:
                intersects.append(num)
                fast_nums2[num] -= 1
    return intersects


# Time complexity: O(n + m) -> traverse and count every num occurrences in nums2 => O(m) ->
# n - len of input_nums1^^| -> traverse and check every num from nums1, to be presented in nums2 => O(n).
# m - len of input_nums2^^|
# Auxiliary space: O(m + n) -> creating dictionary with size of nums2 => O(m) -> worst case, equal lists
#                              intersects will be the same size as nums1 or nums2 => O(n) or O(m).


test_1: list[int] = [1, 2, 2, 1]
test_2: list[int] = [2, 2]
test_out: list[int] = [2, 2]
assert test_out == intersect(test_1, test_2)

test_1 = [4, 9, 5]
test_2 = [9, 4, 9, 8, 4]
test_out = [4, 9]
assert test_out == intersect(test_1, test_2)
