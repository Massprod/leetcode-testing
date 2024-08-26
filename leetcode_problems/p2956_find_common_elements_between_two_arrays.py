# You are given two integer arrays nums1 and nums2 of sizes n and m, respectively.
# Calculate the following values:
#  - answer1 : the number of indices i such that nums1[i] exists in nums2.
#  - answer2 : the number of indices i such that nums2[i] exists in nums1.
# Return [answer1,answer2].
# ----------------------
# n == nums1.length
# m == nums2.length
# 1 <= n, m <= 100
# 1 <= nums1[i], nums2[i] <= 100


def find_intersection_values(nums1: list[int], nums2: list[int]) -> list[int]:
    # working_sol (90.92%, 81.08%) -> (121ms, 16.44mb)  time: O(n + m) | space: O(n + m)
    fast_1: set[int] = set(nums1)
    fast_2: set[int] = set(nums2)
    out_1: int = 0
    for num in nums1:
        if num in fast_2:
            out_1 += 1
    out_2: int = 0
    for num in nums2:
        if num in fast_1:
            out_2 += 1
    return [out_1, out_2]


# Time complexity: O(n + m) <- n - length of the input array `nums1`, m - length of the input array `nums2`.
# Always traversing `nums1` and `nums2`, twice => O((n + m) * 2).
# ----------------------
# Auxiliary space: O(n + m).
# In the worst case, every value is unique.
# `fast_1` <- allocates space for each value from `nums1` => O(n).
# `fast_2` <- allocates space for each value from `nums2` => O(m).


test_1: list[int] = [2, 3, 2]
test_2: list[int] = [1, 2]
test_out: list[int] = [2, 1]
assert test_out == find_intersection_values(test_1, test_2)

test_1 = [4, 3, 2, 3, 1]
test_2 = [2, 2, 5, 2, 3, 6]
test_out = [3, 4]
assert test_out == find_intersection_values(test_1, test_2)

test_1 = [3, 4, 2, 3]
test_2 = [1, 5]
test_out = [0, 0]
assert test_out == find_intersection_values(test_1, test_2)
