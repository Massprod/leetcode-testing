# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# --------------------
# 1 <= nums.length <= 105  ,  -231 <= nums[i] <= 231 - 1  ,  0 <= k <= 105
# --------------------
# Try to come up with as many solutions as you can.
# There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


def rotate1(nums: list[int], k: int) -> None:
    # working_time_limit O(k * n)
    k = k % len(nums)
    turn: int = 0
    while turn < k:
        prev: int = nums[turn]
        for x in range(turn + 1, len(nums)):
            nums[x], prev = prev, nums[x]
            if (x + 1) >= len(nums):
                nums[turn + (len(nums) - (x + 1))] = prev
        turn += 1
    point_1: int = 0
    point_2: int = k - 1
    while point_1 < point_2:
        nums[point_1], nums[point_2] = nums[point_2], nums[point_1]
        point_1 += 1
        point_2 -= 1


def rotate2(nums: list[int], k: int) -> None:
    k = k % len(nums)
    if k == 0:
        return
    nums[:] = nums[-k:] + nums[:-k]



#
# Was correct about slicing, but forget about reversing parts.
# This one is working. But I wanted to make working solution with switching indexes around k-point, and failed...
# In the end. 2 solutions, one working but time_limited -> one_by_one switch.
# Second simple slicing and merge.
# --------------------
# Done with trying to make this with switching indexes.
# --------------------
# Time limit, because I made one_by_one_solution.
# Just wanted to make it work after failing to turn indexes for k insta.
# But here's time limit for that.


test1 = [1, 2, 3, 4, 5, 6, 7]
test1_k = 3
test1_out = [5, 6, 7, 1, 2, 3, 4]
rotate1(test1, test1_k)
# rotate2(test1, test1_k)
print(test1)
assert test1_out == test1

test2 = [-1, -100, 3, 99]
test2_k = 2
test2_out = [3, 99, -1, -100]
rotate1(test2, test2_k)
# rotate2(test2, test2_k)
print(test2)
assert test2_out == test2

test3 = [1, 2, 3]
test3_k = 2
test3_out = [2, 3, 1]
rotate1(test3, test3_k)
# rotate2(test3, 2)
print(test3)
assert test3_out == test3
