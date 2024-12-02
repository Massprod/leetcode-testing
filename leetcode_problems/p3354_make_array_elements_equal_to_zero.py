# You are given an integer array nums.
# Start by selecting a starting position curr such that nums[curr] == 0,
#  and choose a movement direction of either left or right.
# After that, you repeat the following process:
#  - If curr is out of the range [0, n - 1], this process ends.
#  - If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right,
#    or decrementing curr if you are moving left.
#  - Else if nums[curr] > 0:
#   - Decrement nums[curr] by 1.
#   - Reverse your movement direction (left becomes right and vice versa).
#   - Take a step in your new direction.
# A selection of the initial position curr and movement direction is considered valid
#  if every element in nums becomes 0 by the end of the process.
# Return the number of possible valid selections.
# -------------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# There is at least one element i where nums[i] == 0.
from random import randint


def count_valid_selections(nums: list[int]) -> int:
    # working_sol (95.68%, 14.28%) -> (37ms, 17.39mb)  time: O(n) | space: O(n)
    # We need either equal prefix == suffix.
    # Or we need difference between them to be equal to 1,
    #  so we could clear it in one move.
    out: int = 0
    prefix: int = 0
    prefixes: list[int] = []
    for val in nums:
        prefixes.append(prefix)
        prefix += val
    suffix: int = 0
    suffixes: list[int] = []
    for val in nums[::-1]:
        suffixes.append(suffix)
        suffix += val
    prefix_index: int = 0
    suffix_index: int = len(nums) - 1
    while prefix_index < len(prefixes):
        if nums[prefix_index]:
            prefix_index += 1
            suffix_index -= 1
            continue
        cur_prefix: int = prefixes[prefix_index]
        cur_suffix: int = suffixes[suffix_index]
        if cur_prefix == cur_suffix:
            out += 2
        elif 1 == abs(cur_prefix - cur_suffix):
            out += 1
        prefix_index += 1
        suffix_index -= 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, twice to get suffixes and prefixes => O(2 * n).
# Extra traversing all suffixes and prefixes to get correct pairs => O(3 * n).
# -------------------------
# Auxiliary space: O(n).
# `prefixes` <- allocates space for all prefixes == `n` => O(n).
# `suffixes` <- allocates space for all suffixes == `n` => O(2 * n).


test: list[int] = [1, 0, 2, 0, 3]
test_out: int = 2
assert test_out == count_valid_selections(test)

test = [2, 3, 4, 0, 4, 1, 0]
test_out = 0
assert test_out == count_valid_selections(test)

test = [16, 13, 10, 0, 0, 0, 10, 6, 7, 8, 7]
test_out = 3
assert test_out == count_valid_selections(test)

test = [randint(0, 100) for _ in range(100)]
print(test)
