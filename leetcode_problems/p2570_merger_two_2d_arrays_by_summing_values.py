# You are given two 2D integer arrays nums1 and nums2.
#  - nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
#  - nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# Each array contains unique ids and is sorted in ascending order by id.
# Merge the two arrays into one array that is sorted in ascending order by id,
#  respecting the following conditions:
#  - Only ids that appear in at least one of the two arrays should be included in the resulting array.
#  - Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
#    If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.
# ----------------------
# 1 <= nums1.length, nums2.length <= 200
# nums1[i].length == nums2[j].length == 2
# 1 <= idi, vali <= 1000
# Both arrays contain unique ids.
# Both arrays are in strictly ascending order by id.


def merge_arrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    # working_sol (87.38%, 76.05%) -> (54ms, 16.69mb)  time: O(n + m) | space: O(n + m)
    out: list[list[int]] = []
    point1: int = 0
    point2: int = 0
    # Everything already sorted, so we just need to take them in correct order.
    while point1 < len(nums1) and point2 < len(nums2):
        id_1: int = nums1[point1][0]
        id_2: int = nums2[point2][0]
        if id_1 == id_2:
            out.append(
                [id_1, nums1[point1][1] + nums2[point2][1]]
            )
            point1 += 1
            point2 += 1
        else:
            if nums1[point1][0] < nums2[point2][0]:
                out.append(nums1[point1])
                point1 += 1
            else:
                out.append(nums2[point2])
                point2 += 1
    # Everything else is irrelevant and can be placed after.
    out += nums1[point1:]
    out += nums2[point2:]
    return out


# Time complexity: O(n + m) <- n - length of the input array `nums1`, m - length of the input array `nums2`.
# Always traversing every index of both arrays, once => O(n + m).
# ----------------------
# Auxiliary space: O(n + m)
# In the worst case, every `id` in `nums1` and `nums2` unique == none equal.
# `out` <- allocates space for each pair from `nums1`, `nums2` => O(n + m).


test_1: list[list[int]] = [[1, 2], [2, 3], [4, 5]]
test_2: list[list[int]] = [[1, 4], [3, 2], [4, 1]]
test_out: list[list[int]] = [[1, 6], [2, 3], [3, 2], [4, 6]]
assert test_out == merge_arrays(test_1, test_2)

test_1 = [[2, 4], [3, 6], [5, 5]]
test_2 = [[1, 3], [4, 3]]
test_out = [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
assert test_out == merge_arrays(test_1, test_2)
