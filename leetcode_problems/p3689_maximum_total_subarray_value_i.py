# You are given an integer array nums of length n and an integer k.
# You need to choose exactly k non-empty subarrays nums[l..r] of nums.
# Subarrays may overlap, and the exact same subarray (same l and r)
#  can be chosen more than once.
# The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).
# The total value is the sum of the values of all chosen subarrays.
# Return the maximum possible total value you can achieve.
# --- --- --- ---
# 1 <= n == nums.length <= 5 * 10​​​​​​​ ** 4
# 0 <= nums[i] <= 10 ** 9
# 1 <= k <= 10 ** 5


def max_total_value(nums: list[int], k: int) -> int:
    # working_solution: (35.20%, 60.0%) -> (18ms, 26.40mb)  Time: O(n) Space: O(1)
    val_max: int = max(nums)
    val_min: int = min(nums)
    # Best approach is to take maximum difference.
    # Which is basically max_val - min_val of the array, and we can reuse subs.
    out: int = (val_max - val_min) * k
    
    return out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 3, 2]
test_k: int = 2
test_out: int = 4
assert test_out == max_total_value(test, test_k)

test = [4, 2, 5, 1]
test_k = 3
test_out = 12
assert test_out == max_total_value(test, test_k)
