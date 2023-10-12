# (This problem is an interactive problem.)
# You may recall that an array arr is a mountain array if and only if:
#   arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
#   arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#   arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
# If such an index does not exist, return -1.
# You cannot access the mountain array directly.
# You may only access the array using a MountainArray interface:
#   MountainArray.get(k) returns the element of the array at index k (0-indexed).
#   MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
# Also, any solutions that attempt to circumvent the judge will result in disqualification.
# --------------------
# 3 <= mountain_arr.length() <= 10 ** 4
# 0 <= target <= 10 ** 9
# 0 <= mountain_arr.get(index) <= 10 ** 9
from random import randint


class MountainArray:

    def __init__(self, array: list[int]):
        self.mountain: list[int] = array
        self.count: int = 0

    def get(self, index: int) -> int:
        # Assume we don't make Index error :)
        if self.count >= 100:
            raise Exception(f'Count limit: {self.count}')
        self.count += 1
        return self.mountain[index]

    def length(self) -> int:
        return len(self.mountain)


def find_in_mountain(target: int, mountain_arr: MountainArray) -> int:
    # working_sol (70.8%, 60%) -> (37ms, 17.1mb)  time: O(log n) | space: O(1)
    # We can't have duplicates after each other,
    #  but we can have them on different sides.
    peak: int = -1
    left: int = 0
    right: int = mountain_arr.length() - 1
    min1: int = mountain_arr.get(left)
    min2: int = mountain_arr.get(right)
    right_side: bool = True
    left_side: bool = True
    # Target is lower than 2 minimums == can't be present.
    if min1 > target and min2 > target:
        return -1
    # We can return only MOST left, otherwise it can be duplicate.
    elif min1 == target:
        return left
    # Can't be on the left side.
    elif min1 > target:
        left_side = False
    # Can't be on the right side.
    elif min2 > target:
        right_side = False
    # First we need index of a peak value.
    # We can only make 100 calls, so minimise it.
    while left < right:
        middle: int = (left + right) // 2
        mid_val: int = mountain_arr.get(middle)
        # Something higher exist -> shift to right.
        if mid_val < mountain_arr.get(middle + 1):
            left = middle + 1
            continue
        # Nothing higher on right side, and left side == peak.
        elif mid_val > mountain_arr.get(middle - 1):
            peak = middle
            if mid_val == target:
                return peak
            # There's no value higher than peak.
            if mid_val < target:
                return -1
            break
        # Something higher on left side -> shift to left.
        right = middle
    # We need minimum index, so it's left_side check first.
    if left_side:
        left = 0
        right = peak - 1
        # Left side == ascending.
        while left < right:
            middle = (left + right) // 2
            mid_val = mountain_arr.get(middle)
            if mid_val == target:
                return middle
            elif mid_val < target:
                left = middle + 1
                continue
            right = middle
        if mountain_arr.get(left) == target:
            return left
    # Right side == descending.
    if right_side:
        left = peak + 1
        right = mountain_arr.length() - 1
        while left < right:
            middle = (left + right) // 2
            mid_val = mountain_arr.get(middle)
            if mid_val == target:
                return middle
            elif mid_val > target:
                left = middle + 1
                continue
            right = middle
        if mountain_arr.get(left) == target:
            return left
    return -1


# Time complexity: O(log n) -> we always search for a peak => O(log n) -> only after this we will check sides ->
# n - len of array stored in 'MountainArray'^^| -> sides can be halves or lower, essentially its extra search of 'n' ->
#                           -> so it should be correct to say O(2 * log n), anyway peak search will dominate them.
# Auxiliary space: O(1) -> only extra constant INTs used, none of them depends on input => O(1).
# --------------------
# Tag is BS, and hint is to use BS to get peak and find target on left or right side.
# We need most LEFT index, so it's always starting from left side.
# Only question is can we have duplicates?
# No, tested with [1, 1, 2, 1, 1] <- incorrect test case.
# But we can have duplicates on different sides => [1, 2, 1] <- is correct.
# Let's try to build and see, cuz limit of 100 calls is only questionable part.


test: MountainArray = MountainArray([1, 2, 3, 4, 5, 3, 1])
test_target: int = 3
test_out: int = 2
assert test_out == find_in_mountain(test_target, test)

test = MountainArray([0, 1, 2, 4, 2, 1])
test_target = 3
test_out = -1
assert test_out == find_in_mountain(test_target, test)

test_t: list[int] = (sorted([randint(0, 10 ** 5) for _ in range(10 ** 2)])
                     + sorted([randint(10 ** 5 + 1, 10 ** 9) for _ in range(10 ** 2)], reverse=True))
print(test_t)
