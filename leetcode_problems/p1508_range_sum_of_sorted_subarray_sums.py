# You are given the array nums consisting of n positive integers.
# You computed the sum of all non-empty continuous subarrays from the array
#  and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
# Return the sum of the numbers from index left to index right (indexed from 1),
#  inclusive, in the new array.
# Since the answer can be a huge number return it modulo 10 ** 9 + 7.
# ------------------------
# n == nums.length
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 100
# 1 <= left <= right <= n * (n + 1) / 2
from random import randint


def range_sum(nums: list[int], n: int, left: int, right: int) -> int:
    # working_sol (76.55%, 7.08%) -> (213ms, 43.73mb)  time: O(n * n) | space: O(k)
    sums: list[int] = []
    for index in range(len(nums)):
        cur_sum: int = nums[index]
        sums.append(cur_sum)
        for range_end in range(index + 1, len(nums)):
            cur_sum += nums[range_end]
            sums.append(cur_sum)
    return sum(sorted(sums)[left - 1: right]) % (10 ** 9 + 7)


# Time complexity: O(n * n) <- n - length of the input array `nums`, k - length of the `sums`.
# Standard nested loop to check every index => O(n * n)
# `sums` will be of size `n * (n + 1) / 2`, and we're sorting in as whole => O(n * n + k * log k).
# ! `sums` is always of the same size, because we use every subarray !
# Extra slice of size `right - left` and sum of it => O(n * n + k * log k + (right - left) * 2).
# All of these, suppressed by nested loop `n * n` => O(n * n).
# ------------------------
# Auxiliary space: O(k + (right - left))
# `sums` <- always of the same size == `n * (n + 1) / 2` => O(k).
# If we consider slice, extra (right - left) => O(k + (right - left) * 2).


test: list[int] = [1, 2, 3, 4]
test_n: int = 4
test_left: int = 1
test_right: int = 5
test_out: int = 13
assert test_out == range_sum(test, test_n, test_left, test_right)

test = [1, 2, 3, 4]
test_n = 4
test_left = 3
test_right = 4
test_out = 6
assert test_out == range_sum(test, test_n, test_left, test_right)

test = [1, 2, 3, 4]
test_n = 4
test_left = 1
test_right = 10
test_out = 50
assert test_out == range_sum(test, test_n, test_left, test_right)

test = [randint(1, 100) for _ in range(1000)]
print(test)
