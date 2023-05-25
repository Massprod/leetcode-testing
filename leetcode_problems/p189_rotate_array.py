# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# --------------------
# 1 <= nums.length <= 105  ,  -231 <= nums[i] <= 231 - 1  ,  0 <= k <= 105
# --------------------
# Try to come up with as many solutions as you can.
# There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


def rotate(nums: list[int], k: int) -> None:
    pass


#
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

test2 = [-1, -100, 3, 99]
test2_k = 2
test2_out = [3, 99, -1, -100]
