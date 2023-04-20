# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


def three_sum(nums: list[int]) -> list[list[int]] | set:
    # time_limit
    # checked_x = []
    # sums = []
    # nums.sort(reverse=True)
    # for x in range(len(nums)):
    #     first_slice = nums[:x] + nums[x + 1:]
    #     if nums[x] in checked_x:
    #         continue
    #     elif nums[x] < 0:
    #         continue
    #     checked_x.append(nums[x])
    #     for y in range(len(first_slice)):
    #         if first_slice[y] > 0:
    #             continue
    #         second_slice = first_slice[:y] + first_slice[y + 1:]
    #         to_find = (nums[x] + first_slice[y]) * -1
    #         for z in range(len(second_slice)):
    #             if second_slice[z] != to_find:
    #                 continue
    #             elif nums[x] + first_slice[y] + second_slice[z] == 0:
    #                 tempo = [nums[x], first_slice[y], second_slice[z]]
    #                 tempo.sort()
    #                 if tempo not in sums:
    #                     sums.append(tempo)
    # return sums
    # rebuild
    # working sol 19.44%, 93.98%
    nums.sort(reverse=True)
    sums = set()
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
            summ = nums[x] + nums[y] + nums[z]
            if summ == 0:
                to_add = tuple(sorted((nums[x], nums[y], nums[z])))
                sums.add(to_add)
                y += 1
                z -= 1
            elif summ > 0:
                y += 1
            elif summ < 0:
                z -= 1
    return sums

# I should have been used most_water_column from a start.
# Cuz after sorting nums we can already go from biggest to lowest values and skip all X which is already Used
# List[List[int]] - return for LeetCode as a Task, and I was trying to return list without using sets and filtered
# to_add values with IF. Ofc it's always TimeLimit with list's. After googling found return can be SET......


# --------------------------------------
# test = [-1, 0, 1, 2, -1, -4]
# print(three_sum(test))
# for g in range(len(test)):
#     print(test[g + 1:], test[:g])
#     print(test[g + 1:] + test[:g])
#     print("--------")
#     tes_slice = test[g + 1:] + test[:g]
#     for j in range(len(tes_slice)):
#         print(tes_slice[j +1:] + tes_slice[:j])
#         tes_slice2 = tes_slice[j + 1:] + tes_slice[:j]
# for k in range(len(tes_slice2)):
# test1 = [-7, -4, -6, 6, 4, -6, -9, -10, -7, 5, 3, -1, -5, 8, -1, -2, -8, -1, 5, -3, -5, 4, 2, -5, -4, 4, 7]
# test1_out = [[-10, 2, 8], [-10, 3, 7], [-10, 4, 6], [-10, 5, 5], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, 2, 6],
#              [-8, 3, 5], [-8, 4, 4], [-7, -1, 8], [-7, 2, 5], [-7, 3, 4], [-6, -2, 8], [-6, -1, 7], [-6, 2, 4],
#              [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 2, 3], [-4, -4, 8], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5],
#              [-3, -2, 5], [-3, -1, 4], [-2, -1, 3], [-1, -1, 2]]
#
# order = three_sum(test1)
# order.sort()
# assert order == test1_out
# for _ in three_sum(test1):
#     assert _ in test1_out
# my solution is working, but they don't order correctly for Leetcode test.........
# NOPE i just missed [-1, -1, 2] HOW?>??
# OK I was trying to use string instead of a list, dunno why .
# cuz I was using string for 2 days and forgot about unique values, and used it for no reason.
# Because of that, there was 10 in string and obviously while checking IN string we got 1, 0 list it's neglected
# value of 1 for other X index...............nc
# No issue with sorting return value.
# --------------------------------------------

def stolen_three_sums(nums: list[int]) -> set:
    # 97.68%, 14.89%
    sums = set()
    neg, pos, zero = [], [], []
    for _ in nums:
        if _ > 0:
            pos.append(_)
        elif _ < 0:
            neg.append(_)
        elif _ == 0:
            zero.append(_)
    NEG, POS = set(neg), set(pos)
    if zero:
        for num in POS:
            value = num * -1
            if value in NEG:
                sums.add((num * -1, 0, num))
    if len(zero) >= 3:
        sums.add((0, 0, 0))
    for x in range(len(pos)):
        for y in range(x + 1, len(pos)):
            check = (pos[x] + pos[y]) * -1
            if check in NEG:
                sums.add(tuple(sorted((pos[x], pos[y], check))))
    for x in range(len(neg)):
        for y in range(x + 1, len(neg)):
            check = (neg[x] + neg[y]) * -1
            if check in POS:
                sums.add(tuple(sorted((neg[x], neg[y], check))))
    return sums

# Good solution and I need to learn more to stop using simple looping and hit TimeLimits.
