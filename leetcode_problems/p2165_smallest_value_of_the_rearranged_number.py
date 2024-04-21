# You are given an integer num. Rearrange the digits of num such that its value
#  is minimized, and it does not contain any leading zeros.
# Return the rearranged number with minimal value.
# Note that the sign of the number does not change after rearranging the digits.
# ------------------
# -10 ** 15 <= num <= 10 ** 15
from random import randint


def smallest_number(num: int) -> int:
    # working_sol (71.94%, 93.88%) -> (34ms, 16.49mb)  time: O(n * log n) | space: O(n)
    if not num:
        return num
    digits: list[str]
    if num > 0:
        digits = sorted([digit for digit in str(num)])
        index: int = 0
        while '0' == digits[index]:
            index += 1
        digits[0], digits[index] = digits[index], digits[0]
    else:
        digits = sorted([digit for digit in str(num)[1:]], reverse=True)
    out: int = int(''.join(digits))
    return out if num > 0 else out * -1


# Time complexity: O(n * log n) <- n - number of digits in the input value `num`.
# Always rebuild input integer `num` into array with every digit as string `digits` and sorting it => O(n * log n).
# Extra joining them after sorting and converting => O(n).
# ------------------
# Auxiliary space: O(n).
# Every digit from `num` is stored as string in `digits` => O(n).


test: int = 310
test_out: int = 103
assert test_out == smallest_number(test)

test = -7605
test_out = -7650
assert test_out == smallest_number(test)

test = 111
test_out = 111
assert test_out == smallest_number(test)

test = -111
test_out = -111
assert test_out == smallest_number(test)

test = randint(-10 ** 15, 10 ** 15)
print(test)
