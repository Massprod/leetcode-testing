# You are given two integer arrays nums1 and nums2 both of the same length.
# The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].
# Return any permutation of nums1 that maximizes its advantage with respect to nums2.
# --------------------
# 1 <= nums1.length <= 10 ** 5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 10 ** 9
import heapq
from random import randint


def advantage_count(nums1: list[int], nums2: list[int]) -> list[int]:
    # working_sol (45.59%, 77.94%) -> (547ms, 37.46mb)  time: O(n * log n) | space: O(n)
    cur_val: int
    cur_ind: int
    nums1.sort(reverse=True)
    nums2[:] = [(value, index) for index, value in enumerate(nums2)]
    heapq.heapify(nums2)
    # ! 0 <= nums1[i], nums2[i] <= 10 ** 9 ! <- (-1) it's placeholder.
    out: list[int] = [-1 for _ in nums1]
    # Value which can't cover anything in `nums2`.
    not_covers: list[int] = []
    # All we care about is that we need to use the SMALLEST values from `nums1`
    #  to cover the SMALLEST values from `nums2`.
    while nums1:
        # Currently smallest in `nums2` and it's position.
        cur_val, cur_ind = nums2[0]
        cur_counter: int = nums1.pop()
        # If it's higher, then we can use it, and it's smallest so far.
        if cur_counter > cur_val:
            out[cur_ind] = cur_counter
            heapq.heappop(nums2)
        # Otherwise, we can place it on w.e place. Because it can't cover anything in `nums2`.
        else:
            not_covers.append(cur_counter)
    # Place all values which can't cover anything in `nums2` on empty spaces.
    for x in range(len(out)):
        if -1 == out[x]:
            out[x] = not_covers.pop()
    return out


# Time complexity: O(n * log n) <- n - length of input array `nums1` or `nums2`.
# Essentially we're sorting both arrays, one with standard sort() other with adding it into a heapq.
# And then we're just simply traversing whole `nums2`.
# Extra traverse of `out` to cover empty spots, and in the worst case we will have all spots empty.
# So it's O(n) for this traverse anyway.
# --------------------
# Auxiliary space: O(n)
# Standard sort() takes O(n) + heapq takes O(n) + `out` with the size of `n`.
# And `not_covers` can also be a size of `n` => O(4n).


test_1: list[int] = [2, 7, 11, 15]
test_2: list[int] = [1, 10, 4, 11]
test_out: list[int] = [2, 11, 7, 15]
assert test_out == advantage_count(test_1, test_2)

test_1 = [12, 24, 8, 32]
test_2 = [13, 25, 32, 11]
test_out = [24, 32, 8, 12]
assert test_out == advantage_count(test_1, test_2)

test_1 = [randint(0, 10 ** 9) for _ in range(10 ** 3)]
test_2 = [randint(0, 10 ** 9) for _ in range(10 ** 3)]
print(test_1)
print('\n\n!!!!!!!!!------\n\n')
print(test_2)
