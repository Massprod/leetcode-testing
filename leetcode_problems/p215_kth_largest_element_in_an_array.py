# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
# -------------
# 1 <= k <= nums.length <= 10 ** 5
# -10 ** 4 <= nums[i] <= 10 ** 4
import heapq
from random import randint


def find_kth_largest(nums: list[int], k: int) -> int:
    # working_sol (98.25%, 75.29%) -> (438ms, 29.48mb)  time: O(n * log k) | space: O(k)
    largest: heapq = []
    heapq.heapify(largest)
    for num in nums:
        # Populating until limit, no matter the values.
        if len(largest) != k:
            heapq.heappush(largest, num)
        # Delete smallest, and add anything higher.
        # We're always deleting smallest and adding something higher,
        # there's going to be only HIGHEST values, and smallest of them is Kth.
        # Only K highest elements is stored.
        elif largest[0] < num:
            heapq.heappop(largest)
            heapq.heappush(largest, num)
    return largest[0]


# Time complexity: O(n * log k) -> traversing whole input_array, once => O(n) ->
# k - num of largest to find^^|-> in the worst case like n == 10 ** 5, and k = 10 ->
# n - len of input_array^^|    -> we will add 10 elements in heap, and it's small number comparing to whole array,
#                              so we still can count array as n, but every value after this 10 is going to be bigger ->
#                              -> cuz of that we need to pop() and push() for (n - 10) indexes and every push(),pop()
#                              operation is O(log k) => O(n * log k).
# Auxiliary space: O(k) -> using heap to store some number K of largest elements from input_array => O(k).
# -------------
# What's a trick? On first sight it's just heapq, with deleting smallest when we encounter something bigger.
# Don't see how it's incorrect, let's try.
# Bruh, how is that Medium? When literally all Easy today is harder.


test: list[int] = [3, 2, 1, 5, 6, 4]
test_k: int = 2
test_out: int = 5
assert test_out == find_kth_largest(test, test_k)

test = [3, 2, 3, 1, 2, 4, 5, 5, 6]
test_k = 4
test_out = 4
assert test_out == find_kth_largest(test, test_k)

test = []
for _ in range(10 ** 5):
    test.append(randint(-10 ** 4, 10 ** 4))
test_k = randint(1, len(test))
print(test)
print(test_k)
