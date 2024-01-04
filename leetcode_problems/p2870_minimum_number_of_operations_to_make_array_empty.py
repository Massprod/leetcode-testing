# You are given a 0-indexed array nums consisting of positive integers.
# There are two types of operations that you can apply on the array any number of times:
#   - Choose two elements with equal values and delete them from the array.
#   - Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
# -------------------
# 2 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 6
from random import randint
from collections import Counter


def min_operations(nums: list[int]) -> int:
    # working_sol (97.58%, 18.18%) -> (538ms, 31.6mb)  time: O(n) | space: O(n)
    # {value: occurrences}
    all_vals: dict[int, int] = Counter(nums)
    out: int = 0
    for val in all_vals:
        # We can't delete only 1 occurrence.
        if all_vals[val] == 1:
            return -1
        # We want to maximise use of '3 equal' operations and minimise '2 equal'.
        # We don't care about when we do them, like: value = 14
        # 14 - 3 * 4 - 2 => 5 operations == 14 - 2 - 3 * 4 => 5 operations
        # 14 - 3 * 2 - 2 - 3 * 2 => 5 operations, etc.
        while all_vals[val]:
            if all_vals[val] % 3:
                all_vals[val] -= 2
                out += 1
            else:
                out += all_vals[val] // 3
                all_vals[val] = 0
    return out


# Time complexity: O(n) <- n - length of input array `nums`.
# Single traverse of input array `nums` to count all values and their occurrences => O(n).
# Don't think we can count decrease of values by -2 as constant. But how then?
# Like it's always different, some will be divided in equal parts by 3 and some wil be decreased for 1-2-w.e time.
# We don't know how many. And we can't say (n * k), because we can't have all unique values, it's insta return of - 1.
# W.e let's call it linear, because it's not going to be more than 10 (-2) operations, until we hit (%3).
# And I don't see any dependencies for these (-2) operations from input `nums`.
# -------------------
# Auxiliary space: O(n).
# Worst case: every value is unique, so Counter() will hold all original values from `nums` => O(n).
# -------------------
# Tag is 'Greedy', so it's not DP. Then how what is an optimal way?
# Like: 14 occurrences of w.e value.
# We can delete:
# 14 - 2 == 12 - 2 == 10 - 2 * 5 => 7 operations.
# 14 - 3 == 11 - 3 == 8 - 2 * 4 => 6 operations.
# 14 - 3 == 11 - 3 == 8 - 3 == 5 - 3 == 2 - 2 == 0 => 5 operations.
# So, the best way is to take ALL options of '3 equal' first and minimise '2 equal'.
# But, how? Like we can delete: 14 - 3 * 4 - 2 OR 14 - 2 - 3 * 4.
# For this case it seems correct, and other lower values too.
# Seems like we don't care when we're taking out '2 equal' operations.
# So, we can just take them first if we can't take '3 equal' from value, and then take all '3 equal'.
# But what about larger? Dunno about larger values, but because it's 'Greedy' it should be correct.
# Like it's always some straight logic with taking MAX options first.
# Let's just try with random() values and see.
# Works with 10+ random cases for max_constraints. Let's commit.


test: list[int] = [2, 3, 3, 2, 2, 4, 2, 3, 4]
test_out: int = 4
assert test_out == min_operations(test)

test = [2, 1, 2, 2, 3, 3]
test_out = -1
assert test_out == min_operations(test)

test = [randint(1, 10 ** 6) for _ in range(10 ** 5)]
print(test)
