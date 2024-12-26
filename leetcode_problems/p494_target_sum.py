# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+'
#  and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
#  and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build,
#  which evaluates to target.
# ----------------------------
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
import pyperclip
from random import randint
from functools import cache


def find_target_sumways(nums: list[int], target: int) -> int:
    # working_sol (64.96%, 5.57%) -> (151ms, 45.24mb)  time: O(n * s) | space: O(n * s)

    @cache
    def check(index: int, cur_sum: int) -> int:
        if index >= len(nums):
            return 1 if cur_sum == target else 0
        
        out: int = 0
        new_sum: int = cur_sum + nums[index]
        out += check(index + 1, new_sum)
        new_sum = cur_sum - nums[index]
        out += check(index + 1, new_sum)
        return out

    return check(0, 0)


# Time complexity: O(n * s) <- n - length of the input array `nums`,
#                              s - number of unique `cur_sum` value appr == sum(nums).
# We always check every index and unique `cur_sum` combination on it => O(n * s).
# ---------------------------- 
# Auxiliary space: O(n * s)
# All of the combination is cached with `cache` => O(n * s).


test: list[int] = [1, 1, 1, 1, 1]
test_target: int = 3
test_out: int = 5
assert test_out == find_target_sumways(test, test_target)

test = [1]
test_target = 1
test_out = 1
assert test_out == find_target_sumways(test, test_target)

test = [randint(0, 20) for _ in range(20)]
pyperclip.copy(test)
