# You are given an integer array nums, and an integer k.
# Let's introduce K-or operation by extending the standard bitwise OR.
# In K-or, a bit position in the result is set to 1
#  if at least k numbers in nums have a 1 in that position.
# Return the K-or of nums.
# -----------------------
# 1 <= nums.length <= 50
# 0 <= nums[i] < 2 ** 31
# 1 <= k <= nums.length
from random import randint


def find_k_or(nums: list[int], k: int) -> int:
    # working_sol (62.47%, 83.80%) -> (76ms, 16.49mb)  time: O(n * max(nums)) | space: O(max(nums))
    out: list[str] = []
    while any(nums):
        cur_count: int = 0
        for index in range(len(nums)):
            if nums[index] & 1:
                cur_count += 1
            nums[index] >>= 1
        if k <= cur_count:
            out.append('1')
        else:
            out.append('0')
    if not out:
        return 0
    return int(''.join(out[::-1]), 2)


# Time complexity: O(n * max(nums)) <- n - length of the input array `nums`
# Always depleting every value from `nums` to 0.
# But because maximum value is going to have maximum # of bits, we're depleting every bit of it => O(n * max(nums)).
# -----------------------
# Auxiliary space: O(max(nums)).
# Every bit from `max(nums)` is going to be stored in `out` => O(max(nums)).


test: list[int] = [7, 12, 9, 8, 9, 15]
test_k: int = 4
test_out: int = 9
assert test_out == find_k_or(test, test_k)

test = [2, 12, 1, 11, 4, 5]
test_k = 6
test_out = 0
assert test_out == find_k_or(test, test_k)

test = [10, 8, 5, 9, 11, 6, 8]
test_k = 1
test_out = 15
assert test_out == find_k_or(test, test_k)

test = [14, 7, 12, 9, 8, 9, 1, 15]
test_k = 4
test_out = 13
assert test_out == find_k_or(test, test_k)

test = [randint(0, 2 ** 31) for _ in range(50)]
print(test)
