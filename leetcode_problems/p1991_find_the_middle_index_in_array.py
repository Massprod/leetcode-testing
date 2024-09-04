# Given a 0-indexed integer array nums,
#  find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] +
#  + nums[middleIndex+2] + ... + nums[nums.length-1].
# If middleIndex == 0, the left side sum is considered to be 0.
# Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.
# Return the leftmost middleIndex that satisfies the condition,
#  or -1 if there is no such index.
# --------------------------
# 1 <= nums.length <= 100
# -1000 <= nums[i] <= 1000


def find_middle_index(nums: list[int]) -> int:
    # working_sol (52.78%, 34.36%) -> (43ms, 16.54mb)  time: O(n) | space: O(1)
    # Going from left -> right.
    # [0] start, prefix == 0 always.
    prefix: int = 0
    # Suffix for [0] sum() of everything else.
    suffix: int = sum(nums[1:])
    # Unique check for [0]
    if prefix == suffix:
        return 0
    for x in range(1, len(nums)):
        # Every step its increase of prefix,
        # and decrease of suffix.
        prefix += nums[x - 1]
        suffix -= nums[x]
        # Same check.
        # We can insta return, cuz left -> right.
        if prefix == suffix:
            return x
    return -1


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always using every index of `num`, twice => O(n).
# --------------------------
# Auxiliary space: O(1)
# Only two constant INTs used, none of them depends on input => O(1).


test: list[int] = [2, 3, -1, 8, 4]
test_out: int = 3
assert test_out == find_middle_index(test)

test = [1, -1, 4]
test_out = 2
assert test_out == find_middle_index(test)

test = [2, 5]
test_out = -1
assert test_out == find_middle_index(test)
