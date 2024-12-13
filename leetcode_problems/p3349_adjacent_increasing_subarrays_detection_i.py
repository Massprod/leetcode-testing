# Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays
#  of length k such that both subarrays are strictly increasing.
# Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
#  - Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
#  - The subarrays must be adjacent, meaning b = a + k.
# Return true if it is possible to find two such subarrays, and false otherwise.
# ---------------------
# 2 <= nums.length <= 100
# 1 < 2 * k <= nums.length
# -1000 <= nums[i] <= 1000
import pyperclip
from random import randint


def has_increasing_subarrays(nums: list[int], k: int) -> bool:
    # working_sol: (92.32%, 8.96%) -> (72ms, 17.17mb)  time: O(n) | space: O(1)
    # Any 2 values will be correct.
    # And we're guaranteed -> 2 <= nums.length <= 100
    if 1 == k:
        return True
    # All we care about is two sequences of length `k`.
    # With starting points differs by `k`.
    start_1: int = 0
    start_2: int = start_1 + k
    sequence: int = 1
    while len(nums) > start_2 + 1:
        # Expand if we can.
        if (nums[start_1] < nums[start_1 + 1]
            and nums[start_2] < nums[start_2 + 1]):
            sequence += 1
        # Start a new sequences.
        else:
            sequence = 1
        if k == sequence:
            return True
        start_1 += 1
        start_2 += 1
    return False


# Time complexity: O(n)
# Always using every index of the `nums`, once => O(n).
# ---------------------
# Auxiliary space: O(1)
# Only 3 constant INT's used, none of them depends on input => O(1).


test: list[int] = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
test_k: int = 3
test_out: bool = True
assert test_out == has_increasing_subarrays(test, test_k)

test = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
test_k = 5
test_out = False
assert test_out == has_increasing_subarrays(test, test_k)

test = [randint(-1000, 1000) for _ in range(100)]
pyperclip.copy(test)
