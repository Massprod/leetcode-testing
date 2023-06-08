# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string,
# and then at each step perform either of the following:
#   Append the character '0' zero times.
#   Append the character '1' one times.
#   This can be performed any number of times.
# A good string is a string constructed by the above process having a length between low and high (inclusive).
#
# Return the number of different good strings that can be constructed satisfying these properties.
# Since the answer can be large, return it modulo 10 ** 9 + 7.
# ------------------------
# 1 <= low <= high <= 105  ,  1 <= zero, one <= low


def count_good_strings(low: int, high: int, zero: int, one: int) -> int:
    pass


test1_low = 3
test1_high = 3
test1_zero = 1
test1_one = 1
test1_out = 8

test2_low = 2
test2_high = 3
test2_zero = 1
test2_one = 2
test2_out = 5
