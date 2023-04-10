# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


def three_sum(nums: list[int]) -> list[list[int]]:
    checked = []
    sums = []
    for x in range(len(nums)):
        first_slice = nums[:x] + nums[x + 1:]
        if nums[x] in checked:
            continue
        checked.append(nums[x])
        for y in range(len(first_slice)):
            second_slice = first_slice[:y] + first_slice[y + 1:]
            for z in range(len(second_slice)):
                if nums[x] + first_slice[y] + second_slice[z] == 0:
                    tempo = [nums[x], first_slice[y], second_slice[z]]
                    tempo.sort()
                    if tempo not in sums:
                        sums.append(tempo)
    return sums


test = [-1, 0, 1, 2, -1, -4]
# for g in range(len(test)):
#     print(test[g + 1:], test[:g])
#     print(test[g + 1:] + test[:g])
#     print("--------")
#     tes_slice = test[g + 1:] + test[:g]
#     for j in range(len(tes_slice)):
#         print(tes_slice[j +1:] + tes_slice[:j])
#         tes_slice2 = tes_slice[j + 1:] + tes_slice[:j]
#         # for k in range(len(tes_slice2)):
test1 = [-7, -4, -6, 6, 4, -6, -9, -10, -7, 5, 3, -1, -5, 8, -1, -2, -8, -1, 5, -3, -5, 4, 2, -5, -4, 4, 7]
test1_out = [[-10, 2, 8], [-10, 3, 7], [-10, 4, 6], [-10, 5, 5], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, 2, 6],
             [-8, 3, 5], [-8, 4, 4], [-7, -1, 8], [-7, 2, 5], [-7, 3, 4], [-6, -2, 8], [-6, -1, 7], [-6, 2, 4],
             [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 2, 3], [-4, -4, 8], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5],
             [-3, -2, 5], [-3, -1, 4], [-2, -1, 3], [-1, -1, 2]]

order = three_sum(test1)
order.sort()
print(order)
assert order == test1_out
for _ in three_sum(test1):
    assert _ in test1_out
# my solution is working, but they don't order correctly for Leetcode test.........
# NOPE i just missed [-1, -1, 2] HOW?>??
# OK I was trying to use string instead of a list, dunno why .
# cuz I was using string for 2 days and forgot about unique values, and used it for no reason.
# Because of that, there was 10 in string and obviously while checking IN string we got 1, 0 list it's neglected
# value of 1 for other X index...............nc
# No issue with sorting return value.
