# Given a 0-indexed integer array nums of length n and an integer k,
#  return the number of pairs (i, j) where 0 <= i < j < n,
#  such that nums[i] == nums[j] and (i * j) is divisible by k.
# ------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i], k <= 100
from random import randint


def count_pairs(nums: list[int], k: int) -> int:
    # working_sol (89.99%, 18.18%) -> (58ms, 16.72mb)  time: O(n * n) | space: O(n)
    out: int = 0
    # { value: [indexes where occur] }
    val_indexes: dict[int, list[int]] = {}
    for index, num in enumerate(nums):
        if num in val_indexes:
            val_indexes[num].append(index)
        else:
            val_indexes[num] = [index]
    for occurrences in val_indexes.values():
        if 1 == len(occurrences):
            continue
        for i in range(len(occurrences)):
            for j in range(i + 1, len(occurrences)):
                if not ((occurrences[i] * occurrences[j]) % k):
                    out += 1
    return out


# Time complexity: O(n * n) <- n - length of the input array `nums`.
# In the worst case, an array contains only 1 value.
# And we will use every index of the array in nested loop => O(n * n).
# ------------------------
# Auxiliary space: O(n)
# All indexes of the input array `nums` is always stored in `val_indexes` values => O(n).


test: list[int] = [3, 1, 2, 2, 2, 1, 3]
test_k: int = 2
test_out: int = 4
assert test_out == count_pairs(test, test_k)

test = [1, 2, 3, 4]
test_k = 1
test_out = 0
assert test_out == count_pairs(test, test_k)

test = [randint(1, 100) for _ in range(100)]
print(test)
