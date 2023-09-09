# Given an array of distinct integers nums and a target integer target,
#  return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.
# ----------------
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
from random import randint


def combination_sum(nums: list[int], target: int) -> int:
    # working_sol (97.25%, 84.76%) -> (48ms, 16.3mb)  time: O(m * n) | space: O(m)
    recur_cache: dict[int, int] = {}

    def check(cur_target: int) -> int:
        if cur_target in recur_cache:
            return recur_cache[cur_target]
        # All we care is that we get target.
        elif cur_target == 0:
            return 1
        # Or exceed it, all values are positive no reasons to check more.
        elif cur_target < 0:
            return 0
        combs: int = 0
        # Combinations -> we don't care about order and allowed to reuse.
        # Just take everything we can and check.
        for num in nums:
            combs += check(cur_target - num)
        # Cache, we always have same values to use, so we can cull same targets.
        recur_cache[cur_target] = combs
        return combs

    return check(target)


# Time complexity: O(m * n) -> with cache we will store every possible result of (cur_target - num) and in worst case,
# n - len of input_array^^| it's going to be target itself, target - 1, -1 ,-1, -1 -> for every call with these results
# m - input target^^|       we're using all possible nums from input_array => O(m * n).
# Auxiliary space: O(m) -> dict_cache to store all (cur_target - num) results with same worst case never exceeds target
#                          extra recursion stack with same size of m => O(2m).


test: list[int] = [1, 2, 3]
test_t: int = 4
test_out: int = 7
assert test_out == combination_sum(test, test_t)

test = [9]
test_t = 3
test_out = 0
assert test_out == combination_sum(test, test_t)
