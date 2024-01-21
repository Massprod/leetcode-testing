# Given an integer num, return a string representing its hexadecimal representation.
# For negative integers, two’s complement method is used.
# All the letters in the answer string should be lowercase characters,
#  and there should not be any leading zeros in the answer except for the zero itself.
# Note: You are not allowed to use any built-in library method to directly solve this problem.
# --------------------
# -2 ** 31 <= num <= 2 ** 31 - 1


def to_hex(num: int) -> str:
    # working_sol (99.19%, 55.41%) -> (23ms, 16.65mb)  time: O(log_16(num)) | space: O(1)
    if 0 == num:
        return '0'
    hexs: str = '0123456789abcdef'
    out: str = ''
    # Most important is to convert `num` into 32-bit unsigned integer
    if num < 0:
        num += 2 ** 32
    while num:
        rem: int = num % 16
        out = hexs[rem] + out
        num //= 16
    return out


# Time complexity :O(log_16(num))
# --------------------
# Auxiliary space: O(1).
# Nothing depends on input.
# --------------------
# https://www.geeksforgeeks.org/convert-decimal-to-hexa-decimal-including-negative-numbers/
# Most important is to convert `num` into 32-bit unsigned integer


test: int = 26
test_out: str = '1a'
assert test_out == to_hex(test)

test = -1
test_out = "ffffffff"
assert test_out == to_hex(test)

test = -123123
test_out = "fffe1f0d"
assert test_out == to_hex(test)

test = -999
test_out = "fffffc19"
assert test_out == to_hex(test)
