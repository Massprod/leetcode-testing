# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# -------------------
# 1 <= nums.length <= 2500
# -10 ** 4 <= nums[i] <= 10 ** 4
# -------------------
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
from random import randint


def length_of_list(nums: list[int]) -> int:
    # working_sol (88.27%, 78.43%) -> (74ms, 16.57mb)  time: O(n * log n) | space: O(n)
    def bs(array: list[int], value: int) -> int:
        """
        Binary search to get index in the array,
        for whom all the values on the left side of it is lower than `value`.
        """
        left: int = 0
        right: int = len(array)
        while left < right:
            middle: int = (left + right) // 2
            if value > array[middle]:
                left = middle + 1
            else:
                right = middle
        return left

    sequence: list[int] = [nums[0]]
    for x in range(1, len(nums)):
        index: int = bs(sequence, nums[x])
        # nums[x] higher than everything in sequence => continuation of maximum sequence.
        if index == len(sequence):
            sequence.append(nums[x])
        # nums[x] lower than everything or some part of the sequence.
        # [1, 3, 4] , nums[x] = 2 => [2, 3, 4] , nums[x] = 10 => [2, 3, 4, 10].
        # (2, 3, 4, 10) <- incorrect sequence.
        # But, because we replaced 1 with 2 we still have correct length for sequence (1, 3, 4, 10).
        # So, every value we replace is still here, but only in length terms.
        # (2, 3, 4, 10) , nums[x] = 5 => [2, 3, 4, 5] -> (1, 3, 4, 5) or (2, 5) sequences.
        else:
            sequence[index] = nums[x]
    return len(sequence)


# Time complexity: O(n * log n) <- length of input array `nums`.
# BinarySearch on every index of `nums`, and we're doing BS on the array with size == (n - 1) in the end.
# O(n * log n).
# -------------------
# Auxiliary space: O(n).
# Worst case: everything is already in ascending order.
# So, we will just recreate original `nums` in `sequence` => O(n).


test: list[int] = [10, 9, 2, 5, 3, 7, 101, 18]
test_out: int = 4
assert test_out == length_of_list(test)

test = [0, 1, 0, 3, 2, 3]
test_out = 4
assert test_out == length_of_list(test)

test = [7, 7, 7, 7, 7, 7, 7]
test_out = 1
assert test_out == length_of_list(test)

test = [randint(-10 ** 4, 10 ** 4) for _ in range(2500)]
print(test)
