# You are given an array nums that consists of non-negative integers.
# Let us define rev(x) as the reverse of the non-negative integer x.
# For example, rev(123) = 321, and rev(120) = 21.
# A pair of indices (i, j) is nice if it satisfies all of the following conditions:
#  - 0 <= i < j < nums.length
#  - nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices.
# Since that number can be too large, return it modulo 10 ** 9 + 7.
# -------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 10 ** 9
from random import randint


def count_nice_pairs(nums: list[int]) -> int:
    # working_sol (80.45%, 61.19%) -> (562ms, 26.7mb)  time: O(n) | space: O(n)
    # (unique result: encounters so far)
    unique_values: dict[int, int] = {}
    pairs: int = 0
    # right -> left , we can reuse everything we already met.
    for x in range(len(nums) - 1, -1, -1):
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        value: int = nums[x] - int(str(nums[x])[::-1])
        if value in unique_values:
            pairs += unique_values[value]
            unique_values[value] += 1
        else:
            unique_values[value] = 1
    return pairs % (10 ** 9 + 7)


# Time complexity: O(n) -> traversing whole input array 'nums' once => O(n).
# n - len of input array 'nums'^^|
# Auxiliary space: O(n) -> worst case == every resulting value in nums is unique -> we will store every result => O(n).


test: list[int] = [42, 11, 1, 97]
test_out: int = 2
assert test_out == count_nice_pairs(test)

test = [13, 10, 35, 24, 76]
test_out = 4
assert test_out == count_nice_pairs(test)

test = [randint(0, 10 ** 9) for _ in range(10 ** 4)]
# print(test)
