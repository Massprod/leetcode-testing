# You are given a binary array nums (0-indexed).
# We define xi as the number whose binary representation is the subarray nums[0..i]
#  (from most-significant-bit to least-significant-bit).
# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
# -----------------------
# 1 <= nums.length <= 10 ** 5
# nums[i] is either 0 or 1.
from random import choice


def prefix_div_5(nums: list[int | bool]) -> list[bool]:
    # working_sol (59.39%, 97.19%) -> (207ms, 17.16mb)  time: O(n) | space: O(1)
    cur_bin: int = 0
    for x in range(len(nums)):
        # left_shift -> delete MSB if exceeds, place 0 as LSB
        # Instead of using string, we can just shift and place 1 or 0 as LSB.
        cur_bin = (cur_bin << 1) + nums[x]
        if cur_bin % 5 == 0:
            nums[x] = True
        else:
            nums[x] = False
    return nums


# Time complexity: O(n) -> traversing whole input_array, once => O(n)
# n - len of input_array^^|
# Auxiliary space: O(1) -> reusing input array, and One extra constant INT used => O(1).


test: list[int] = [0, 1, 1]
test_out: list[bool] = [True, False, False]
assert test_out == prefix_div_5(test)

test = [1, 1, 1]
test_out = [False, False, False]
assert test_out == prefix_div_5(test)

test = [choice([1, 0]) for _ in range(10 ** 3)]
print(test)
