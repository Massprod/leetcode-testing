# Given the array nums, for each nums[i] find out how many numbers
#  in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's
#  such that j != i and nums[j] < nums[i].
# Return the answer in an array.
# ----------------------
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100
from random import randint


def smaller_than_current(nums: list[int]) -> list[int]:
    # working_sol (93.76%, 18.78%) -> (46ms, 16.63mb)  time: O(n * log n) | space: O(n)
    # [(original_index, value)]
    nums_sorted: list[tuple[int, int]] = sorted(
        [(index, value) for index, value in enumerate(nums)], key=lambda x: x[1]
    )
    # [number of smaller values]
    out: list[int] = [0 for _ in nums]
    cur_smaller: int = 0
    for index in range(1, len(nums_sorted)):
        # Equal values in sequence == same number of smaller values.
        if nums_sorted[index][1] != nums_sorted[index - 1][1]:
            cur_smaller = index
        out[nums_sorted[index][0]] = cur_smaller
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting original array `nums` and extra traversing it => O(n * log n + n).
# ----------------------
# Auxiliary space: O(n).
# `nums_sorted` <- always of the same size as `nums` => O(n).
# `out` <- extra array with the same size as `nums` => O(2 * n).


test: list[int] = [8, 1, 2, 2, 3]
test_out: list[int] = [4, 0, 1, 1, 3]
assert test_out == smaller_than_current(test)

test = [6, 5, 4, 8]
test_out = [2, 1, 0, 3]
assert test_out == smaller_than_current(test)

test = [7, 7, 7, 7]
test_out = [0, 0, 0, 0]
assert test_out == smaller_than_current(test)

test = [randint(0, 100) for _ in range(500)]
print(test)
