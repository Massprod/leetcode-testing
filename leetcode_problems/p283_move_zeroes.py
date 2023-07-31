# Given an integer array nums, move all 0's to the end of it while
#   maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# -------------
# 1 <= nums.length <= 10 ** 4
# -2 ** 31 <= nums[i] <= 2 ** 31 - 1
from random import randint, choice


def move_zeroes(nums: list[int]) -> None:
    # working_sol (99.90%, 52.33%) -> (132ms, 17.9mb)  time: O(n) | space: O(1)
    # Step we need to take from current_index to 0.
    step: int = 0
    for x in range(len(nums)):
        # Incrementing step for every 0 we met.
        if nums[x] == 0:
            step += 1
            continue
        # Step is equal of distance from current_index to 0,
        # so we're just switching them.
        nums[x - step], nums[x] = nums[x], nums[x - step]


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 1 extra constant created and just switching index_values in_place => O(1).
# -------------
# Record step and switch everything except 0 for this step and increment step by every 0 met?
# Should be working.
# Follow up: Could you minimize the total number of operations done?
# Dunno I'm already just switching every value once.


test1 = [0, 1, 0, 3, 12]
test1_out = [1, 3, 12, 0, 0]
move_zeroes(test1)
assert test1_out == test1

test2 = [0]
test2_out = [0]
move_zeroes(test2)
assert test2_out == test2

test: list[int] = []
for _ in range(10 ** 4):
    test.append(choice([randint(-2 ** 31, 2 ** 31 - 1), 0]))
print(test)
