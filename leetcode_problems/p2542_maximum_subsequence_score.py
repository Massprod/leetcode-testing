# You are given two 0-indexed integer arrays nums1 and nums2
#   of equal length n and a positive integer k.
# You must choose a subsequence of indices from nums1 of length k.
# For chosen indices i0, i1, ..., ik - 1, your score is defined as:
#   - The sum of the selected elements from nums1 multiplied
#     with the minimum of the selected elements from nums2.
#   - It can defined simply as:
#     (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.
# A subsequence of indices of an array is a set that can be derived
#   from the set {0, 1, ..., n-1} by deleting some or no elements.
# --------------------
# n == nums1.length == nums2.length
# 1 <= n <= 10 ** 5
# 0 <= nums1[i], nums2[j] <= 10 ** 5
# 1 <= k <= n
import heapq
from random import randint


def max_score(nums1: list[int], nums2: list[int], k: int) -> int:
    # working_sol (93.47%, 48.99%) -> (827ms, 38.3mb)  time: O(n * log n) | space: O(n + k)
    # ! n == nums1.length == nums2.length !
    # We can use indexes from nums1 only corresponding with nums2.
    # Combine them to use correctly.
    combined: list[tuple[int, int]] = [(nums1[_], nums2[_]) for _ in range(len(nums1))]
    # Sort by values in nums2, cuz we need to maintain Maximized sequence
    #  from nums1 and take every possible option from nums2.
    # But we need to take this options in descending order.
    # Otherwise, we can't maintain Maximized sequence correctly.
    # So it's either Sort in descending or just Reverse traversing.
    combined.sort(key=lambda x: x[1])
    # Take first Maximized sequence as a Heap.
    # Heap -> to maintain (k - 1)/k elements of the sequence Maximized.
    max_indexes: heapq = [_[0] for _ in combined[-1:(-k - 1):-1]]
    heapq.heapify(max_indexes)
    current_sum: int = sum(max_indexes)
    # Take Minimum from corresponding sequence of nums2.
    current_min: int = min([_[1] for _ in combined[-1:(-k - 1):-1]])
    max_score_: int = current_sum * current_min
    for y in range(len(nums2) - k - 1, -1, -1):
        # Delete smallest and append new index value.
        current_sum -= heapq.heappop(max_indexes)
        # ^^This step is why we need Descending order for
        #  values in nums2.
        # Cuz we can delete Minimum value from a Heap,
        #  and still leave Value which corresponds with previous
        #  Minimum from nums2.
        # And if we take Values from nums2 in descending order,
        #  we can delete w.e we want from Heap and still have correct new
        #  Value|Index from nums1 added which corresponds with current Minimum in nums2.
        current_sum += combined[y][0]
        current_min = combined[y][1]
        # Saving 2/3 Maximized Values|Indexes from nums1,
        #  and adding a new one.
        heapq.heappush(max_indexes, combined[y][0])
        # So we always maintain (k - 1)/k Maximized from nums1,
        #  and check every other Value from nums1 with correct indexing for num2.
        max_score_ = max(max_score_, current_sum * current_min)
    return max_score_


# Time complexity: O(n * log n) -> combine both arrays to one => O(n) -> sort combined array => O(n * log n) ->
# n - len of input_arrays^^| -> traverse every index of combined array once, to calc everything ->
#                            -> heap operations are constant, change of sum and current_min also constant =>
#                            => O(n).
# Auxiliary space: O(n + k) -> combined array with size of n but storing tuple[int, int] not int => O(2n) ->
# k - input limit^^|           -> heap with a size of k at all time => O(k).
# --------------------
# Ok. Subsequence is any sequence of Indexes, but we're restricted with taking the same indexes from nums2.
# ! (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]) !
# Anything we take from nums1 is mirrored by indexes in nums2.
# How we can combine them?
# Create array with [(nums1[0],nums2[0]) etc] and? Taking a Hint ->
# -> ! Try sorting the two arrays based on second array. ! and?
# Sort by nums2 and take sequence of length == K.
# Then we will have standard Sequence with some elements in it, we can save?
# What we essentially want? Save Maximum possible values from nums1 and use Minimum possible in nums2?
# Like we can't do this cuz indexes can differ, but we can at least save some of the maximum values from nums1.
# After taking this sequence of K we can leave indexes with maximum values
#  and replace minimum one of them with a new index?
# Then we will maintain somewhat Maximized sequence and use every possible new index from nums2 to multiply with.
# Let's try.
# Failed, we can't use num2 in ascending order, cuz we're removing Minimum option which can correspond
#  with not Minimum option from num1. And we're deleting Minimum from nums1 sequence, to leave it Maximized.
# In other words, we always maintain 2 indexes Maximized and when we delete Lowest, we can leave Index which is
#  not lowest and in pair with previous Minimum from nums2.
# So it's either sort in descending or reverse traverse to maintain them correctly.
# Then we can delete any stored|Maximized Index from nums1, cuz it will never be paired with current Minimum from nums2.


test_1: list[int] = [1, 3, 3, 2]
test_2: list[int] = [2, 1, 3, 4]
test_k: int = 3
test_out: int = 12
assert test_out == max_score(test_1, test_2, test_k)

test_1 = [4, 2, 3, 1, 1]
test_2 = [7, 5, 10, 9, 6]
test_k = 1
test_out = 30
assert test_out == max_score(test_1, test_2, test_k)

test_1 = []
test_2 = []
for _ in range(10 ** 3):
    test_1.append(randint(0, 10 ** 5))
    test_2.append(randint(0, 10 ** 5))
test_k = randint(1, len(test_1))
print(test_1)
print('---------')
print(test_2)
print('---------!')
print(test_k)
