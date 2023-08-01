# You are given a 0-indexed array nums of n integers and an integer target.
# You are initially positioned at index 0. In one step,
#   you can jump from index i to any index j such that:
#       0 <= i < j < n
#       -target <= nums[j] - nums[i] <= target
# Return the maximum number of jumps you can make to reach index n - 1.
# If there is no way to reach index n - 1, return -1.
# ---------------
# 2 <= nums.length == n <= 1000
# -10 ** 9 <= nums[i] <= 10 ** 9
# 0 <= target <= 2 * 10 ** 9
from random import randint


def maximum_jumps(nums: list[int], target: int) -> int:
    # working_sol (96.30%, 90.91%) -> (765ms, 16.5mb)  time: O(n ** 2) | space: O(n)
    # All landing indexes, with starting position at [0]
    dp: list[int] = [0 for _ in range(len(nums))]
    # 0 <= i < j < n | used x == i, y == j
    # Y should be always higher, so we can't start from last_index.
    # Extra we need to land on last_index, and we can't jump on place.
    for x in range(len(nums) - 1):
        for y in range(x + 1, len(nums)):
            # X is start position to continue jumping sequence,
            # and we can't start from anything except nums[0].
            # ! You are initially positioned at index 0. !
            # ^^So if we can't jump from this and land correctly, we can't move at all.
            if dp[x] == 0 and x != 0:
                continue
            # If we continue jumping from any correct landing_point,
            # we still need to satisfy:
            if -target <= nums[y] - nums[x] <= target:
                # And choose maximum option already stored,
                # which equal to number of jumps taken to land here before,
                # and number of jumps from current start_point(i) + 1.
                # dp[x] -> start_point | dp[y] -> landing_point.
                dp[y] = max(dp[y], dp[x] + 1)
    # ! Return the maximum number of jumps you can make to reach index n - 1 !
    # ^^n == len(nums).
    # If nothing stored, then we didn't landed here even once.
    if dp[-1] == 0:
        return -1
    return dp[-1]


# Time complexity: O(n ** 2) -> creating dp with size of n => O(n) -> first_loop is going to be used for (n - 1) steps
# n - len of input_array^^| and extra nested loop with (n - x) steps => x is always changing and no idea how to calc
#                           it correctly, so I will just stick to classic n ** 2, for nested loops ->
#                           -> and in the worst case we're using (n - 1) for X loop and x == 0, so its (0 + 1, n) =>
#                           => same loops, it's at least once going to be ((n - 1) ** 2) -> ignoring -1 => O(n ** 2).
# Auxiliary space: O(n) -> creating only dp_array with size of n => O(n).
# ---------------
# Well rebuild of HINT is correct. And now at least I understand what task is.
# Similar to max_stair_jumps, but with extra requirements to meet.
# ---------------
# Ok. It's working, so basically we're just setting all indexes to 0, cuz there's no jumps done at first.
# Then we're checking if we can jump from some index == i, and we're skipping indexes i where value is still 0.
# Cuz it's mean there was no JUMP from some other index on THIS index, and we ALWAYS start from [0], otherwise
# it means we're going to start from this index, and we're not allowed to do this. So they're skipped.
# Everything else, is taking values from dp[i] and incrementing or just staying.
# Always jump from i and land on j, always choose maximum, cuz jump from i is +1, but j is already storing
# max jumps landed on this index.
# ---------------
# So we basically need dp_array with n size, and we need all indexes except last,
# cuz J can't be equal to n, and J is always higher than I -> we can't use last 2 indexes for I,
# and last index for J.
# ^^Ok. This incorrect ! 0 <= i < j < n ! They give this, but if I skip 2 last indexes for i, then
# it's incorrect if only 1 it's correct -> guess it's for zero indexed n == len(nums) not last index == len(nums) - 1.
# So i is limited to 0 -> len(nums) - 1, and j is always higher than i and lower than len(nums).
# And because j is always higher, we can't use last index for i.
# Standard DP is 0, cuz we didn't make any jumps. Everything else if from a HINT, and we're storing
# DP[i] for maximum_number of jumps, and our last index to jump on is [-1].
# So we need to return it, and -1 if there's 0.
# WTH this description ! If there is no way to reach index n - 1 ! <- why can't they use at least length,
# cuz n can be treated like just last index, not LENGTH itself. W.e just remember some n can be length not index.
# ---------------
# What the actual f... this description and task itself.
# It can't be a normal task, it some rebuild of something with restrictions to satisfy.
# Cuz they even provide solution in HINT.
# !
# Define a dynamic programming array dp of size n,
#   where dp[i] represents the maximum number of jumps from index 0 to index i. !
# !
# For each j iterate over all i < j.
#   Set dp[j] = max(dp[j], dp[i] + 1) if -target <= nums[j] - nums[i] <= target. !
# ^^I will just try to build from this HINT and understand.


test1 = [1, 3, 6, 4, 1, 2]
test1_target = 2
test1_out = 3
assert test1_out == maximum_jumps(test1, test1_target)

test2 = [1, 3, 6, 4, 1, 2]
test2_target = 3
test2_out = 5
assert test2_out == maximum_jumps(test2, test2_target)

test3 = [1, 3, 6, 4, 1, 2]
test3_target = 0
test3_out = -1
assert test3_out == maximum_jumps(test3, test3_target)

test: list[int] = []
for _ in range(100):
    test.append(randint(-10 ** 9, 10 ** 9))
test_target: int = randint(0, 2 * 10 ** 9)
# print(test)
# print(test_target)
