# Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
#  return the minimum integer common to both arrays.
# If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least
#  one occurrence of that integer.
# ---------------------------
# 1 <= nums1.length, nums2.length <= 10 ** 5
# 1 <= nums1[i], nums2[j] <= 10 ** 9
# Both nums1 and nums2 are sorted in non-decreasing order.
from random import randint


def get_common(nums1: list[int], nums2: list[int]) -> int:
    # working_sol (91.71%, 37.44%) -> (380ms, 36.7mb)  time: O(n + m) | space: O(n)
    # !  if both arrays have at least one occurrence of that integer. !
    # Assuming we can have more than 1 occurrence of any integer.
    # It's better to remove them, and extra O(1) checks for set.
    min_num: int | float = float('inf')
    fast_nums: set[int] = set(nums1)
    for num in nums2:
        if num in fast_nums:
            min_num = min(min_num, num)
    if type(min_num) == int:
        return min_num
    return -1


# Time complexity: O(n + m) -> traversing nums1 once to recreate as set => O(n) -> check every num in nums2 => O(m).
# n - len of input_nums1^^|
# m - len of input_nums2^^|
# Auxiliary space: O(n) -> always recreating set(nums1) => O(n).


test_1: list[int] = [1, 2, 3]
test_2: list[int] = [2, 4]
test_out: int = 2
assert test_out == get_common(test_1, test_2)

test_1 = [1, 2, 3, 6]
test_2 = [2, 3, 4, 5]
test_out = 2
assert test_out == get_common(test_1, test_2)

test_1 = [2, 4]
test_2 = [1, 2]
test_out = 2
assert test_out == get_common(test_1, test_2)

test_1 = sorted([randint(1, 10 ** 9) for _ in range(10 ** 3)])
test_2 = sorted([randint(1, 10 ** 9) for _ in range(10 ** 3)])
print(test_1)
print('---------')
print(test_2)
