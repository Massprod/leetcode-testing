# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
#   and it will automatically contact the police if two adjacent houses
#   were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
#   return the maximum amount of money you can rob tonight without alerting the police.
# -----------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
from random import randint


def rob(nums: list[int]) -> int:
    # working_sol (95.96%, 44.70%) -> (38ms, 16.3mb)  time: O(n) | space: O(n)
    first_path: list[int] = nums
    second_path: list[int] = nums.copy()
    # First path IGNORES first house and counting
    # everything else as standard I version of the task
    for x in range(3, len(first_path)):
        f_option: int = first_path[x - 2]
        s_option: int = 0
        # ignoring first 3 houses, for correct pathing
        if x > 3:
            s_option = first_path[x - 3]
        # first is best
        if f_option > s_option:
            first_path[x] = f_option + first_path[x]
            continue
        # second is best
        if s_option > f_option:
            first_path[x] = s_option + first_path[x]
            continue
        # equal
        first_path[x] = s_option + first_path[x]
    # Second path IGNORES last house and counting
    # everything else as before
    for x in range(2, len(second_path) - 1):
        f_option = second_path[x - 2]
        s_option = 0
        # ignoring first 2, for correct pathing
        if x > 2:
            s_option = second_path[x - 3]
        if f_option > s_option:
            second_path[x] = f_option + second_path[x]
            continue
        if s_option > f_option:
            second_path[x] = s_option + second_path[x]
            continue
        second_path[x] = s_option + second_path[x]
    # There's always 2 maximized ends of the paths in the end.
    # For the First it's [-1], [-2] -> because we can include last_house
    # Second path can't include last_house, so it's -1 from basic case [-2], [-3]
    if len(nums) > 2:
        # standard case
        return max(first_path[-1], first_path[-2], second_path[-2], second_path[-3])
    if len(nums) == 2:
        # case when we're having nums of len == 2, then our second path
        # have only 1 end option, cuz there's no [-3] house at all.
        return max(first_path[-1], first_path[-2], second_path[-2])
    # case with 1 house
    return nums[-1]


# Time complexity: O(n) -> traversing (n - 3) indexes to calculate correct end_points for the First/Second paths =>
# n - len of input_array^^| => O(n - 3) + O(n - 3) => O(2 * (n - 3)) => O(n).
# Auxiliary space: O(n) -> creating one copy of the input_array, and 2 extra INTs used => O(n).
# -----------------------
# Failed to see that there's 2 end_points on BOTH paths, and case with len(nums) == 2 -> we don't have [-3] at all.
# Well, at least everything else is correct.
# And we actually need only 1 copy of the nums, and just use original as First to save space.
# -----------------------
# Ok. Same as p198, but now I need to consider circled paths.
# Actually it should be working as it is.
# Just how we can ignore border_cases with last and first houses?
# Like if we start from 0(first) house, we can't end on last, but summarized path is still should be correct
# we just need to exclude it. Calculate whole path, and subtract last house value?
# But how we can know that we started from first_house in that case?
# Even if I make some bool to check it, there's second path we can take which is allowed to end on last_house.
# And if we count everything starting from first_house, after we subtract last_house we're not getting
# correct summ. Because we could have started from second house in that case path could be different.
# Guess it's better to calculate 2 paths and choose between them.
# First -> starting from 1, 2 houses and continue till the last_house.
# Second -> starting from 0, 1 houses and continue till the pre_last_house.
# Like its doubles our time, but I don't see other solution for now.


test1 = [2, 3, 2]
test1_out = 3
assert test1_out == rob(test1)

test2 = [1, 2, 3, 1]
test2_out = 4
assert test2_out == rob(test2)

test3 = [1, 2, 3]
test3_out = 3
assert test3_out == rob(test3)

test4 = [1, 2, 3, 4, 5]
test4_out = 8
assert test4_out == rob(test4)

# test5 -> failed -> failed, because in both paths, we have 2 endpoints to consider and I didn't see it.
test5 = [200, 3, 140, 20, 10]
test5_out = 340
assert test5_out == rob(test5)

# test6 -> failed -> unique case in which second_path will have only [-2] endpoint.
test6 = [0, 0]
test6_out = 0
assert test6_out == rob(test6)

# testing with leetcode testcases, all correct
test = []
for _ in range(100):
    test.append(randint(0, 1000))
print(test)
print(rob(test))
