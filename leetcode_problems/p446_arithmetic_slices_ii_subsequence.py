# Given an integer array nums, return the number of all the arithmetic subsequences of nums.
# A sequence of numbers is called arithmetic if it consists of at least three elements
#  and if the difference between any two consecutive elements is the same.
#   - For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
#   - For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
# A subsequence of an array is a sequence that can be formed by removing some elements
#  (possibly none) of the array.
#   - For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# The test cases are generated so that the answer fits in 32-bit integer.
# --------------------------
# 1  <= nums.length <= 1000
# -2 ** 31 <= nums[i] <= 2 ** 31 - 1
from random import randint


def number_of_arithmetic_slices(nums: list[int]) -> int:
    # working_sol (81.30%, 17.63%) -> (455ms, 107.97mb)  time: O(n ** 2) | space: O(n ** 2)
    # {(index, arith_diff): # of sequences which ends on this index}
    all_sequences: dict[tuple[int, int], int] = {}
    # All sequences with length >= 3.
    out: int = 0
    for end in range(1, len(nums)):
        for start in range(0, end):
            arith_diff: int = nums[end] - nums[start]
            # New sequence with length == 2, which ends on `end` index.
            if (end, arith_diff) not in all_sequences:
                all_sequences[end, arith_diff] = 1
            # Other sequence with length == 2, which also ends on `end` index.
            # Like: [2, 2, 3, 4] -> [2, 3] + [2, 3] we need both of them.
            else:
                all_sequences[end, arith_diff] += 1
            # We already have sequences which ends on `start` index, and we can continue it with `nums[end]`.
            # Like: [2, 2, 3, 4], start == 2, end == 3 => [2, 3, 4] + [2, 3, 4]
            if (start, arith_diff) in all_sequences:
                all_sequences[end, arith_diff] += all_sequences[start, arith_diff]
                # And we only care about how many sequences we continued from default size == 2.
                out += all_sequences[start, arith_diff]
    return out


# Time complexity: O(n ** 2) <- n - length of input array `nums`.
# We check every pair of indexes in `nums` => O(n ** 2).
# --------------------------
# Auxiliary space: O(n ** 2).
# For every pair we check, we find arithmetic difference `arith_diff` between them.
# Worst case: every pair will have different `arith_diff`.
# So, we will store every pair we check => O(n ** 2).


test: list[int] = [2, 4, 6, 8, 10]
test_out: int = 7
assert test_out == number_of_arithmetic_slices(test)

test = [7, 7, 7, 7, 7]
test_out = 16
assert test_out == number_of_arithmetic_slices(test)

test = [2, 2, 3, 4]
test_out = 2
assert test_out == number_of_arithmetic_slices(test)

test = [randint(-2 ** 31, 2 ** 31 - 1) for _ in range(1000)]
print(test)
