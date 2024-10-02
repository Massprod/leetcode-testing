# Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
#  - nums[a] + nums[b] + nums[c] == nums[d], and
#  - a < b < c < d
# -------------------
# 4 <= nums.length <= 50
# 1 <= nums[i] <= 100
import bisect
from random import randint


def count_quadruplets(nums: list[int]) -> int:
    # working_sol (68.68%, 71.08%) -> (289ms, 16.49mb)  time: O(n ** 3) | space: O(n)
    out: int = 0
    # { value: [index] }
    sum_values: dict[int, list[int]] = {}
    for index, value in enumerate(nums):
        if value in sum_values:
            sum_values[value].append(index)
        else:
            sum_values[value] = [index]

    def check(index: int, path: list[int]) -> None:
        nonlocal out
        nonlocal sum_values
        sum_path: int
        if 3 == len(path):
            sum_path = sum(path)
            if sum_path in sum_values:
                # We can use indexes with only HIGHER values.
                # So, we should find a place where we can place our current index.
                # And everything after it can be used.
                out += len(sum_values[sum_path]) - bisect.bisect_left(sum_values[sum_path], index)
            return
        for new_index in range(index + 1, len(nums)):
            check(new_index, path + [nums[new_index]])

    for start in range(len(nums)):
        check(start, [nums[start]])
    return out


# Time complexity: O(n ** 3) <- n - length of the input array `nums`.
# Traversing `num` once to get all the values, and their indexes of occurrences => O(n)
# Always using 3 calls to check == 3 nested loops to check all the quadruplets => O(n + n ** 3).
# -------------------
# Auxiliary space: O(n)
# `sum_values` <- stores all indexes of `nums` => O(n).
# `path` <- always contains at most 3 elements, we can count it as constant.


test: list[int] = [1, 2, 3, 6]
test_out: int = 1
assert test_out == count_quadruplets(test)

test = [3, 3, 6, 4, 5]
test_out = 0
assert test_out == count_quadruplets(test)

test = [1, 1, 1, 3, 5]
test_out = 4
assert test_out == count_quadruplets(test)

test = [randint(1, 100) for _ in range(50)]
print(test)
