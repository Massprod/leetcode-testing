# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

def quad_sum(nums: list[int], target: int) -> list[list[int]] | set:
    nums.sort()
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
        while y < (z - 1):
            if x == y:
                y += 1
            elif x == z:
                z -= 1
            for g in range(y + 1, z):
                if x == g:
                    continue
                summ = nums[x] + nums[y] + nums[z] + nums[g]
                print(x, y, g, z)
                if summ == target:
                    to_add = tuple(sorted((nums[x], nums[y], nums[z], nums[g])))
                    sums.add(to_add)
                    y += 1
                    z -= 1
            y += 1
    return sums


# Guess it's same as 3_sum but with another num?? Try.
test1 = [1, 0, -1, 0, -2, 2]
test1_target = 0
test1_out = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
# print(quad_sum(test1, test1_target))
test2 = [-3, -1, 0, 2, 4, 5]
test2_target = 0
test2_out = [[-3, -1, 0, 4]]
print(quad_sum(test2, test2_target))