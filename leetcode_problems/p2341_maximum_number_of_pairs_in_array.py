# You are given a 0-indexed integer array nums. In one operation, you may do the following:
#   Choose two integers in nums that are equal.
#   Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.
# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs
#   that are formed and answer[1] is the number of leftover integers in nums after
#   doing the operation as many times as possible.
# -------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


def number_of_pairs(nums: list[int]) -> list[int]:
    # working_sol (88.59%, 69.37%) -> (40ms, 16.2mb)  time: O(n) | space: O(1)
    # Inplace, should be slower but dict() is too obvious.
    # After sorting all values can be counted before breakpoint.
    nums.sort()
    answer: list[int] = [0, 0]
    val_occur: int = 0
    for x in range(len(nums)):
        # Breakpoint, reset counter and calc pairs.
        if nums[x] != nums[x - 1]:
            # Floor == all pairs.
            answer[0] += val_occur // 2
            # Leftovers.
            answer[1] += val_occur % 2
            val_occur = 0
        # Count every unique value.
        val_occur += 1
    # Last index ignored in a loop, so we need extra calc.
    answer[0] += val_occur // 2
    answer[1] += val_occur % 2
    return answer


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> nothing depends on input => O(1).
# -------------------
# See at least 2 ways to solve it: inplace with sorting and dictionary with counting.
# Dictionary is too obvious so, let's try inplace.


test: list[int] = [1, 3, 2, 1, 3, 2, 2]
test_out: list[int] = [3, 1]
assert test_out == number_of_pairs(test)

test = [1, 1]
test_out = [1, 0]
assert test_out == number_of_pairs(test)

test = [0]
test_out = [0, 1]
assert test_out == number_of_pairs(test)
