# Given an array of integers nums and an integer k.
# A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.
# ---------------------
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10 ** 5
# 1 <= k <= nums.length
from collections import deque


def number_of_subarrays(nums: list[int], k: int) -> int:
    # working_sol (95.75%, 93.80%) -> (560ms, 23.25mb)  time: O(n) | space: O(n)
    out: int = 0
    if k > len(nums):
        return out
    # [index] <- indexes of the ODD values we meet.
    odds: deque[int] = deque([])
    # We need `continuous` subarrays.
    # So, all we actually care about is - if our current window has `k` ODDs in it or not.
    # And if it does, we can build some `g` subarrays from `start` to our FIRST ODD value index.
    start: int = -1
    for index, num in enumerate(nums):
        if num % 2:
            odds.append(index)
        # Repeat for every window reset.
        if k < len(odds):
            start = odds.popleft()
        if k == len(odds):
            out += odds[0] - start
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# In the worst case, we're going to have `k` = 1, and every value is going to be an ODD number.
# So, we will append every value and pop (n - 1) elements => O(n + (n - 1)).
# ---------------------
# Auxiliary space: O(n)
# In the worst case, we're going to have `k` == `n` and every value is going to be an ODD number.
# So, we will have `odds` with the size of `n` => O(n).


test: list[int] = [1, 1, 2, 1, 1]
test_k: int = 3
test_out: int = 2
assert test_out == number_of_subarrays(test, test_k)

test = [2, 4, 6]
test_k = 1
test_out = 0
assert test_out == number_of_subarrays(test, test_k)

test = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
test_k = 2
test_out = 16
assert test_out == number_of_subarrays(test, test_k)
