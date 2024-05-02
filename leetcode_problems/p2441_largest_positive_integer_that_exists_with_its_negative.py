# Given an integer array nums that does not contain any zeros,
#  find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.
# ------------------------------
# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# nums[i] != 0
from random import randint, choice


def find_max_k(nums: list[int]) -> int:
    # working_sol (87.14%, 98.70%) -> (102ms, 16.66mb)  time: O(n) | space: O(n)
    uniques: set[int] = set(nums)
    out: int = -1
    for num in uniques:
        if (num > 0 and num * -1) in uniques:
            out = max(out, num)
    return out


# Time complexity: O(n) <- n - length of an input array `nums`
# We're traversing it once to get all `uniques` from it => O(n).
# And in the worst case, there are only unique values, so we will traverse all of them again => O(2n).
# ------------------------------
# Auxiliary space: O(n)
# Same worst case, we will store all values from `nums` in `uniques` => O(n).


test: list[int] = [-1, 2, -3, 3]
test_out: int = 3
assert test_out == find_max_k(test)

test = [-1, 10, 6, 7, -7, 1]
test_out = 7
assert test_out == find_max_k(test)

test = [-10, 8, 6, 7, -2, -3]
test_out = -1
assert test_out == find_max_k(test)

test = [choice([randint(-1000, -1), randint(1, 1000)]) for _ in range(1000)]
print(test)
