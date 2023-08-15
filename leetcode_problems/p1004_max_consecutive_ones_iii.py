# Given a binary array nums and an integer k,
#   return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# --------------
# 1 <= nums.length <= 10 ** 5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
from random import randint


def longest_ones(nums: list[int], k: int) -> int:
    # working_sol (93.49%, 77.37%) -> (470ms, 17.02mb)  time: O(n) | space: O(1)
    left_l: int = 0
    right_l: int = 0
    count_zeroes: int = 0
    max_con_sub: int = 0
    while right_l != len(nums):
        # By default:
        # 1 == True | 0 == False
        if nums[right_l]:
            right_l += 1
            continue
        count_zeroes += 1
        # If limit exceeding we can calculate current subsequence.
        if count_zeroes > k:
            max_con_sub = max(right_l - left_l, max_con_sub)
        right_l += 1
        # Shrink current window until it's correct on '0' counter.
        while count_zeroes > k:
            if not nums[left_l]:
                count_zeroes -= 1
                left_l += 1
                continue
            left_l += 1
    # If limit never exceeded, we need to calc it explicitly.
    # Can be calculated for every iteration, but we don't need to.
    max_con_sub = max(right_l - left_l, max_con_sub)
    return max_con_sub


# Time complexity: O(n) -> in the worst case with k == 0 and list like [1, 1, 1, 1 ... 1, 0], we will traverse
# n - len of input_array^^| n - 2 indexes and then shrink window for the same amount => O(2n).
# Auxiliary space: O(1) -> only 4 constant INTs used, none of them depends on input => O(1).
# --------------
# Maintain count of '0' and when exceed flip limit shrink window? Should be correct.


test: list[int] = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
test_k: int = 2
test_out: int = 6
assert test_out == longest_ones(test, test_k)

test = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
test_k = 3
test_out = 10
assert test_out == longest_ones(test, test_k)

test = []
for _ in range(10 ** 5):
    test.append(randint(0, 1))
# print(test)
# print(randint(0, len(test)))
