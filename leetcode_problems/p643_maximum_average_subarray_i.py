# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value
#   and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.
# ---------------------
# n == nums.length
# 1 <= k <= n <= 10 ** 5
# -10 ** 4 <= nums[i] <= 10 ** 4


def find_max_average(nums: list[int], k: int) -> float:
    # working_sol (78.25%, 96.92%) -> (1037ms, 27.84mb)  time: O(n) | space: O(1)
    # Left|Right indexes to maintain window.
    left_l: int = 0
    right_l: int = k - 1
    # First window sum.
    cur_sum: int = sum(nums[left_l:k])
    # First avg of this window.
    max_avg: float = cur_sum / k
    # Slide window and increase by new element added,
    # decrease by element deleted.
    while right_l < len(nums) - 1:
        cur_sum -= nums[left_l]
        left_l += 1
        right_l += 1
        cur_sum += nums[right_l]
        # Recheck max_avg for every window.
        max_avg = max(max_avg, cur_sum / k)
    return max_avg


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 4 constants used, none of them depends on input => O(1).
# ---------------------
# Ok. Its bad idea to rush solution without checking max_constraints especially like this.
# I was calculating sum for every window we can build, which is dumb AF. But I only woke up,
# and didn't even bother to think for Easy. We need to maintain cur_cum and increase by new,
# decrease by deleted. Brain-lag is real.
# ! Remind yourself that overconfidence is a slow and insidious killer !


test: list[int] = [1, 12, -5, -6, 50, 3]
test_k: int = 4
test_out: float = 12.75000
assert test_out == find_max_average(test, test_k)

test = [5]
test_k = 1
test_out = 5.00000
assert test_out == find_max_average(test, test_k)
