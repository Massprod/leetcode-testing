# You are given a 0-indexed integer array nums.
# You have to partition the array into one or more contiguous subarrays.
# We call a partition of the array valid if each of the obtained subarrays
#   satisfies one of the following conditions:
#  -The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
#  -The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
#  -The subarray consists of exactly 3 consecutive increasing elements, that is,
#    the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good,
#    but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.
# ---------------------
# 2 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 6
from random import randint


def valid_partition(nums: list[int]) -> bool:
    # working_sol (57.69%, 26.92%) -> (1047ms, 103.96mb)  time: O(3 * (3 ** n) | space: O(3 ** n)
    # Standard cache.
    recur_cache: dict[int, bool] = {}

    def check(index: int) -> bool:
        # If we ever come out from indexes, then
        # every call done before this is correct sequence.
        # So it's only return of True.
        # And there's at least one valid partition.
        if index >= len(nums):
            return True
        # Reuse stored.
        if index in recur_cache:
            return recur_cache[index]
        # Count correct values in sequence.
        count: int = 1
        # ! Can be changed for just nums[x + 1] == nums[index],
        #   but I want it to look symmetrical, and it's same 1 index check anyway. !
        # Checking all 3 options:
        # ! The subarray consists of exactly 2 equal elements. !
        for x in range(index + 1, index + 2):
            if x < len(nums):
                if nums[x] == nums[index]:
                    count += 1
                    if count == 2:
                        # Correct sequence, recall with +2 from original index.
                        # Skipping sequence == 2 values.
                        if check(index + 2):
                            # Cache result.
                            recur_cache[index] = True
                            return True
        count = 1
        # ! The subarray consists of exactly 3 equal elements. !
        for x in range(index + 1, index + 3):
            if x < len(nums):
                if nums[x] == nums[index]:
                    count += 1
                    if count == 3:
                        # Same, but with +3 cuz it's sequence == 3 values.
                        if check(index + 3):
                            recur_cache[index] = True
                            return True
        count = 1
        current_index: int = index
        # ! The subarray consists of exactly 3 consecutive increasing elements !
        for x in range(index + 1, index + 3):
            if x < len(nums):
                # Standard check with resetting of current_index.
                if (nums[x] - nums[current_index]) == 1:
                    count += 1
                    current_index = x
                    if count == 3:
                        # Same.
                        if check(index + 3):
                            recur_cache[index] = True
                            return True
        # Cache result.
        recur_cache[index] = False
        return recur_cache[index]

    return check(0)


# Time complexity: O(2 * (3 ** n)) -> recursion with maximum depth of n and for every call we're using 3 loops with
# n - len of input_array^^|         2 indexes checked => O(2 * (3 ** n)) -> with memorization it can be even,
#                                   O(n) in case if every subarray is correct repeat of 2 values, no idea how to calc
#                                   it more correctly, so sticking to maximum with O(2 * (3 ** n)) <- loops + recursion.
#                                   Totally need to find some info, how to calculate caching correctly.
#                                   But there's None so far :(
# Auxiliary space: O(3 ** n) -> storing most of the calls into cache dictionary => O(3 ** n).
# ---------------------
# Ok. It's working and not even with worst results. Best solutions is 750ms, mine is 1040 -> Fine for me.
# But I will search DP bottom_top later.
# ---------------------
# Recursion with cache, a.k.a top-down dp. But might be TLE for max_constraints. Let's test.
# Otherwise, it's some DP array with memorization I don't see it for now.
# Ok. 10 ** 3 is already maximum_depth for recursion. What to cull?
# Hmm. But it's working on leet, guess they removed limit.
# Well I don't have any idea about tricky parts in test_cases, so it's better to just Fail and see.
# Because locally I need to extra remove recursion_limit to test, and it's already working for max_constraints
# on leet itself.


test: list[int] = [4, 4, 4, 5, 6]
test_out: bool = True
assert test_out == valid_partition(test)

test = [1, 1, 1, 2]
test_out = False
assert test_out == valid_partition(test)

test = []
# Remove some of the last indexes,
# for test False result with maximum depth.
for _ in range((10 ** 5) // 3):
    value: int = randint(1, 10 ** 6)
    choice: int = randint(1, 2)
    if choice == 1:
        for _ in range(2):
            test.append(value)
        continue
    for _ in range(3):
        test.append(value)
# print(test)
