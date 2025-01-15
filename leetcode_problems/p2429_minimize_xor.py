# Given two positive integers num1 and num2,
#  find the positive integer x such that:
#  - x has the same number of set bits as num2, and
#  - The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.
# Return the integer x. The test cases are generated such that
#  x is uniquely determined.
# The number of set bits of an integer is the number of 1's
#  in its binary representation.
# ---------------------------
# 1 <= num1, num2 <= 10 ** 9


def minimize_xor(num1: int, num2: int) -> int:
    # working_sol (100.00%, 41.60%) -> (0ms, 17.72mb)  time: O(n + k) | space: O(n + k)
    # We need to nulify all set bits in `num1`.
    # Prefer to start from MSB -> lower value in the end.
    # And if we stil have extra bits from `num2`,
    #  we need to place it on unset bit places in `num1`.
    bits_count: int = num2.bit_count()
    extra_bits: int = bits_count - num1.bit_count()
    if 0 == extra_bits:
        return num1
    num1_bits: list[str] = list(bin(num1)[2:])
    set_bits: list[str] = ['0' for _ in range(len(num1_bits))]
    index: int = len(num1_bits) - 1
    # If we can not only nulify set bits == `1` in `num1`,
    #  but have smth extra to place.
    # We need to place it starting from LSB.
    while -1 < index and 0 < extra_bits:
        # We don't care about `1`, because it should be nullified anyway.
        if '0' == num1_bits[index]:
            set_bits[index] = '1'
            extra_bits -= 1
            bits_count -= 1
        index -= 1
    index = 0
    # Everything else is just about removing MSB from `num1`.
    # Which is going to give us smaller value.
    while len(num1_bits) > index and bits_count:
        if '1' == num1_bits[index]:
            set_bits[index] = '1'
            bits_count -= 1
        index += 1
    # If after everything, we still have some unset bits.
    # We have no other option than add them as MSB.
    set_bits = ['1' for _ in range(bits_count)] + set_bits

    return int(''.join(set_bits), base=2)


# Time complexity: O(n + k) <- n - number of bits in `num1`, k - number of bits in `num2`.
# Count both input value bits => O(n + k).
# Traversing `num1` bits to set desired bits in `set_bits` => O(n).
# Add extra bits after exhausting everything => O(k).
# ---------------------------
# Auxiliary space: O(n + k)
# `num1_bits` <- allocates space for each bit in `num1` => O(n).
# `set_bits` <- allocates space for each bit in `num1`,
#               takes extra space for extra bits from `num2` => O(n + k).


test_1: int = 3
test_2: int = 5
test_out: int = 3
assert test_out == minimize_xor(test_1, test_2)

test_1 = 1
test_2 = 12
test_out = 3
assert test_out == minimize_xor(test_1, test_2)
