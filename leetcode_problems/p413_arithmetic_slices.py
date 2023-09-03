# An integer array is called arithmetic if it consists of at least three elements
#  and if the difference between any two consecutive elements is the same.
# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.
# A subarray is a contiguous subsequence of the array.
# ------------------
# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000
from random import randint


def number_of_ari_slices(nums: list[int]) -> int:
    # working_sol (91.1%, 60.45%) -> (39ms, 16.6mb)  time: O(n * n) | space: O(n * n)
    ari_count: int = 0
    if len(nums) < 3:
        return ari_count
    recur_cache: dict[tuple[int, int], bool] = {}

    def check(start: int, end: int) -> int:
        # len < 3
        if 0 < end - start < 2:
            return 0
        # Already included.
        if (start, end) in recur_cache:
            return 0
        # Always starting with correct ari_sequence.
        count: int = 1
        # Count every correct we can get from deleting,
        #  last or first element.
        count += check(start + 1, end)
        count += check(start, end - 1)
        # Value doesn't matter, just a placeholder.
        recur_cache[start, end] = True
        return count

    # Building with a sliding window.
    left_l: int = 0
    right_l: int = 1
    diff: int = 0
    correct: bool = False
    while left_l != len(nums):
        # If we still have something to use.
        if right_l < len(nums):
            # Resetting indexes when sequence is broken,
            #  so everytime we need to get new diff.
            if (right_l - left_l) == 1:
                diff: int = nums[right_l] - nums[left_l]
                # right_limit expends by 1 on every diff check.
                right_l += 1
                continue
            # If sequence is still correct, trying to build max size as possible.
            if (nums[right_l] - nums[right_l - 1]) == diff:
                right_l += 1
                correct = True
                continue
        # If we build correct sequence.
        if correct:
            # Count subarrays in it. Cuz every subarray with len >= 3,
            #  in this sequence is arithmetic sequence as well.
            ari_count += check(left_l, right_l - 1)
            # Reset left_limit on the last element of this sequence.
            left_l = right_l - 1
            # Building a new one.
            correct = False
            continue
        # If we didn't build one with this limit,
        #  try to shift it by 1 index, and recheck.
        left_l += 1
        correct = False

    return ari_count


# Time complexity: O(n * n) -> traversing whole input_array indexes once => O(n) -> if at any moment we had build
# n - len of input_array^^| correct ari_sequence then we're calling check() to count all it's subarrays ->
#                           -> worst case, sequence is correct for whole input_array ->
#                           -> then we're checking all pairs of indexes of input_array, once => O(n * n).
# Auxiliary space: O(n * n) -> using dictionary as a cache to store recursion arg_calls, calls are made for every
#                           pair of indexes in the worst case => O(n * n).


test: list[int] = [1, 2, 3, 4]
test_out: int = 3
assert test_out == number_of_ari_slices(test)

test = [1]
test_out = 0
assert test_out == number_of_ari_slices(test)

# test -> Failed -> I was sorting whole input array, when we should consider original indexes.
test = [
    -591, 222, -88, 667, 785, 524, 140, -16, -165, -518, 200, 300, 400,
    -547, 705, -417, -406, -769, 68, 287, 646, -653, 781, 267, -460
]
test_out = 1
assert test_out == number_of_ari_slices(test)

# test -> Failed -> Incorrectly used cache, when we increment every call we don't need to return Value stored.
#                   It's needs to be just ignored.
test = [1, 2, 3, 4, 5, 6]
test_out = 10
assert test_out == number_of_ari_slices(test)

# test -> Failed -> Incorrectly reset left_limit as right_limit not (right_limit - 1)
test = [1, 2, 3, 5, 7]
test_out = 2
assert test_out == number_of_ari_slices(test)

test = [randint(-1000, 1000) for _ in range(5000)]
print(test)
