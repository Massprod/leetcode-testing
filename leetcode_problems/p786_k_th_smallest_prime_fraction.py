# You are given a sorted integer array arr containing 1 and prime numbers,
#  where all the integers of arr are unique. You are also given an integer k.
# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2,
#  where answer[0] == arr[i] and answer[1] == arr[j].
# ---------------------------
# 2 <= arr.length <= 1000
# 1 <= arr[i] <= 3 * 10 ** 4
# arr[0] == 1
# arr[i] is a prime number for i > 0.
# All the numbers of arr are unique and sorted in strictly increasing order.
# 1 <= k <= arr.length * (arr.length - 1) / 2
import heapq


def kth_smallest_prime_fraction(arr: list[int], k: int) -> list[int]:
    # working_sol (72.20%, 91.19%) -> (568ms, 16.8mb)  time: O(n + (n + k) * log n) | space: O(n)
    kek: int
    numer_index: int
    denominator_index: int
    if 1 == k:
        return [arr[0], arr[-1]]
    heap: list[tuple[float, int, int]] = []
    heapq.heapify(heap)
    out: list[int] = [0, 0]
    denominator_index = len(arr) - 1
    for index in range(len(arr) - 1):
        heapq.heappush(heap, (
            arr[index] / arr[-1],
            index,
            denominator_index,
        ))
    while 1 != k:
        kek, numer_index, denominator_index = heapq.heappop(heap)
        denominator_index -= 1
        if numer_index < denominator_index:
            heapq.heappush(heap, (
                (arr[numer_index] / arr[denominator_index]),
                numer_index,
                denominator_index
            ))
        k -= 1
    kek, out[0], out[1] = heapq.heappop(heap)
    out[0], out[1] = arr[out[0]], arr[out[1]]
    return out


# Time complexity: O(((k + n) * log n) + n) <- length of the input array `arr`.
# Always traversing whole input array `arr` once => O(n).
# Extra using `heapq.heappop()` and `heapq.heappush()`, `k` times on a `heap` with `n` elements in it.
# Every push(), pop() operations is O(log n) => O(((k + n) * log n) + n)
# ---------------------------
# Auxiliary space: O(n)
# `heap` will always store only `n` elements.
# We're always taking one and pushing one back => O(n).
# ---------------------------
# Best tactic, is to use SMALLEST / HIGHEST combs.
# So, we calculate all SMALLEST one by one with current HIGHEST.
# And everything else which can be lower, is in logic like.
# We're taking currentyl SMALLEST fraction we got, and change our DENOMINATOR to the next possible to use.
# And it's always previous (DENOMINATOR - 1).
# So, we store everything in a `heap` and take the SMALLEST fractions one by one, until we reach our k value.
# That's why we're always taking only (k - 1) values from `heap`, last `k` value is what we need.


test: list[int] = [1, 2, 3, 5]
test_k: int = 3
test_out: list[int] = [2, 5]
assert test_out == kth_smallest_prime_fraction(test, test_k)

test = [1, 7]
test_k = 1
test_out = [1, 7]
assert test_out == kth_smallest_prime_fraction(test, test_k)

test = [1, 7, 23, 29, 47]
test_k = 8
test_out = [23, 47]
assert test_out == kth_smallest_prime_fraction(test, test_k)
