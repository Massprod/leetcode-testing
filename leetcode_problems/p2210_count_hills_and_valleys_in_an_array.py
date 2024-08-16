# You are given a 0-indexed integer array nums.
# An index i is part of a hill in nums if the closest non-equal neighbors of i
#  are smaller than nums[i].
# Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i
#  are larger than nums[i].
# Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].
# Note that for an index to be part of a hill or valley,
#  it must have a non-equal neighbor on both the left and right of the index.
# Return the number of hills and valleys in nums.
# ---------------------------
# 3 <= nums.length <= 100
# 1 <= nums[i] <= 100
from random import randint


def count_hill_valley(nums: list[int]) -> int:
    # working_sol (69.15%, 70.45%) -> (39ms, 16.50mb)  time: O(n) | space: O(n)
    unique_nums: list[int] = [nums[0]]
    for index in range(1, len(nums)):
        if nums[index] == unique_nums[-1]:
            continue
        unique_nums.append(nums[index])
    out: int = 0
    for index in range(1, len(unique_nums) - 1):
        if unique_nums[index - 1] < unique_nums[index] > unique_nums[index + 1]:
            out += 1
        elif unique_nums[index - 1] > unique_nums[index] < unique_nums[index + 1]:
            out += 1
    return out


test: list[int] = [2, 4, 1, 1, 6, 5]
test_out: int = 3
assert test_out == count_hill_valley(test)

test = [6, 6, 5, 5, 4, 1]
test_out = 0
assert test_out == count_hill_valley(test)

test = [randint(1, 100) for _ in range(100)]
print(test)
