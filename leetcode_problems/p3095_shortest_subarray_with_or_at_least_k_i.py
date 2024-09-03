# You are given an array nums of non-negative integers and an integer k.
# An array is called special if the bitwise OR of all of its elements is at least k.
# Return the length of the shortest special non-empty subarray of nums,
#  or return -1 if no special subarray exists.
# --------------------------
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 0 <= k < 64
from random import randint


def minimum_subarray_length(nums: list[int], k: int) -> int:
    # working_sol (65.14%, 44.57%) -> (51ms, 16.51mb)  time: O(n) | space: O(1)
    def count_or(_left: int, _right: int) -> int:
        _out: int = 0
        for num in nums[_left: _right + 1]:
            _out = _out | num
        return _out

    out: int = len(nums) + 1
    left: int = 0
    right: int = 0
    cur_window: int = nums[0]
    if cur_window >= k:
        out = 1
        return out
    while right < len(nums) - 1:
        if nums[right] >= k:
            return 1
        right += 1
        cur_window = cur_window | nums[right]
        while left < right and cur_window >= k:
            out = min(out, (right - left) + 1)
            left += 1
            cur_window = count_or(left, right)
    if cur_window >= k:
        out = min(out, (right - left) + 1)
    return out if out <= len(nums) else -1


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always using `nums` indexes at most twice => O(2 * n).
# --------------------------
# Auxiliary space: O(1).


test: list[int] = [1, 2, 3]
test_k: int = 2
test_out: int = 1
assert test_out == minimum_subarray_length(test, test_k)

test = [2, 1, 8]
test_k = 10
test_out = 3
assert test_out == minimum_subarray_length(test, test_k)

test = [1, 2]
test_k = 0
test_out = 1
assert test_out == minimum_subarray_length(test, test_k)

test = [randint(0, 50) for _ in range(50)]
print(test)
