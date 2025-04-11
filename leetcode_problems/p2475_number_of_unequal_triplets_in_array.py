# You are given a 0-indexed array of positive integers nums.
# Find the number of triplets (i, j, k) that meet the following conditions:
#  - 0 <= i < j < k < nums.length
#  - nums[i], nums[j], and nums[k] are pairwise distinct.
#    - In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
# Return the number of triplets that meet the conditions.
# -------------------------
# 3 <= nums.length <= 100
# 1 <= nums[i] <= 1000
from random import randint

from pyperclip import copy


def unequal_triplets(nums: list[int]) -> int:
    # working_sol (55.70%, 97.34%) -> (251ms, 17.52mb)  time: O(n ** 3) | space: O(1)
    out: int = 0
    for index in range(len(nums)):
        for index_2 in range(index + 1, len(nums)):
            for index_3 in range(index_2 + 1, len(nums)):
                if (nums[index] != nums[index_2]
                    and nums[index] != nums[index_3]
                    and nums[index_2] != nums[index_3]):
                    out += 1
    
    return out


# Time complexity: O(n ** 3) <- n - length of the input array `nums`.
# 3 nested loops over the input array `nums` => O(n ** 3).
# -------------------------
# Auxiliary space: O(1)


test: list[int] = [4, 4, 2, 4, 3]
test_out: int = 3
assert test_out == unequal_triplets(test)

test = [1, 1, 1, 1, 1]
test_out = 0
assert test_out == unequal_triplets(test)

test = [randint(1, 1000) for _ in range(100)]
copy(test)
