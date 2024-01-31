# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
# A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
#   - i < j < k,
#   - nums[j] - nums[i] == diff, and
#   - nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.
# ------------------
# 3 <= nums.length <= 200
# 0 <= nums[i] <= 200
# 1 <= diff <= 50
# nums is strictly increasing.
from random import randint
from collections import defaultdict


def arithm_triplets(nums: list[int], diff: int) -> int:
    # working_sol (90.64%, 64.67%) -> (38ms, 16.54mb)  time: O(n) | space: O(n)
    out: int = 0
    # {value: indexes of this value}
    left_side: dict[int, int] = defaultdict(int)
    # i < j < k
    # nums[j] - nums[i] = diff AND nums[k] - nums[j] = diff
    # nums[j] = diff + nums[i] AND nums[k] = diff + nums[j]
    # nums[k] = diff + diff + nums[i]
    # If we start from last value, we need to find:
    #  nums[j] = nums[k] - diff AND nums[i] = nums[k] - diff - diff
    for _ in range(2):
        left_side[nums[_]] += 1
    for k in range(2, len(nums)):
        nums_j: int = nums[k] - diff
        nums_i: int = nums_j - diff
        if nums_j in left_side and nums_i in left_side:
            # We can use all index combinations to get uniques (i, j, k):
            # Like: [1, 1, 2, 2, 3] => 1 = 2occ, 2 = 2occ => [0, 2, 4], [0, 3, 4], [1, 2, 4], [1, 3, 4]
            out += left_side[nums_j] * left_side[nums_i]
        left_side[nums[k]] += 1
    return out


# Time complexity: O(n) <- n - length of input array `nums`.
# Traversing whole input array, once => O(n).
# ------------------
# Auxiliary space: O(n).
# We're always given `nums` strictly increasing, so we're always going to have unique values.
# And all these unique values always stored in `left_side` => O(n).


test: list[int] = [0, 1, 4, 6, 7, 10]
test_diff: int = 3
test_out: int = 2
assert test_out == arithm_triplets(test, test_diff)

test = [4, 5, 6, 7, 8, 9]
test_diff = 2
test_out = 2
assert test_out == arithm_triplets(test, test_diff)

test = sorted(set([randint(0, 200) for _ in range(200)]))
print(test)
