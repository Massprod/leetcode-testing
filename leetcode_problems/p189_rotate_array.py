# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# --------------------
# 1 <= nums.length <= 105  ,  -231 <= nums[i] <= 231 - 1  ,  0 <= k <= 105
# --------------------
# Try to come up with as many solutions as you can.
# There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


def rotate1(nums: list[int], k: int) -> None:
    # working_time_limit O(k * n) | space: O(1)
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
    # working_sol (94.5%, 33.5%) -> (207ms, 27.9mb)  time: O(n) | space: O(1)
    k = k % len(nums)
    if k == 0:
        return
    nums[:] = nums[-k:] + nums[:-k]


# Time complexity: O(n) -> slicing one part, from k to [end] => O(k) ->
# n - length of input_list^^ -> from [0] to [k] => O(n - k) -> O(n - k) + O(k) => O(n)
# k - pivot point^^
# Space complexity: O(1) -> no extra space.
# --------------------
# ! This might be incorrect ^^. Because, reason why I even tried other solution's with switching indexes.
#   Wanted to make constant space, and because python_slice is taking
#   extra space to store a slice, we're not saving it but still.
#   @@Each slice operation basically amounts to a primitive O(n) copy operation.
#   Since only references are copied, the size or type of elements does not matter.
#   Space complexity is only O(n), since the temporary slices are reclaimable immediately.@@
#   ^^ this one reference to a creating list and then slicing it, but we're having list already.
#      so we're just referencing it.
#   @@In a nutshell, every list slicing operation involves making a copy
#   of the relevant object references (but not the objects themselves).@@
#   Ok. W.e I just doesn't want to start with binary trees and started this, as I already experienced with similar.
#   But failed with making solution for just *switching_indexes* without slicing or rebuilding.
#   Actually made one, but it's O(n*k) <- most simple way.
#   Maybe will just google to learn the way to do this without slicing, but this one might be correct for O(1).
#   !
# --------------------
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
# rotate1(test1, test1_k)
rotate2(test1, test1_k)
print(test1)
assert test1_out == test1

test2 = [-1, -100, 3, 99]
test2_k = 2
test2_out = [3, 99, -1, -100]
# rotate1(test2, test2_k)
rotate2(test2, test2_k)
print(test2)
assert test2_out == test2

test3 = [1, 2, 3]
test3_k = 2
test3_out = [2, 3, 1]
# rotate1(test3, test3_k)
rotate2(test3, 2)
print(test3)
assert test3_out == test3
