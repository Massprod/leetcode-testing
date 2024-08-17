# You are given a 0-indexed array nums of length n containing distinct positive integers.
# Return the minimum number of right shifts required to sort nums and -1 if this is not possible.
# A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.
# -----------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# nums contains distinct integers.
from random import randint


def minimum_right_shifts(nums: list[int]) -> int:
    # working_sol (75.20%, 41.95%) -> (45ms, 16.59mb)  time: O(n) | space: O(1)
    if len(nums) == 1:
        return 0
    prev_max: int = nums[-1]
    break_reached: int = -1
    for index in range(len(nums) - 1, -1, -1):
        if nums[index] >= nums[index - 1]:
            continue
        if -1 == break_reached:
            break_reached = index
            if prev_max > nums[index - 1]:
                return -1
        else:
            return -1
    if 0 == break_reached:
        return break_reached
    return len(nums) - break_reached


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# -----------------------
# Auxiliary space: O(1).


test: list[int] = [3, 4, 5, 1, 2]
test_out: int = 2
assert test_out == minimum_right_shifts(test)

test = [1, 3, 5]
test_out = 0
assert test_out == minimum_right_shifts(test)

test = [2, 1, 4]
test_out = -1
assert test_out == minimum_right_shifts(test)

test = sorted(set([randint(1, 100) for _ in range(100)]))
pivot: int = randint(0, len(test) - 1)
shuffled: list[int] = test[pivot:] + test[0:pivot]
print(shuffled)
