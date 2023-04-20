# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

def quad_sum(nums: list[int], target: int) -> list[list[int]] | set:
    # working_sol (7.96%, 86.34%)
    all_sums = []

    def three_recur(sliced: list[int], rema: int):
        sums = []
        checked = set()
        max_x = len(sliced) - 1
        for x in range(len(sliced)):
            y = 0
            z = len(sliced) - 1
            if sliced[x] in checked:
                continue
            elif x == max_x:
                y = 0
                z = x - 1
            elif x == 0:
                y = x + 1
                z = len(sliced) - 1
            checked.add(sliced[x])
            while y < z:
                if x == y:
                    y += 1
                    continue
                elif x == z:
                    z -= 1
                    continue
                summ = sliced[x] + sliced[y] + sliced[z]
                if summ == rema:
                    to_add = [sliced[x], sliced[y], sliced[z]]
                    to_add.sort()
                    if to_add not in sums:
                        sums.append(to_add)
                    y += 1
                    z -= 1
                elif summ - rema > 0:
                    y += 1
                elif summ - rema < 0:
                    z -= 1
        return sums

    nums.sort(reverse=True)
    for g in range(len(nums) - 3):  # there's always len-3 slice and all values in it will be summed
        if g == 0 or nums[g] != nums[g - 1]:  # skip duplicates
            tempo = three_recur(nums[g + 1:], target - nums[g])  # recall
            for _ in tempo:
                _.append(nums[g])
                all_sums.append(_)
    return all_sums


# W.e I guessed is failed miserably and as always with 2+ loops I needed to use recursion.
# For the 3-rd recursion task in life is a bit hard, but doable. Need to do more of these.


test1 = [1, 0, -1, 0, -2, 2]
test1_target = 0
test1_out = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(quad_sum(test1, test1_target))
test2 = [-3, -1, 0, 2, 4, 5]
test2_target = 0
test2_out = [[-3, -1, 0, 4]]
print(quad_sum(test2, test2_target))
test3 = [-3, -2, -1, 0, 0, 1, 2, 3]
test3_target = 0
test3_out = [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2],
             [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(quad_sum(test3, test3_target))
for tes in test3_out:
    tes_list = list(quad_sum(test3, test3_target))
    assert tes in tes_list
