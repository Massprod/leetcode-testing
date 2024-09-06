# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
# For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
# Given a string n that represents a positive decimal integer,
#  return the minimum number of positive deci-binary numbers needed so that they sum up to n.
# ----------------------
# 1 <= n.length <= 10 ** 5
# n consists of only digits.
# n does not contain any leading zeros and represents a positive integer.


def min_partitions(n: str) -> int:
    # working_sol (27.21%, 78.32%) -> (150ms, 17.18mb)  time: O(n) | space: O(1)
    # All we essentially care is the MAXIMUM DIGIT in the number.
    # Because w.e the place it will be positioned at,
    #  or value it's going to have, we NEED to cover it.
    # Examples:
    #   1_234_789 -> we cover 1_111_111
    #   123_678 -> we cover 111_111
    #   13_567 -> we cover 11_111
    #   2_456 -> we cover 1_111
    #   1_345 -> we cover 1_111
    #   234 -> we cover 111
    #   123 -> we cover 101
    #   22 -> we cover 11
    #   11 -> we cover 11 => 0
    # `24`:
    #   24 -> we need to cover 2 first
    #   24 -> we cover 1
    #   23 -> we cover 1
    #   22 -> we cover 11
    #   11 -> we cover 11
    return int(max(n, key=lambda x: int(x)))


# Time complexity: O(n)
# Always traversing every char in `n` => O(n).
# ----------------------
# Auxiliary space: O(1).


test: str = "32"
test_out: int = 3
assert test_out == min_partitions(test)

test = "82734"
test_out = 8
assert test_out == min_partitions(test)

test = "27346209830709182346"
test_out = 9
assert test_out == min_partitions(test)
