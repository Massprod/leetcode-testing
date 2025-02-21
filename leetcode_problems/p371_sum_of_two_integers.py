# Given two integers a and b, return the sum of the two integers
#  without using the operators + and -.
# ------------------
# -1000 <= a, b <= 1000


def get_sum(a: int, b: int) -> int:
    # working_sol (100.00%, 95.68%) -> (0ms, 17.58mb)  time: O(log(max(a, b))) | space: O(1)
    # If we can't `+`, we can bitwise sum :)
    # XOR gives us bitwise sum of bits.
    # With `0` on place where 1 + 1.
    # And if we actually get some carry after 1 + 1
    # We can use it after we use `a & b` which annuls everything except `1`
    #  in both digits + shifting this carry bit to the left position.
    # Which is essentially bitwise sum operation.
    # -----
    # For Python3 - we need extra check for 32 bits integer.
    # Otherwise it's unsigned and we will get infinite loop.
    MASK = 0xFFFFFFFF  # Mask to get last`` 32 bits
    MAX_INT = 0x7FFFFFFF  # Max positive 32-bit integer

    a &= MASK
    b &= MASK

    while 0 != b:
        sum_no_carry: int = a ^ b
        carry: int = (a & b) << 1
        a, b = sum_no_carry, carry
        b = b & MASK

    # We can use as it is.
    # Or we will need to remove extra bits and reverse after it.
    return a if a <= MAX_INT else ~(a ^ MASK)


# Time complexity: O(log(max(a, b)))
# Auxiliary space: O(1)


test_a: int = 1
test_b: int = 2
test_out: int = 3
assert test_out == get_sum(test_a, test_b)

test_a = 2
test_b = 3
test_out = 5
assert test_out == get_sum(test_a, test_b)
