# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j].
# The width of such a ramp is j - i.
# Given an integer array nums, return the maximum width of a ramp in nums.
# If there is no ramp in nums, return 0.
# ----------------------
# 2 <= nums.length <= 5 * 10 ** 4
# 0 <= nums[i] <= 5 * 10 ** 4


def max_width_ramp(nums: list[int]) -> int:
    # working_sol (43.46%, 56.38%) -> (354ms, 23.62mb)  time: O(n) | space: O(n)
    stack: list[int] = [0]
    # [0, 1, 2, 3]
    # If we already have `0` placed, we don't care about higher values.
    # Because they will give less ramp than our index if `0`.
    for index in range(1, len(nums)):
        if nums[index] < nums[stack[-1]]:
            stack.append(index)
    out: int = 0
    # Now we can just go in reverse and take distance for every value that is lower than our current.
    # And we can guarantee that this `stack` values is going to be the lowest on the left side.
    for index in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[index]:
            out = max(out, index - stack[-1])
            stack.pop()
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing input array `nums`, twice => O(2 * n).
# ----------------------
# Auxiliary space: O(n)
# In the worst case input array `nums` in descending order.
# `stack` <- allocates space for each value from `nums` => O(n).


test: list[int] = [6, 0, 8, 2, 1, 5]
test_out: int = 4
assert test_out == max_width_ramp(test)

test = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
test_out = 7
assert test_out == max_width_ramp(test)
