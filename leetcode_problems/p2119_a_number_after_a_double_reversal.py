# Reversing an integer means to reverse all its digits.
# For example, reversing 2021 gives 1202.
# Reversing 12300 gives 321 as the leading zeros are not retained.
# Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2.
# Return true if reversed2 equals num. Otherwise return false.
# --------------------
# 0 <= num <= 10 ** 6
from random import randint


def is_same_after_reversals(num: int) -> bool:
    # working_sol (79.33%, 89.71%) -> (31ms, 16.49mb)  time: O(n) | space: O(n)
    if not num:
        return True
    out: int = int(str(num)[::-1].lstrip('0')[::-1])
    return out == num


# Time complexity: O(n) <- n - number of digits in `num`.
# Always traversing whole digits once to reverse first, and in the worst case there's no `0` in `num`.
# So, we will extra traverse them to reverse again => O(2n).
# --------------------
# Auxiliary space: O(n)
# Converting `num` to the string with all digits in it => O(n).


test: int = 526
test_out: bool = True
assert test_out is is_same_after_reversals(test)

test = 1800
test_out = False
assert test_out is is_same_after_reversals(test)

test = 0
test_out = True
assert test_out is is_same_after_reversals(test)

test = randint(0, 10 ** 6)
print(test)
