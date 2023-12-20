# You are given a 0-indexed integer array nums and an integer k.
# You can perform the following operation on the array at most k times:
#   - Choose any index i from the array and increase or decrease nums[i] by 1.
# The score of the final array is the frequency of the most frequent element in the array.
# Return the maximum score you can achieve.
# The frequency of an element is the number of occurrences of that element in the array.
# --------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# 0 <= k <= 10 ** 14
from collections import Counter
from random import randint


def max_frequency_score(nums: list[int], k: int) -> int:
    # working_sol (71.22%, 5.72%) -> (913ms, 34.9mb)  time: O(n * log n) | space: O(n)
    if k == 0:
        # Maximum sequence of equal values.
        return max(Counter(nums).values())
    nums.sort()
    prefixes: list[int] = [0 for _ in range(len(nums))]
    suffixes: list[int] = [0 for _ in range(len(nums))]
    for x in range(1, len(nums)):
        prefixes[x] = prefixes[x - 1] + nums[x - 1]
    for x in range(len(nums) - 2, -1, -1):
        suffixes[x] = suffixes[x + 1] + nums[x + 1]
    # Leftmost, rightmost indexes of sliding window.
    left: int = 0
    right: int = 0
    max_score: int = 1
    # Expand.
    while right < len(nums) - 1:
        right += 1
        middle: int = (left + right) // 2
        target: int = nums[middle]  # value we want in the whole subarray (left -> right, inclusive)
        # Operations to get subarray in balance, i.e make all values equal to target:
        # (sum of values we need in {left -> middle, middle not inclusive}) - (what we already have)) +
        # + (what we already have) - (sum of values we need in {middle -> right, middle not inclusive})
        balance_cost: int = ((target * (middle - left) - (prefixes[middle] - prefixes[left]))
                             + (suffixes[middle] - suffixes[right] - target * (right - middle)))
        # Shrink, until window is correct.
        while balance_cost > k:
            left += 1
            middle = (left + right) // 2
            target = nums[middle]
            balance_cost = ((target * (middle - left) - (prefixes[middle] - prefixes[left]))
                            + (suffixes[middle] - suffixes[right] - target * (right - middle)))
        max_score = max(max_score, right + 1 - left)  # +1 for 0-indexed.
    return max_score


# Time complexity: O(n * log n) <- n - length of input array `nums`.
# Standard python sort() => O(n * log n).
# Expanding window from 0 -> n - 1, and for every step searching for the middle element(BS) => O(n * log n).
# --------------------
# Auxiliary space: O(n).
# Standard python sort() => O(n).
# `prefixes` and `suffixes` both of size `n` => O(2n).
# Extra 4 constant INTs none of them depends on input.


test: list[int] = [1, 2, 6, 4]
test_k: int = 3
test_out: int = 3
assert test_out == max_frequency_score(test, test_k)

test = [1, 4, 4, 2, 4]
test_k = 0
test_out = 3
assert test_out == max_frequency_score(test, test_k)

test = [1, 2, 6, 4]
test_k = 1
test_out = 2
assert test_out == max_frequency_score(test, test_k)

test = [randint(1, 10 ** 9) for _ in range(10 ** 4)]
print(test)
print('!!!!!!!!!--')
print(10 ** 14)
