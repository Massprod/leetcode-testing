# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.


def sum_closest(nums: list[int], target: int) -> int:
    # working sol 5.11%, 13.84%
    # nums.sort()
    # diffs = {}
    # checked = set()
    # max_x = len(nums) - 1
    # for x in range(len(nums)):
    #     y = 0
    #     z = len(nums) - 1
    #     if nums[x] in checked:
    #         continue
    #     elif x == max_x:
    #         y = 0
    #         z = x - 1
    #     elif x == 0:
    #         y = x + 1
    #         z = len(nums) - 1
    #     checked.add(nums[x])
    #     while y < z:
    #         if x == y:
    #             y += 1
    #             continue
    #         elif x == z:
    #             z -= 1
    #             continue
    #         three_sum = nums[x] + nums[y] + nums[z]
    #         if three_sum > 0:
    #             diff = target - three_sum
    #             if diff > 0:
    #                 y += 1
    #                 diffs[abs(diff)] = three_sum
    #             elif diff < 0:
    #                 z -= 1
    #                 diffs[abs(diff)] = three_sum
    #             elif diff == 0:
    #                 return three_sum
    #         elif three_sum < 0:
    #             diff = target - three_sum
    #             if diff > 0:
    #                 y += 1
    #                 diffs[abs(diff)] = three_sum
    #             elif diff < 0:
    #                 z -= 1
    #                 diffs[abs(diff)] = three_sum
    #             elif diff == 0:
    #                 return three_sum
    #         elif three_sum == 0:
    #             diff = 0 - target
    #             if diff > 0:
    #                 z -= 1
    #                 diffs[abs(diff)] = three_sum
    #             elif diff < 0:
    #                 y += 1
    #                 diffs[abs(diff)] = three_sum
    #             elif diff == 0:
    #                 return three_sum
    # min_diff = min(diffs.keys())
    # return diffs[min_diff]
    # second_try (6.3%, 50.75%) slow_afb
    nums.sort()
    diff = target - (nums[0] + nums[1] + nums[2])
    lowest = nums[0] + nums[1] + nums[2]
    checked = set()
    max_x = len(nums) - 1
    for x in range(len(nums)):
        y = 0
        z = len(nums) - 1
        if nums[x] in checked:
            continue
        elif x == max_x:
            y = 0
            z = x - 1
        elif x == 0:
            y = x + 1
            z = len(nums) - 1
        checked.add(nums[x])
        while y < z:
            if x == y:
                y += 1
                continue
            elif x == z:
                z -= 1
                continue
            three_sum = nums[x] + nums[y] + nums[z]
            tempo = target - three_sum
            if abs(tempo) < abs(diff):
                diff = tempo
                lowest = three_sum
            if three_sum < target:
                y += 1
            elif three_sum > target:
                z -= 1
            elif tempo == 0:
                return three_sum
    return lowest


test1 = [-1, 2, 1, -4]
test1_target = 1
test1_out = 2
print(sum_closest(test1, test1_target))
test2 = [0, 0, 0]
test2_target = 1
test2_out = 0
print(sum_closest(test2, test2_target))
test3 = [1, 1, 1, 0]
test3_target = 100
test3_out = 3
print(sum_closest(test3, test3_target))
# Not correct slicing, cuz of that I was skipping some values from left(y) side
test4 = [0, 1, 2]
test4_target = 0
test4_out = 3
print(sum_closest(test4, test4_target))
# Error because I left LOWEST as 0 and not first sum, and forgot about changing it later.
