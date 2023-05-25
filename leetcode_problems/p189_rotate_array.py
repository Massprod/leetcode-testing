# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# --------------------
# 1 <= nums.length <= 105  ,  -231 <= nums[i] <= 231 - 1  ,  0 <= k <= 105
# --------------------
# Try to come up with as many solutions as you can.
# There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)
    if k == 0:
        return
    if len(nums) % 2 != 0:
        prev: int = nums[k]
        nums[k] = nums[0]
        point_1: int = k + k
        if point_1 >= len(nums):
            point_1 = point_1 - len(nums)
        point_2: int = k + 1
        if point_2 >= len(nums):
            point_2 = point_2 - len(nums)
        point_3: int = 1
        if (len(nums) - k) < k:
            while point_3 < k:
                nums[point_1], nums[point_2] = nums[point_2], nums[point_1]
                nums[point_2], nums[point_3] = nums[point_3], nums[point_2]
                point_1 += 1
                if point_1 >= len(nums):
                    point_1 = point_1 - len(nums)
                point_2 += 1
                if point_2 >= len(nums):
                    point_2 = point_2 - len(nums)
                point_3 += 1
        if (len(nums) - k) > k:
            while point_3 < k:
                nums[point_1], nums[point_2] = nums[point_2], nums[point_1]
                nums[point_2], nums[point_3] = nums[point_3], nums[point_2]
                point_1 += 1
                if point_1 >= len(nums):
                    point_1 = point_1 - len(nums)
                point_2 += 1
                if point_2 >= len(nums):
                    point_2 = point_2 - len(nums)
                point_3 += 1
                if point_3 >= len(nums):
                    point_3 = point_3 - len(nums)
            for y in range(len(nums) - 1, point_2 - 1, -1):
                index: int = y + 1
                if index >= len(nums):
                    index = index - len(nums)
                nums[y], nums[index] = nums[index], nums[y]
        prev_index: int = k + k
        if prev_index >= len(nums):
            prev_index = prev_index - len(nums)
        nums[prev_index] = prev
        return
    if len(nums) % 2 == 0:
        for x in range(k):
            next_index: int = x + k
            if next_index >= len(nums):
                next_index = next_index - len(nums)
            nums[x], nums[next_index] = nums[next_index], nums[x]


# --------------------
# Time limit, because I made one_by_one_solution.
# Just wanted to make it work after failing to turn indexes for k insta.
# But here's time limit for that.
# --------------------
# Already done similar but with linked_list in p61.
# Three different ways:
#   1) We're just slicing at [:x + 1] and [x + 1:] and returning => [x + 1:] + [:x + 1] => O(2n)
#      ^^not in place solution, but there's no mentioning three in_place solutions.
#   2) Same solution as 1 but, we're recreating new list from indexes not slices, not actually a different one.
#   3) Changing every index 1 by 1 for k times, in_place. But it will be O(k * n),
#      because we're only rotating by one at a time.
#      ^^did this in p61, if I recall correctly.
#   3+) 99% sure we can rotate every index by k in one walk, but how?


test1 = [1, 2, 3, 4, 5, 6, 7]
test1_k = 3
test1_out = [5, 6, 7, 1, 2, 3, 4]
rotate(test1, test1_k)
print(test1)
assert test1_out == test1


test2 = [-1, -100, 3, 99]
# test2_k = 2
# test2_out = [3, 99, -1, -100]
# rotate(test2, test2_k)
# print(test2)
# assert test2_out == test2

test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
rotate(test3, 3)
print(test3)
