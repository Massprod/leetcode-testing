# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.
# ---------------
# 1 <= nums.length <= 5 * 10 ** 5
# -2 ** 31 <= nums[i] <= 2 ** 31 - 1
# ---------------
# Follow up:
# Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
from random import randint


def increasing_triplet(nums: list[int]) -> bool:
    # working_sol (23.92%, 67.96%) -> (1096ms, 32.5mb)  time: O(n) | space: O(n)
    # No Triplet possible.
    if len(nums) < 3:
        return False
    right_limits: list[int] = [0 for _ in nums]
    # Last element we can use to build with.
    right_max: int = nums[-1]
    # Record every max_value we can use for every index.
    for x in range(len(nums) - 2, -1, -1):
        right_limits[x] = right_max
        right_max = max(right_max, nums[x])
    # [0] most left index, we can use it as possible minimum.
    left_min: int = nums[0]
    # Check every index for being in range ->
    for y in range(1, len(nums)):
        if left_min < nums[y] < right_limits[y]:
            return True
        # -> if something smaller met, we can update min_value.
        # Cuz going from left -> right, we will only meet correct triplets
        # with this value as minimum later.
        left_min = min(nums[y], left_min)
    return False


# Origin.
# Time complexity: O(n) -> creating array of size n => O(n) -> calc all right_max for every index => O(n - 1) ->
# n - len of input_array^^| -> extra traverse to find value in from left_min to right_max, not inclusive => O(n).
# Auxiliary space: O(n) -> extra list with same size as input_array => O(n).


def increasing_triple_follow(nums: list[int]) -> bool:
    # working_sol (98.93%, 67.96%) -> (871ms, 32.4mb)  time: O(n) | space: O(1)
    first_m: int | float = float('inf')
    second_m: int | float = float('inf')
    for num in nums:
        # Update first_marker if something smaller met ->
        if num < first_m:
            first_m = num
        # -> update second_marker if something in range met ->
        elif first_m < num <= second_m:
            second_m = num
        # -> correct Triplet if something bigger met.
        elif num > second_m:
            return True
    return False


# Follow up.
# Time complexity: O(n) -> traversing input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 extra constants used => O(1).
# ---------------
# Ok. It's working correctly, but time => O(3n) and space: O(n) (20.18, 68).
# Time to learn follow up:
#   We can just use 3 markers and change them ->
#   - if met something smaller than first_marker update it.
#   - if met something in from first_marker to second_marker(inclusive) update second.
#   - if met something bigger than second_marker, return True.
# Actually not so much of a diff mine is (1118ms) -> (908ms). But space is constant now.
# ---------------
# Ok. Window seems working, always maintaining range(left_l, right_l) not inclusive.
# And if we find anything in this range return True, if not then there's no correct triplet.
# And range is always only EXPANDING, cuz left_l is changing only for lower values and right_l
# for higher values. Allowing us to expand range and still check every index one by one.
# Incorrect, im always changing indexes one by one, and it could miss some values like =>
# [4, 5, 2147483647, 1, 2] <- 5 will be checked before 214474... found and set.
# If I stop counting left side? Then how would I come into 1 correctly?
# Saving right|left sides? Like save every index right_maximum we can find on this side.
# And check left side for min_value and index by index min_value < index_value < right_maximum.
# Same reset for left side, if we met something smaller.
# Extra ignore [0] and [-1] cuz they don't have left and right sides respectively.


test: list[int] = [1, 2, 3, 4, 5]
test_out: bool = True
assert test_out == increasing_triplet(test)
assert test_out == increasing_triple_follow(test)

test = [5, 4, 3, 2, 1]
test_out = False
assert test_out == increasing_triplet(test)
assert test_out == increasing_triple_follow(test)

test = [2, 1, 5, 0, 4, 6]
test_out = True
assert test_out == increasing_triplet(test)
assert test_out == increasing_triple_follow(test)

test = [0, 0, 0, 0, 0, 0]
test_out = False
assert test_out == increasing_triplet(test)
assert test_out == increasing_triple_follow(test)

test = [4, 5, 2147483647, 1, 2]
test_out = True
assert test_out == increasing_triplet(test)
assert test_out == increasing_triple_follow(test)

test = [5, 4, 1, 2, 3]
test_out = True
assert test_out == increasing_triplet(test)
assert test_out == increasing_triple_follow(test)

test = []
for _ in range(5 * 10 ** 4):
    test.append(randint(-2 ** 31, 2 ** 31 - 1))
# print(test)
