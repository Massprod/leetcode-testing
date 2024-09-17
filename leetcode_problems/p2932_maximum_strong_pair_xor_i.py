# You are given a 0-indexed integer array nums.
# A pair of integers x and y is called a strong pair if it satisfies the condition:
#  |x - y| <= min(x, y)
# You need to select two integers from nums such that they form a strong pair
#  and their bitwise XOR is the maximum among all strong pairs in the array.
# Return the maximum XOR value out of all possible strong pairs in the array nums.
# Note that you can pick the same integer twice to form a pair.
# ----------------------------
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 100


def maximum_strong_pair_xor(nums: list[int]) -> int:
    # working_sol (13.74%, 95.69%) -> (152ms, 16.35mb)  time: O(n * n) | space: O(1)
    out: int = 0
    for num1 in nums:
        for num2 in nums:
            if abs(num1 - num2) <= min(num1, num2):
                out = max(out, num1 ^ num2)
    return out


# Time complexity: O(n * n) <- n - length of the input array `nums`.
# Always traversing whole `nums` with nested loop => O(n * n).
# ----------------------------
# Auxiliary space: O(1).


test: list[int] = [1, 2, 3, 4, 5]
test_out: int = 7
assert test_out == maximum_strong_pair_xor(test)

test = [10, 100]
test_out = 0
assert test_out == maximum_strong_pair_xor(test)

test = [5, 6, 25, 30]
test_out = 7
assert test_out == maximum_strong_pair_xor(test)
