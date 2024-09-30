# You are given a 0-indexed integer array nums and an integer k.
# Your task is to perform the following operation exactly k times in order to maximize your score:
# 1. Select an element m from nums.
# 2. Remove the selected element m from the array.
# 3. Add a new element with a value of m + 1 to the array.
# 4. Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.
# -----------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 100
from random import randint


def maximize_sum(nums: list[int], k: int) -> int:
    # working_sol (67.09%, 86.65%) -> (143ms, 16.50mb)  time: O(n + k) | space: O(1)
    out: int = 0
    max_val: int = max(nums)
    while k:
        out += max_val
        max_val += 1
        k -= 1
    return out


# Time complexity: O(n + k) <- n - length of the input array `nums`.
# Always traversing whole `nums` to get maximum value to use => O(n).
# Incrementing and adding this value for `k` times => O(n + k).
# -----------------------------
# Auxiliary space: O(1)
# Only 2 extra INTs used, none of them depends on input => O(1).


test: list[int] = [1, 2, 3, 4, 5]
test_k: int = 3
test_out: int = 18
assert test_out == maximize_sum(test, test_k)

test = [5, 5, 5]
test_k = 2
test_out = 11
assert test_out == maximize_sum(test, test_k)

test = [randint(1, 100) for _ in range(100)]
print(test)
