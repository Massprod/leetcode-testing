# You are given an integer array nums containing positive integers.
# We define a function encrypt such that encrypt(x) replaces every digit in x
#  with the largest digit in x.
# For example, encrypt(523) = 555 and encrypt(213) = 333.
# Return the sum of encrypted elements.
# --------------------------
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 1000
from random import randint


def sum_of_encrypted_int(nums: list[int]) -> int:
    # working_sol (77.39%, 35.06%) -> (49ms, 16.58mb)  time: O(n * k) | space: O(1)
    out: int = 0

    def encrypt(number: int) -> int:
        cur_number: int = number
        digits: int = 0
        max_digit: int = 0
        while cur_number:
            max_digit = max(max_digit, cur_number % 10)
            cur_number //= 10
            digits += 1
        out_number: int = 0
        for _ in range(digits):
            out_number *= 10
            out_number += max_digit
        return out_number

    for num in nums:
        out += encrypt(num)
    return out


# Time complexity: O(n * k) <- n - length of the input array `nums`, k - average bits in `nums` numbers.
# Always using every bit of all numbers from `nums` => O(n * k).
# --------------------------
# Auxiliary space: O(1).


test: list[int] = [1, 2, 3]
test_out: int = 6
assert test_out == sum_of_encrypted_int(test)

test = [10, 21, 31]
test_out = 66
assert test_out == sum_of_encrypted_int(test)

test = [randint(1, 1000) for _ in range(50)]
print(test)
