# You are given a 0-indexed integer array nums.
# A subarray of nums is called continuous if:
#  - Let i, i + 1, ..., j be the indices in the subarray.
#    Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
# Return the total number of continuous subarrays.
# A subarray is a contiguous non-empty sequence of elements within an array.
# ------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
import pyperclip
from random import randint


def continuous_subarrays(nums: list[int]) -> int:
    # working_sol: (75.83%, 90.32%) -> (619ms, 27.39mb)  time: O(n) | space: O(1)
    # Expand window while we can.
    # Then remove sub_windows which can be used with the next window.
    window_length: int
    out: int = 0
    left: int = 0
    right: int = 0
    window_min: int = nums[0]
    window_max: int = nums[0]
    for right in range(len(nums)):
        # 0 <= |nums[i1] - nums[i2]| <= 2
        # If it stands for `min` and `max` value of the subarray.
        # Then it stands for every value.
        window_max = max(window_max, nums[right])
        window_min = min(window_min, nums[right])
        if not (2 < (window_max - window_min)):
            continue
        # Don't count +1 for 0-indexed, because we're not using `right`.
        # It's out of correct sequence
        window_length = right - left
        out += window_length * (window_length + 1) // 2
        left = right
        window_min = window_max = nums[right]
        # If we can build a window starting from inside our current window.
        # We need to find a start of it and remove subarrays we will use
        #  with this next window.
        while 0 < left and 2 >= abs(nums[right] - nums[left - 1]):
            left -= 1
            window_min = min(window_min, nums[left])
            window_max = max(window_max, nums[left])
        remove_length: int = right - left
        out -= remove_length * (remove_length + 1) // 2
    # Last subarray can be never triggered, because whole array is correct seq.
    # Or we just need to count the last value.
    window_length = right - left + 1
    out += window_length * (window_length + 1) // 2
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# In the worst case, only 1 sized subarrays can be used.
# So, we will use every index of the `nums`, twice => O(2 * n).
# ------------------------
# Auxiliary space: O(1)
# Only 6 constant INTs used, none of them depends on input => O(1).


test: list[int] = [5, 4, 2, 4]
test_out: int = 8
assert test_out == continuous_subarrays(test)

test = [1, 2, 3]
test_out = 6
assert test_out == continuous_subarrays(test)

test = [randint(1, 10 ** 9) for _ in range(100)]
pyperclip.copy(test)
