# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


def three_sum(nums: list[int]) -> list[list[int]]:
    checked = ""
    sums = []
    for x in range(len(nums)):
        first_slice = nums[x + 1:] + nums[:x]
        if str(x) in checked:
            continue
        checked += str(nums[x])
        for y in range(len(first_slice)):
            second_slice = first_slice[y + 1:] + first_slice[:y]
            for z in range(len(second_slice)):
                if nums[x] + nums[y] + nums[z] == 0:
                    sums.append([nums[x], nums[y], nums[z]])
                    break
    return sums


test = [-1, 0, 1, 2, -1, -4]
print(three_sum(test))
# for g in range(len(test)):
#     print(test[g + 1:], test[:g])
#     print(test[g + 1:] + test[:g])
#     print("--------")
#     tes_slice = test[g + 1:] + test[:g]
#     for j in range(len(tes_slice)):
#         print(tes_slice[j +1:] + tes_slice[:j])
#         tes_slice2 = tes_slice[j + 1:] + tes_slice[:j]
#         # for k in range(len(tes_slice2)):
