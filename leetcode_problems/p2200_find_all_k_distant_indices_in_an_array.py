# You are given a 0-indexed integer array nums and two integers key and k.
# A k-distant index is an index i of nums for which there exists
#  at least one index j such that |i - j| <= k and nums[j] == key.
# Return a list of all k-distant indices sorted in increasing order.
# -----------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# key is an integer from the array nums.
# 1 <= k <= nums.length
from random import randint


def find_k_distant_indices(nums: list[int], key: int, k: int) -> list[int]:
    # working_sol (26.32%, 39.34%) -> (269ms, 16.85mb)  time: O(n * n) | space: O(n)

    def fill_range(start: int) -> None:
        for ind in range(start - k, start + k + 1):
            if 0 <= ind < len(nums):
                if key == nums[ind]:
                    nums[ind] = -1
                    fill_range(ind)
                    break
                nums[ind] = -1

    for index in range(len(nums)):
        if key == nums[index]:
            nums[index] = -1
            fill_range(index)

    out: list[int] = []
    for index in range(len(nums)):
        if -1 == nums[index]:
            out.append(index)
    return out


# Time complexity: O(n * n) <- n - length of the input array `nums`.
# We're culling some loops, when we're getting already checked `-1`,
#  but still we're going to check all the ranges for every index => O(n * n).
# -----------------------
# Auxiliary space: O(n)
# `out` <- will allocate space for each value from `nums` => O(n).


test: list[int] = [3, 4, 9, 1, 3, 9, 5]
test_key: int = 9
test_k: int = 1
test_out: list[int] = [1, 2, 3, 4, 5, 6]
assert test_out == find_k_distant_indices(test, test_key, test_k)

test = [2, 2, 2, 2, 2]
test_key = 2
test_k = 2
test_out = [0, 1, 2, 3, 4]
assert test_out == find_k_distant_indices(test, test_key, test_k)

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_key = 2
test_k = 5
test_out = [0, 1, 2, 3, 4, 5, 6]
assert test_out == find_k_distant_indices(test, test_key, test_k)

test = [randint(1, 1000) for _ in range(1000)]
print(test)
