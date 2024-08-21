# Given a positive integer num,
#  return the number of positive integers less than or equal to num whose digit sums are even.
# The digit sum of a positive integer is the sum of all its digits.
# -----------------------
# 1 <= num <= 1000


def count_even(num: int) -> int:
    # working_sol (89.02%, 73.55%) -> (36ms, 16.42mb)  time: O(num) | space: O(num)
    out: int = 0
    for val in range(2, num + 1):
        if not sum([int(digit) for digit in str(val)]) % 2:
            out += 1
    return out


# Time complexity: O(num)
# Always using every value in range(2, num + 1) => O(num).
# We check every digit in `num` => O(num).
# -----------------------
# Auxiliary space: O(num)
# String and List we create depends on digits in `num` => O(num).


test: int = 4
test_out: int = 2
assert test_out == count_even(test)

test = 30
test_out = 14
assert test_out == count_even(test)
