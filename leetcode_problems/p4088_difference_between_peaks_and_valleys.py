# You are given an integer array nums of length n.
# An index i is called a peak if all of the following conditions hold:
#  - 0 < i < n - 1
#  - nums[i] > nums[i - 1]
#  - nums[i] > nums[i + 1]
# An index i is called a valley if all of the following conditions hold:
#  - 0 < i < n - 19
#  - nums[i] < nums[i - 1]
#  - nums[i] < nums[i + 1]
# Return an integer denoting the difference between the sum of all peak values
#  and the sum of all valley values.
# --- --- --- ---
# 3 <= n == nums.length <= 100
# -100 <= nums[i] <= 100


def peak_valley_difference(nums: list[int]) -> int:
    # working_solution: (83.06%, 83.13%) -> (2ms, 19.1mb)  Time: O(n) Space: O(1)
    sum_peaks: int = 0
    sum_valleys: int = 0
    for index in range(1, len(nums) - 1):
        if nums[index - 1] < nums[index] > nums[index + 1]:
            sum_peaks += nums[index]
        elif nums[index - 1] > nums[index] < nums[index + 1]:
            sum_valleys += nums[index]
    
    return sum_peaks - sum_valleys


# Time complexity: O(n)
# n - lengt of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 5, 2, 4, 1, 3, 0]
test_out: int = 9
assert test_out == peak_valley_difference(test)

test = [-5, -6, -1, -2, 5, 3, 2]
test_out = 12
assert test_out == peak_valley_difference(test)

test = [6, 5, 2, 5, 5, 3, 6]
test_out = -5
assert test_out == peak_valley_difference(test)
