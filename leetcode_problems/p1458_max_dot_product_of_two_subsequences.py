# Given two arrays nums1 and nums2.
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none)
#  of the characters without disturbing the relative positions of the remaining characters.
# (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
# -----------------------
# 1 <= nums1.length, nums2.length <= 500
# -1000 <= nums1[i], nums2[i] <= 1000
from random import randint


def max_dot_prod(nums1: list[int], nums2: list[int]) -> int:
    # working_sol (14.79%, 26.76%) -> (594ms, 97.5mb)  time: O(n * m) | space: O(n * m)
    recur_cache: dict[tuple[int, int], int] = {}

    def check(index1: int, index2: int) -> int | float:
        if (index1, index2) in recur_cache:
            return recur_cache[index1, index2]
        # Out of bounds.
        if index1 == len(nums1) or index2 == len(nums2):
            return 0
        maximum: int = max(
            nums1[index1] * nums2[index2] + check(index1 + 1, index2 + 1),  # use index values.
            check(index1 + 1, index2),  # skip index1 value.
            check(index1, index2 + 1),  # skip index2 value.
        )
        recur_cache[index1, index2] = maximum
        return maximum
    # If everything is negative in one of the input arrays.
    # We need to use at least 1 subsequence. So we need to use 1 index from both.
    # And because we need maximum it's always some max(negatives) * min(positives).
    if (neg := max(nums1)) < 0 and (pos := min(nums2)) > 0:
        return neg * pos
    elif (neg := max(nums2)) < 0 and (pos := min(nums1)) > 0:
        return neg * pos
    return check(0, 0)


# Time complexity: O(n * m) -> traversing of both array to check for all negatives and positives, twice => O(2*(n + m))
# n - len of input array 'nums1'^^| -> we will check every combination of indexes once => O(n * m).
# m - len of input array 'nums2'^^|
# Auxiliary space: O(n * m) -> store every combination of indexes into a dictionary => O(n * m).
# -----------------------
# Well find subsequence is easy with recursion and use, skip indexes.
# But we need two subsequences from both arrays and product of all index options.
# There's at least 2 options to build subs:
# (index1 + 1, index2) and (index1, index2 + 1) <- in case if we just skip them.
# (index1 + 1, index2 + 1) <- in case if we use them.
# And if we use them == we need to get product of them.
# Recursion with 3 options:
# nums1[index1] * nums2[index2] + check(index1 + 1, index2 + 2) <- using indexes.
# check(index1 + 1, index2)
# check(index1, index2 + 1) <- if we skip and use next.
# Because we need maximum product then it should be max(3options).
# Should be correct, but slow.


test_1: list[int] = [2, 1, -2, 5]
test_2: list[int] = [3, 0, -6]
test_out: int = 18
assert test_out == max_dot_prod(test_1, test_2)

test_1 = [3, -2]
test_2 = [2, -6, 7]
test_out = 21
assert test_out == max_dot_prod(test_1, test_2)

test_1 = [-1, -1]
test_2 = [1, 1]
test_out = -1
assert test_out == max_dot_prod(test_1, test_2)

test_1 = [randint(-1000, 1000) for _ in range(500)]
test_2 = [randint(-1000, 1000) for _ in range(500)]
print(test_1)
print('==========!')
print(test_2)
