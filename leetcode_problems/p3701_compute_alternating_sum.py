# You are given an integer array nums.
# The alternating sum of nums is the value obtained by adding elements at even indices
#  and subtracting elements at odd indices. That is, nums[0] - nums[1] + nums[2] - nums[3]...
# Return an integer denoting the alternating sum of nums.
# --- --- --- ---
# constraints1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def alternating_sum(nums: list[int]) -> int:
    # working_solution: (100%, 36.36%) -> (0ms, 17.99mb)  Time: O(n) Space: O(1)
    out: int = 0
    for index, value in enumerate(nums):
        if index % 2:
            out -= value
        else:
            out += value
    
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing the whole input array `nums`, once => O(n).
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 3, 5, 7]
test_out: int = -4
assert test_out == alternating_sum(test)

test = [100]
test_out = 100
assert test_out == alternating_sum(test)
