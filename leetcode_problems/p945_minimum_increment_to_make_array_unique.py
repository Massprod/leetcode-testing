# You are given an integer array nums.
# In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
# The test cases are generated so that the answer fits in a 32-bit integer.
# ----------------------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 10 ** 5
from random import randint
from collections import Counter


def min_increment_for_unique(nums: list[int]) -> int:
    # working_sol (52.03%, 57.43%) -> (647ms, 30.55mb)  time: O(n * log n) | space: O(n)
    # Basically, we could start from any value and just increment it by 1 for every collision.
    # But it's slow af.
    # Better to `sort` and use differences between adjusted elements.
    nums.sort()
    out: int = 0
    for index in range(1, len(nums)):
        # We can be sure that everything on the left side is lower and unique.
        # And it's already adjusted for maximum unique value on a previous element.
        # So, we always need to increment this value by difference and add +1 later.
        if nums[index] < nums[index - 1]:
            out += abs(nums[index] - nums[index - 1])
            nums[index] = nums[index - 1]
        # We guarantee that everything on the left side is lower and unique.
        # So, we can just increment it by 1 to make it a new unique so far.
        if nums[index] == nums[index - 1]:
            nums[index] = nums[index - 1] + 1
            out += 1
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting the array `nums` with basic `sort` => O(n * log n).
# Also single traverse of the whole array `nums` to get number of moves => O(n).
# ----------------------------
# Auxiliary space: O(n)
# Basic `sort` takes O(n) + one constant INT => O(n)


test: list[int] = [1, 2, 2]
test_out: int = 1
assert test_out == min_increment_for_unique(test)

test = [3, 2, 1, 2, 1, 7]
test_out = 6
assert test_out == min_increment_for_unique(test)

test = [randint(0, 10 ** 5) for _ in range(10 ** 5)]
print(test)
