# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# ---------------------------------
# nums1.length == m + n  ,  nums2.length == n
# 0 <= m, n <= 200  ,  1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
# ---------------------------------
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # working_sol (54.79%, 17.1%) -> (43ms, 16.4mb)  time: O(m + n) | space: O(1)
    nums1_index: int = m + n - 1
    nums1_pointer: int = m - 1
    for x in range(n - 1, -1, -1):
        if nums2[x] >= nums1[nums1_pointer]:
            nums1[nums1_index] = nums2[x]
            nums1_index -= 1
        if nums2[x] < nums1[nums1_pointer]:
            while nums1[nums1_pointer] >= nums2[x] and nums1_pointer >= 0:
                nums1[nums1_pointer], nums1[nums1_index] = nums1[nums1_index], nums1[nums1_pointer]
                nums1_pointer -= 1
                nums1_index -= 1
            nums1[nums1_index] = nums2[x]
            nums1_index -= 1


# Time complexity: O(m + n) -> looping once through every index in nums2 => O(n) ->
#                              -> looping once through indexes in range(m, -1, -1) in nums1 => O(m) -> O(m + n)
# m - number of correct values in nums1 ^^
# n - number of correct values in nums2 ^^
#     (extra 0 in nums1 incorrect, ignored)
#
# Space complexity: O(1) -> 2 extra constants: nums1_index, nums1_pointer => O(1)
# -----------------------
# Always fun to succeed in 10+ values test and fail with [2, 0] :)
# At least I made it working from the start, and only failed to consider going negative on index.
# -----------------------
# In every nums1 - m -> first index where's 0 placed (free point).
# In every nums2 - n -> last index of the array.


test1_nums1 = [1, 2, 3, 0, 0, 0]
test1_m = 3
test1_nums2 = [2, 5, 6]
test1_n = 3
to_assert = test1_nums1.copy() + test1_nums2.copy()
to_assert.sort()
for _ in range(test1_n):
    to_assert.remove(0)
merge(test1_nums1, test1_m, test1_nums2, test1_n)
print(test1_nums1)
assert test1_nums1 == to_assert

test2_nums1 = [1]
test2_m = 1
test2_nums2 = []
test2_n = 0
to_assert = test2_nums1.copy() + test2_nums2.copy()
to_assert.sort()
for _ in range(test2_n):
    to_assert.remove(0)
merge(test2_nums1, test2_m, test2_nums2, test2_n)
print(test2_nums1)
assert test2_nums1 == to_assert

test3_nums1 = [0]
test3_m = 0
test3_nums2 = [1]
test3_n = 1
to_assert = test3_nums1.copy() + test3_nums2.copy()
to_assert.sort()
for _ in range(test3_n):
    to_assert.remove(0)
merge(test3_nums1, test3_m, test3_nums2, test3_n)
print(test3_nums1)
assert test3_nums1 == to_assert

test4_nums1 = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
test4_m = 5
test4_nums2 = [1, 2, 3, 4, 5]
test4_n = 5
to_assert = test4_nums1.copy() + test4_nums2.copy()
to_assert.sort()
for _ in range(test4_n):
    to_assert.remove(0)
merge(test4_nums1, test4_m, test4_nums2, test4_n)
print(test4_nums1)
assert test4_nums1 == to_assert

test5_nums1 = [-100, -32, -30, -15, -8, 0, 10, 15, 18, 0, 0, 0, 0, 0]
test5_m = 9
test5_nums2 = [-80, -32, 1, 2, 3]
test5_n = 5
to_assert = test5_nums1.copy() + test5_nums2.copy()
to_assert.sort()
for _ in range(test5_n):
    to_assert.remove(0)
merge(test5_nums1, test5_m, test5_nums2, test5_n)
print(test5_nums1)
assert test5_nums1 == to_assert

# test6 - failed -> we're holding max_value index in nums1 as nums1_pointer, and it shouldn't be less than 0 ->
#                   -> in this case it overlapped and made it -1.
test6_nums1 = [2, 0]
test6_m = 1
test6_nums2 = [1]
test6_n = 1
to_assert = test6_nums1.copy() + test6_nums2.copy()
to_assert.sort()
for _ in range(test6_n):
    to_assert.remove(0)
merge(test6_nums1, test6_m, test6_nums2, test6_n)
print(test6_nums1)
assert test6_nums1 == to_assert

test7_nums1 = [2, 0, 0, 0, 0, 0, 0, 0, 0]
test7_m = 1
test7_nums2 = [-1, 0, 1, 1, 1, 2, 2, 3]
test7_n = 8
to_assert = test7_nums1.copy() + test7_nums2.copy()
to_assert.sort()
for _ in range(test7_n):
    to_assert.remove(0)
merge(test7_nums1, test7_m, test7_nums2, test7_n)
print(test7_nums1)
assert test7_nums1 == to_assert
