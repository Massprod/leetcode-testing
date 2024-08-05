# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.
# ------------------------------
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length
from random import randint


def find_kth_positive(arr: list[int], k: int) -> int:
    # working_sol (91.51%, 89.38%) -> (44ms, 16.58mb)  time: O(n + m + k) | space: O(m)
    max_val: int = arr[-1]
    # [array with all positive integers we can have]
    shame: list[int] = [val for val in range(1, max_val + 2)]
    cur_vals: int = len(shame)
    # Remove presented values.
    for val in arr:
        shame[val - 1] = 0
    cur_vals -= len(arr)
    # We need to expand our array, because these values are not enough.
    # And we can either expend it and check with `k`.
    # Or we already know, that there's not enough values => we can just add what we need and use it.
    # (always expand with +1 values, so it's the same as add `diff`)
    if cur_vals < k:
        diff: int = k - cur_vals
        return shame[-1] + diff
    cur_index: int = -1
    while k:
        cur_index += 1
        if 0 != shame[cur_index]:
            k -= 1
    return shame[cur_index]


# Time complexity: O(n + m + k) <- n - length of the input array `arr`, m - maximum value in `arr`.
# Always building `shame` of the size `m + 2` => O(m + 2).
# Extra traversing every in `arr` to remove already presented values from `shame` => O(n + m).
# Extra depleting `k` to find the k-th element and return it => O(n + m + k).
# ------------------------------
# Auxiliary space: O(m)
# `shame` <- is always of the same size `m + 1` => O(m).


test: list[int] = [2, 3, 4, 7, 11]
test_k: int = 5
test_out: int = 9
assert test_out == find_kth_positive(test, test_k)

test = [1, 2, 3, 4]
test_k = 2
test_out = 6
assert test_out == find_kth_positive(test, test_k)

test = sorted(set([randint(1, 1000) for _ in range(1000)]))
print(test)
