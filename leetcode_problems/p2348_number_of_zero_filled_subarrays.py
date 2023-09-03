# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.
# ------------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 9 <= nums[i] <= 10 ** 9
from random import randint


def zero_filled_subs(nums: list[int]) -> int:
    # working_sol (86.67%, 63.42%) -> (904ms, 27mb)  time: O(n) | space: O(1)
    zeroes: int = 0
    subs: int = 0
    # ! For each zero, you can calculate the number of zero-filled subarrays
    #   that end on that index, which is the number of consecutive zeros
    #   behind the current element + 1 !
    for x in range(len(nums)):
        # Reset on other values.
        if nums[x] != 0:
            zeroes = 0
            continue
        subs += zeroes + 1
        zeroes += 1

    return subs


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 extra constant INTs used => O(1).
# ------------------
# New rule to know ->
# -> to count every possible sub_array we can build from same symbol sequence
#    we need to count number of consecutive elements +1 and store it on every index step,
#    until it's sequence didn't broke.
# Actually isn't this correct for any sequence?
# Like 'abc' -> same 6 options.
# So it's just count everything before some element and count for every index step, all_before + 1.
# And stop at something unusable.
# ------------------
# Well TLE without memo and MemoryLimit with memo, hmm.
# Guess there's some rule instead of checking subarrays.
# Hints:
# ! For each zero, you can calculate the number of zero-filled subarrays that end on that index,
#   which is the number of consecutive zeros behind the current element + 1 !
# So we just need all 0 before, and append subs on every brake?
# ! Maintain the number of consecutive zeros behind the current element,
#   count the number of zero-filled subarrays that end on each index, sum it up to get the answer. !


test: list[int] = [1, 3, 0, 0, 2, 0, 0, 4]
test_out: int = 6
assert test_out == zero_filled_subs(test)

test = [0, 0, 0, 2, 0, 0]
test_out = 9
assert test_out == zero_filled_subs(test)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 4)]
for _ in range(len(test)):
    if randint(1, 3) == 1:
        test[_] = 0
print(test)
