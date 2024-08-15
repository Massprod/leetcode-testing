# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
#  - Each element belongs to exactly one pair.
#  - The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.
# -------------------------
# nums.length == 2 * n
# 1 <= n <= 500
# 1 <= nums[i] <= 500
from random import randint
from collections import Counter


def divide_array(nums: list[int]) -> bool:
    # working_sol (82.84%, 40.66%) -> (74ms, 16.76mb)  time: O(n) | space: O(n)
    # 2 * n => we can build n pairs.
    # ! The elements present in a pair are equal. !
    # And all of them should contain the same elements.
    # So, we should always have all unique elements presented as (`occurs` % 2 == 0).
    occurrences: dict[int, int] = Counter(nums)
    for val in occurrences.values():
        if val % 2:
            return False
    return True


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums` to get all occurrences of the values, once => O(n).
# If there's `n // 2` pairs, then we're extra traversing them => O(n + n // 2).
# -------------------------
# Auxiliary space: O(n)
# `occurrences` <- in the worst case will hold every `num` from `nums` => O(n).


test: list[int] = [3, 2, 3, 2, 2, 2]
test_out: bool = True
assert test_out == divide_array(test)

test = [1, 2, 3, 4]
test_out = False
assert test_out == divide_array(test)

test = [randint(1, 500) for _ in range(500)]
print(test)
