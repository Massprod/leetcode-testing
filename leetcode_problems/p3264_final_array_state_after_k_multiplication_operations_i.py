# You are given an integer array nums, an integer k, and an integer multiplier.
# You need to perform k operations on nums. In each operation:
# Find the minimum value x in nums. If there are multiple occurrences of the minimum value,
#  select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.
# ---------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 10
# 1 <= multiplier <= 5
import heapq
from random import randint


def get_final_state(nums: list[int], k: int, multiplier: int) -> list[int]:
    # working_sol (97.55%, 50.84%) -> (47ms, 16.58mb)  time: O(n + k * log n + n * log n) | space: O(n)
    cur_val: int
    cur_index: int
    heap: list[tuple[int, int]] = [
        (num, index) for index, num in enumerate(nums)
    ]
    heapq.heapify(heap)
    while k:
        cur_val, cur_index = heapq.heappop(heap)
        cur_val *= multiplier
        heapq.heappush(heap, (cur_val, cur_index))
        k -= 1
    out: list[int] = [0 for _ in range(len(nums))]
    while heap:
        cur_val, cur_index = heapq.heappop(heap)
        out[cur_index] = cur_val
    return out


# Time complexity: O(n + k * log n + n * log n) <- n - length of the input array `nums`.
# Creating `heap` of size `n` with `enumerate` => O(2 * n).
# We're always multiplying every value from `nums`, and our `heap` is at max of size `n`.
# Every operation we pop it and push which is `log n` and we repeat for `k` times => O(2 * n + k * log n).
# `pop` everything from `heap` to build `out` => O(2 * n + k * log n + n * log n) =>
# ---------------------------
# Auxiliary space: O(n)
# `heap` <- always of the same size as `nums` => O(n).
# `out` <- always of the same size as `nums` => O(2 * n).


test: list[int] = [2, 1, 3, 5, 6]
test_k: int = 5
test_multiplier: int = 2
test_out: list[int] = [8, 4, 6, 5, 6]
assert test_out == get_final_state(test, test_k, test_multiplier)

test = [1, 2]
test_k = 3
test_multiplier = 4
test_out = [16, 8]
assert test_out == get_final_state(test, test_k, test_multiplier)

test = [randint(1, 100) for _ in range(100)]
print(test)
