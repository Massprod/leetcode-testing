# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# -----------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from collections import Counter


def num_ident_pairs(nums: list[int]) -> int:
    # working_sol (87.1%, 53.10%) -> (35ms, 16.2mb)  time: O(n) | space: O(n)
    uniques: dict[int, int] = Counter(nums)
    pairs: int = 0
    # ! pairs == n * (n – 1) // 2 ! <- for any unique number.
    for unique in uniques:
        pairs += (uniques[unique] * (uniques[unique] - 1)) // 2
    return pairs


# Time complexity: O(n) -> count every unique value => O(n) -> extra traverse of every unique to count pairs ->
# n - len of input array^^| -> worst case == everything is unique, just traversing all indexes(keys) again => O(n).
# Auxiliary space: O(n) -> same worst case == dictionary will store every index => O(n).
# -----------------
# ! n * (n – 1) // 2 ! <- for any unique number.


test: list[int] = [1, 2, 3, 1, 1, 3]
test_out: int = 4
assert test_out == num_ident_pairs(test)

test = [1, 1, 1, 1]
test_out = 6
assert test_out == num_ident_pairs(test)

test = [1, 2, 3]
test_out = 0
assert test_out == num_ident_pairs(test)
