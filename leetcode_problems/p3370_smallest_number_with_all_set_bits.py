# You are given a positive number n.
# Return the smallest number x greater than or equal to n,
#  such that the binary representation of x contains only set bits.
# A set bit refers to a bit in the binary representation of a number that has a value of 1.
# ---------------------
# 1 <= n <= 1000


def smallest_number(n: int) -> int:
    # working_sol (100.0%, 100.0%) -> (0ms, 17.19mb)  time: O(n) | space: O(n)
    # `0x` <- we don't need it.
    cur_bits: str = bin(n)[2:]
    zero_present: bool = False
    # If there's at least one unset bit.
    # Then we can just convert it and get a higher value.
    for bit in cur_bits:
        if '0' == bit:
            zero_present = True
            break
    if zero_present:
        return int(''.join(['1' for _ in cur_bits]), 2)
    # If there are no unset bits, then we can just return `n`.
    return n


# Time complexity: O(n)
# Always converting `n` to binary string, and in the worst case -> traverse all the string => O(n).
# Auxiliary space: O(n)
# `cur_bits` <- allocates space for bits in `n` => O(n).


test: int = 5
test_out: int = 7
assert test_out == smallest_number(test)

test = 10
test_out = 15
assert test_out == smallest_number(test)

test = 3
test_out = 3
assert test_out == smallest_number(test)
