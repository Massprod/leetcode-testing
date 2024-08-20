# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
# Given an integer array nums and an integer k, return the kth smallest distance
#  among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
# -----------------------
# n == nums.length
# 2 <= n <= 10 ** 4
# 0 <= nums[i] <= 10 ** 6
# 1 <= k <= n * (n - 1) / 2
from random import randint


def smallest_distance_pair(nums: list[int], k: int) -> int:
    min_val: int = 0
    max_pair: int = max(nums)  # max_val - min_val
    all_distances: list[int] = [0 for val in range(min_val, max_pair + 1)]
    for y in range(len(nums)):
        for x in range(y + 1, len(nums)):
            cur_pair: int = abs(nums[y] - nums[x])
            all_distances[cur_pair] += 1
    for index, distance in enumerate(all_distances):
        k -= distance
        if 0 >= k:
            return index
    return -1


test: list[int] = [1, 3, 1]
test_k: int = 1
test_out: int = 0
assert test_out == smallest_distance_pair(test, test_k)

test = [1, 1, 1]
test_k = 2
test_out = 0
assert test_out == smallest_distance_pair(test, test_k)

test = [1, 6, 1]
test_k = 3
test_out = 5
assert test_out == smallest_distance_pair(test, test_k)

test = [randint(0, 10 ** 6) for _ in range(10 ** 4)]
print(test)
