# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
#  and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
#  where the first m elements denote the elements that should be merged,
#  and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# ---------------------------------
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10 ** 9 <= nums1[i], nums2[j] <= 10 ** 9
# ---------------------------------
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # working_sol (97.60%, 96.58%) -> (34ms, 16.2mb)  time: O(m + n) | space: O(1)
    # Last index with '0' placed.
    nums1_index: int = m + n - 1
    # Last index with normal value placed == highest value in nums1.
    nums1_pointer: int = m - 1
    for x in range(n - 1, -1, -1):
        # Lower than our highest in original nums1.
        if nums2[x] < nums1[nums1_pointer]:
            # Shift higher value to the right_side.
            while nums1[nums1_pointer] > nums2[x] and nums1_pointer >= 0:
                nums1[nums1_pointer], nums1[nums1_index] = nums1[nums1_index], nums1[nums1_pointer]
                nums1_pointer -= 1
                nums1_index -= 1
            # Replace shifted from right_side '0' with nums2 value.
            nums1[nums1_index] = nums2[x]
            nums1_index -= 1
        # Higher than our highest in original nums1.
        elif nums2[x] >= nums1[nums1_pointer]:
            nums1[nums1_index] = nums2[x]
            nums1_index -= 1


# Time complexity: O(m + n) -> worst case == every value in nums2 is lower than everything in nums1 ->
# m - number of correct values in nums1 ^^| -> then we will shift every zero on left side first, m indexes used => O(m)
# n - len of input array nums2 ^^| -> and replace shifted '0' with nums2 values => O(n) => O(m + n).
# Space complexity: O(1) -> only 2 extra constant INTs: nums1_index, nums1_pointer => O(1)
# -----------------------
# In every nums1 - (m) == first index where's 0 placed (free point).
# In every nums2 - (n - 1) == last index of the array.


test_nums1: list[int] = [1, 2, 3, 0, 0, 0]
test_m: int = 3
test_nums2: list[int] = [2, 5, 6]
test_n: int = 3
to_assert: list[int] = sorted(test_nums1[:test_m] + test_nums2)
merge(test_nums1, test_m, test_nums2, test_n)
assert test_nums1 == to_assert

test_nums1 = [1]
test_m = 1
test_nums2 = []
test_n = 0
to_assert: list[int] = sorted(test_nums1[:test_m] + test_nums2)
merge(test_nums1, test_m, test_nums2, test_n)
assert test_nums1 == to_assert

test_nums1 = [0]
test_m = 0
test_nums2 = [1]
test_n = 1
to_assert: list[int] = sorted(test_nums1[:test_m] + test_nums2)
merge(test_nums1, test_m, test_nums2, test_n)
assert test_nums1 == to_assert

test_nums1 = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
test_m = 5
test_nums2 = [1, 2, 3, 4, 5]
test_n = 5
to_assert: list[int] = sorted(test_nums1[:test_m] + test_nums2)
merge(test_nums1, test_m, test_nums2, test_n)
assert test_nums1 == to_assert

test_nums1 = [-100, -32, -30, -15, -8, 0, 10, 15, 18, 0, 0, 0, 0, 0]
test_m = 9
test_nums2 = [-80, -32, 1, 2, 3]
test_n = 5
to_assert: list[int] = sorted(test_nums1[:test_m] + test_nums2)
merge(test_nums1, test_m, test_nums2, test_n)
assert test_nums1 == to_assert

# test -> Failed -> we're holding max_value index in nums1 as nums1_pointer, and it shouldn't be less than 0 ->
#                  -> in this case it overlapped and made it -1.
test_nums1 = [2, 0]
test_m = 1
test_nums2 = [1]
test_n = 1
to_assert: list[int] = sorted(test_nums1[:test_m] + test_nums2)
merge(test_nums1, test_m, test_nums2, test_n)
assert test_nums1 == to_assert

test_nums1 = [2, 0, 0, 0, 0, 0, 0, 0, 0]
test_m = 1
test_nums2 = [-1, 0, 1, 1, 1, 2, 2, 3]
test_n = 8
to_assert: list[int] = sorted(test_nums1[:test_m] + test_nums2)
merge(test_nums1, test_m, test_nums2, test_n)
assert test_nums1 == to_assert
