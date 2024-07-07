# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because
#  128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right,
#  return a list of all the self-dividing numbers in the range [left, right].
# ----------------------
# 1 <= left <= right <= 10 ** 4


def self_dividing_numbers(left: int, right: int) -> list[int]:
    # working_sol (75.76%, 98.32%) -> (42ms, 16.39mb)  time: O(n) | space: O(n)
    out: list[int] = []
    for num in range(left, right + 1):
        orig: int = num
        while num:
            digit: int = num % 10
            if 0 == digit:
                break
            if orig % digit:
                break
            num //= 10
        if not num:
            out.append(orig)
    return out


# Time complexity: O(n) <- n - range between `left` and `right` inclusive.
# Always check all the values between `left` and `right`, inclusive => O(n)
# ----------------------
# Auxiliary space: O(n)
# Worst case: every value in range will be correct, so we will store everything => O(n)


test_l: int = 1
test_r: int = 22
test_out: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert test_out == self_dividing_numbers(test_l, test_r)

test_l = 47
test_r = 85
test_out = [48, 55, 66, 77]
assert test_out == self_dividing_numbers(test_l, test_r)
