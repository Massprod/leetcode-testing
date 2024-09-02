# You have an array of floating point numbers averages which is initially empty.
# You are given an array nums of n integers where n is even.
# You repeat the following procedure n / 2 times:
#  - Remove the smallest element, minElement, and the largest element maxElement, from nums.
#  - Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.
# -------------------------
# 2 <= n == nums.length <= 50
# n is even.
# 1 <= nums[i] <= 50


def minimum_average(nums: list[int]) -> float:
    # working_sol (84.85%, 99.12%) -> (42ms, 16.38mb)  time: O(n * log n) | space: O(n)
    sorted_nums: list[int] = sorted(nums)
    out: float = sorted_nums[-1]
    left: int = 0
    right: int = len(sorted_nums) - 1
    while left < right:
        out = min(
            out, (sorted_nums[left] + sorted_nums[right]) / 2
        )
        left += 1
        right -= 1
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting input array `nums`, once => O(n * log n).
# Extra using every value from `sorted_nums`, once => O(n * log n + n).
# -------------------------
# Auxiliary space: O(n)
# `sorted_nums` <- sorted copy of the original array `nums` => O(n).


test: list[int] = [7, 8, 3, 4, 15, 13, 4, 1]
test_out: float = 5.5
assert test_out == minimum_average(test)

test = [1, 9, 8, 3, 10, 5]
test_out = 5.5
assert test_out == minimum_average(test)

test = [1, 2, 3, 7, 8, 9]
test_out = 5.0
assert test_out == minimum_average(test)
