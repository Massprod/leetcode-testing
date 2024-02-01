# You are given an integer array nums and a positive integer k.
# You can choose any subsequence of the array and sum all of its elements together.
# We define the K-Sum of the array as the kth largest subsequence sum that can be obtained
#  (not necessarily distinct).
# Return the K-Sum of the array.
# A subsequence is an array that can be derived from another array
#  by deleting some or no elements without changing the order of the remaining elements.
# Note that the empty subsequence is considered to have a sum of 0.
# ---------------------
# n == nums.length
# 1 <= n <= 10 ** 5
# -10 ** 9 <= nums[i] <= 10 ** 9
# 1 <= k <= min(2000, 2 ** n)
import heapq
from random import randint


def k_sum(nums: list[int], k: int) -> int:
    # working_sol (98.11%, 52.83%) -> (551ms, 31.76mb)  time: O(n * log n + k * log k)  space: O(n + k)
    cur_sum: int
    index: int
    max_sum: int = 0
    for num in nums:
        if 0 < num:
            max_sum += num
    nums[:] = sorted([abs(num) for num in nums])
    # [(sum, index of used value)], max-heap.
    sums: list[tuple[int, int]] = []
    heapq.heapify(sums)
    heapq.heappush(sums, (max_sum * -1 + nums[0], 0))
    out: int = max_sum * -1
    k -= 1
    limit: int = len(nums) - 1
    while k:
        cur_max, index = heapq.heappop(sums)
        out = cur_max
        # DP like approach with using index and not using this index, but with Heapq.
        # We either delete nums[index] from SUM, and never restore it.
        # Or we restore this value and delete next.
        # Allows us to cover all subsequences without recursion, and maintain maximum current sum.
        # Works, because next lower sum we can have is either:
        #  - sum we have and minus something higher
        #  - sum we have and minus something higher with leaving previously deleted.
        # Like: [1, 2, 3, 4] -> [1 + 2 + 3 + 4] lower: [2 + 3 + 4] next lower: [1 + 3 + 4]
        # [2 + 3 + 4] lower: [3, 4] next lower: [2, 4] etc.
        if index < limit:
            # Restore value of used_value(deleted) from sum, and delete first Higher element.
            heapq.heappush(sums, (cur_max - nums[index] + nums[index + 1], index + 1))
            # Don't restore used_value, and just delete next first Higher element.
            heapq.heappush(sums, (cur_max + nums[index + 1], index + 1))
        k -= 1
    return out * -1


# Time complexity: O(n * log n + k * log k) <- n - length of input array `nums`.
# First we're sorting input array `nums` with builtin sorted() => O(n * log n).
# Worst case: k >= len(nums), len == 2, k = 2 ** 2 = 4
# So, we will use every value from `nums` to get deleted|restored sum options.
# And heap will be at max size of (k * 2), but we only use heap operations for k times => O(k * log k).
# ---------------------
# Auxiliary space: O(n + k).
# We're repopulating `nums` with abs() values and it's same size and INTs inside => O(1).
# But sorted() will still take space => O(n).
# And max-heap `sums` with all sums we build at max of size (k * 2) => O(2k).
# ---------------------
# Hints:
# ! Start from the largest sum possible,
#   and keep finding the next largest sum until you reach the kth sum. !
# ! Starting from a sum, what are the two next largest sums that you can obtain from it? !


test: list[int] = [2, 4, -2]
test_k: int = 5
test_out: int = 2
assert test_out == k_sum(test, test_k)

test = [1, -2, 3, 4, -10, 12]
test_k = 16
test_out = 10
assert test_out == k_sum(test, test_k)

test = [-1, 1]
test_k = 1
test_out = 1
assert test_out == k_sum(test, test_k)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 4)]
print(test)
