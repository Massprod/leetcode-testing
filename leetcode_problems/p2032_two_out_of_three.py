# Given three integer arrays nums1, nums2, and nums3,
#  return a distinct array containing all the values that are present in at least two out of the three arrays.
# You may return the values in any order.
# ------------------------
# 1 <= nums1.length, nums2.length, nums3.length <= 100
# 1 <= nums1[i], nums2[j], nums3[k] <= 100


def two_out_of_three(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    # working_sol (90.37%, 12.07%) -> (58ms, 16.62mb)  time: O(n + k + m) | space: O(n + k + m + max(n, k, m))
    occurs: dict[int, int] = {}
    for num in set(nums1):
        if num in occurs:
            continue
        occurs[num] = 1
    for num in set(nums2):
        if num in occurs:
            occurs[num] = 2
            continue
        occurs[num] = 1
    for num in set(nums3):
        if num in occurs:
            occurs[num] = 2
    out: list[int] = []
    for value, occur in occurs.items():
        if occur == 2:
            out.append(value)
    return out


# Time complexity: O(n + k + m) <- n, k, m - length of the input arrays.
# Always traversing all 3 input arrays to get all unique values => O(n + k + m).
# In the worst case, there's only unique values in all of them.
# Traverse all these values again => O(2 * (n + k + m)).
# Extra traversing all the unique values from all three => O(3 * (n + k + m)).
# ------------------------
# Auxiliary space: O(n + k + m + max(n, k, m)).
# `occurs` <- allocates space for each unique value from all the input arrays => O(n + k + m).
# In the worst case, there's one array that holds all the unique from 2 others.
# `out` <- allocates space for this array => O(n + k + m + max(n, k, m)).


test_1: list[int] = [1, 1, 3, 2]
test_2: list[int] = [2, 3]
test_3: list[int] = [3]
test_out: list[int] = [2, 3]
assert test_out == two_out_of_three(test_1, test_2, test_3)

test_1 = [3, 1]
test_2 = [2, 3]
test_3 = [1, 2]
test_out = [1, 3, 2]
assert test_out == two_out_of_three(test_1, test_2, test_3)

test_1 = [1, 2, 2]
test_2 = [4, 3, 3]
test_3 = [5]
test_out = []
assert test_out == two_out_of_three(test_1, test_2, test_3)
