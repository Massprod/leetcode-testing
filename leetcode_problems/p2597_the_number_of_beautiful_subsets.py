# You are given an array nums of positive integers and a positive integer k.
# A subset of nums is beautiful if it does not contain two integers
#  with an absolute difference equal to k.
# Return the number of non-empty beautiful subsets of the array nums.
# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums.
# Two subsets are different if and only if the chosen indices to delete are different.
# ------------------------------
# 1 <= nums.length <= 20
# 1 <= nums[i], k <= 1000
from collections import defaultdict


def beautiful_subsets(nums: list[int], k: int) -> int:
    # working_sol (41.83%, 84.32%) -> (2992ms, 16.52mb)  time: O(2 ** n) | space; O(n)
    # After sorting we can guarantee that we need to check only ! nums[index] - k !
    nums.sort()
    # {value: marker of usage in a subset}
    used_values: dict[int, int] = defaultdict(int)

    def check(index: int, already_used: dict[int, int]) -> int:
        if index == len(nums):
            return 1
        skip: int = check(index + 1, already_used)
        take: int = 0
        if (nums[index] - k) not in already_used:
            already_used[nums[index]] += 1
            take = check(index + 1, already_used)
            already_used[nums[index]] -= 1
            if 0 == already_used[nums[index]]:
                del already_used[nums[index]]
        return skip + take

    return check(0, used_values) - 1


# Time complexity: O(2 ** n) <- n- length of an input array `nums`.
# Sorting with basic python `sort()` => O(n * log n).
# Subset generation with a recursion => O(2 ** n)
# ------------------------------
# Auxiliary space: O(n)
# In the worst case: stores all values from `nums` in `already_used`, and recursion stack is `n` as well => O(2n).


test: list[int] = [2, 4, 6]
test_k: int = 2
test_out: int = 4
assert test_out == beautiful_subsets(test, test_k)

test = [1]
test_k = 1
test_out = 1
assert test_out == beautiful_subsets(test, test_k)
