# You are given a binary array nums.
# You can do the following operation on the array any number of times (possibly zero):
#  - Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.
# Return the minimum number of operations required to make all elements in nums
#  equal to 1. If it is impossible, return -1.
# -------------------------
# 3 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 1


def min_operations(nums: list[int]) -> int:
    # working_sol (59.38%, 89.20%) -> (109ms, 21.59mb)  time: O(n) | space: O(1)
    out: int = 0
    # We can't skip `0` => convert it instantly.
    # And we can't convert size 3 subarray into all `1`,
    #  if there's not all `0`s.
    # Essentially we always convert by size 3 arrays,
    #  so we still need to:
    # Start from all indexes and convert it to `1`.
    for index in range(2, len(nums)):
        # Already `1`
        if nums[index - 2]:
            continue
        # Flip to get `1`
        nums[index - 2], nums[index - 1], nums[index] = (
            nums[index - 2] ^ 1, nums[index - 1] ^ 1, nums[index] ^ 1
        )
        out += 1
    if sum(nums) != len(nums):
        return -1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Traversing every index of `nums`, once to convert all 3 sized => O(n).
# Extra using every value to get `sum(nums)` => O(2 * n).
# -------------------------
# Auxiliary space: O(1)


test: list[int] = [0, 1, 1, 1, 0, 0]
test_out: int = 3
assert test_out == min_operations(test)

test = [0, 1, 1, 1]
test_out = -1
assert test_out == min_operations(test)
