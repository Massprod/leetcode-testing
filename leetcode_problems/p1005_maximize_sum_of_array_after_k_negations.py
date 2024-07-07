# Given an integer array nums and an integer k, modify the array in the following way:
#   choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times.
# You may choose the same index i multiple times.
# Return the largest possible sum of the array after modifying it in this way.
# --------------------------
# 1 <= nums.length <= 10 ** 4
# -100 <= nums[i] <= 100
# 1 <= k <= 10 ** 4
import heapq
from random import randint


def largest_sum_after_k_negations(nums: list[int], k: int) -> int:
    # working_sol (87.57%, 14.03%) -> (43ms, 16.75mb)  time: O(n * log n) | space: O(n)
    out = 0
    min_abs: int = 101
    heap: list[int] = []
    heapq.heapify(heap)
    for num in nums:
        if 0 > num:
            heapq.heappush(heap, num)
        # We can have the smallest positive or the highest negative we can switch after.
        # So, we need to get the smallest of them after switching.
        min_abs = min(min_abs, abs(num))
        out += num
    while heap and k:
        out += (heapq.heappop(heap) * -1) * 2
        k -= 1
    # Switched all negative, and still have moves.
    if k:
        # So, we're either switching the smallest positive and leaving it as negative.
        # Or we're switching the highest negative again, to use it instead.
        # Because positive 3 => -3 > negative -2 => 2.
        if k % 2:
            out -= min_abs * 2
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# In the worst case, every value is negative.
# So, `heap` is going to be a size of `n` and pushing to it is `log(size)` => O(n * log n).
# Extra traversing whole `heap` to deplete `k` => O(k).
# --------------------------
# Auxiliary space: O(n)
# `heap` with size of `n` => O(n).


test: list[int] = [4, 2, 3]
test_k: int = 1
test_out: int = 5
assert test_out == largest_sum_after_k_negations(test, test_k)

test = [3, -1, 0, 2]
test_k = 3
test_out = 6
assert test_out == largest_sum_after_k_negations(test, test_k)

test = [2, -3, -1, 5, -4]
test_k = 2
test_out = 13
assert test_out == largest_sum_after_k_negations(test, test_k)

test = [-8, 3, -5, -3, -5, -2]
test_k = 6
test_out = 22
assert test_out == largest_sum_after_k_negations(test, test_k)

test = [randint(-100, 100) for _ in range(10 ** 4)]
print(test)
