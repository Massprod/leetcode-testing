# Given an integer array nums of length n where all the integers of nums are in the range [1, n]
#  and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
# -------------------
# n == nums.length
# 1 <= n <= 10 ** 5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.
from random import shuffle


def find_duplicate(nums: list[int]) -> list[int]:
    # working_sol (35.27%, 67.78%) -> (276, 24.62)  time: O(n) | space: O(1)
    out: list[int] = []
    # We can only have 2 values pointing to the same Index.
    # So, we can just mark this value at the First time,
    #  and if we meet something pointing to this index again.
    # It's a duplicate.
    for num in nums:
        index: int = abs(num) - 1
        if 0 > nums[index]:
            out.append(abs(num))
            continue
        nums[index] = nums[index] * -1
    return out


# Time complexity: O(n) <- n - length of input array `nums`.
# Only traversing whole input array `nums` once.
# -------------------
# Auxiliary space: O(1)
# Constant if we ignore answer array `out`. And it's standard rule to ignore size of the answer.
# Otherwise, we can just change `nums` by deleting everything except values like: VALUE + PLACEHOLDER_VALUE.
# Use smth like (10 ** 5 + VALUE) as unique values and delete them afterward.


test: list[int] = [4, 3, 2, 7, 8, 2, 3, 1]
test_out: list[int] = [3, 2]
assert test_out == find_duplicate(test)

test = [1, 1, 2]
test_out = [1]
assert test_out == find_duplicate(test)

test = [1]
test_out = []
assert test_out == find_duplicate(test)

test = [num for num in range(1, 10 ** 5)]
shuffle(test)
print(test)
