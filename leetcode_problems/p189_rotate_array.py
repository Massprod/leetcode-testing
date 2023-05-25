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
    for x in range(k):
        next_index: int = x + k
        if next_index >= len(nums):
            next_index = next_index - len(nums)
        prev: int = nums[next_index]
        nums[x], nums[next_index] = nums[next_index], nums[x]
        step_index: int = next_index + k
        if step_index >= len(nums):
            step_index = step_index - len(nums)
        while step_index <= x:
            nums[step_index], prev = prev, nums[step_index]
            step_index += k
            if step_index >= len(nums):
                step_index = step_index - len(nums)
        nums[x] = prev

# Done with trying to make this with switching indexes.
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


# test1 = [1, 2, 3, 4, 5, 6, 7]
# test1_k = 3
# test1_out = [5, 6, 7, 1, 2, 3, 4]
# rotate(test1, test1_k)
# print(test1)
# assert test1_out == test1


# test2 = [-1, -100, 3, 99]
# test2_k = 2
# test2_out = [3, 99, -1, -100]
# rotate(test2, test2_k)
# print(test2)
# assert test2_out == test2

test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotate(test3, 4)
print(test3)
