# Given an integer array nums, return the greatest common divisor
#  of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer
#  that evenly divides both numbers.
# --------------------
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000


def find_gcd(nums: list[int]) -> int:
    # working_sol (38.13%, 71.91%) -> (57ms, 16.64mb)  time: O(n + log(min(a, b))) | space: O(1)
    min_val: int = 1000
    max_val: int = 0
    for val in nums:
        min_val = min(val, min_val)
        max_val = max(max_val, val)

    def gcd(higher: int, lower: int):
        if 0 == lower:
            return higher
        return gcd(lower, higher % lower)

    return gcd(max_val, min_val)


# Time complexity: O(n + log(min(a, b))) <- n - length of the input array `nums`
#                                           a - maximum value in `nums`
#                                           b - minimum value in `nums`
# Always traversing whole input array `nums`, once => O(n).
# Extra finding GCD of `min_val` and `max_val` => O(n + log(min(a, b)).
# --------------------
# Auxiliary space: O(1).


test: list[int] = [2, 5, 6, 9, 10]
test_out: int = 2
assert test_out == find_gcd(test)

test = [7, 5, 6, 8, 3]
test_out = 1
assert test_out == find_gcd(test)

test = [3, 3]
test_out = 3
assert test_out == find_gcd(test)
