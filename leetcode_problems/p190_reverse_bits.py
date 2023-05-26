# Reverse bits of a given 32 bits unsigned integer.
# ------------------
# The input must be a binary string of length 32


def reverse_bits(n: int) -> int:
    reverse: int = 0
    for x in range(32):
        reverse = reverse << 1
        less_signi: int = n & 1
        reverse += less_signi
        n = n >> 1
    return reverse


# We need to reverse read input bits, and return INT for this reversed bits.
# * y << x * -> shifting bits, by deleting most significant(left) and inserting 0 at other end.
#             x => number of bits to shift.
# ^^ equal to  y * 2 ** x
# 0010 << 1 -> 0100
# 0010 << 2 -> 1000
# * y >> x * -> shifting bits, by deleting less significant(right) and copying most significant(left)
# 0010 >> 1 -> 0001 => 0 most signi, 0 less signi 0+001-0
# 0010 >> 2 -> 0000 => 1shift == 0 most signi, 0 less signi 0+001-0 => 0001
#                      2shift == 0 most signi, 1 less signi 0+000-1 => 0000
# ^^ equal to  y / 2 ** x
# Every positive_integer in 32bit_system represented:
#      Sign  Exponent   Fraction
#      0     00000000   00000000000000000000000
# Bit  31    [30 - 23]  [22        -         0]
# Flow:
#   So we can read given input INT by bits, from right to left, because we need to reverse it.
#   Starting from 0 with 0b0, we either add 1 or not.
#   Which is going to depend on less significant bit we have in input INT.
#   We're shifting left * reverse << 1 * to make a room for a new bit,
#   and new bit is going to be 0, 1 depending on * n & 1 * ->
#   -> which is bit AND operand checking bits from n with our mask(1) ->
#   -> our mask(1) only have 1 bit, so it's deciding what less significant bit in n is.
#    if it's 1 return 1 and if 0 return 0, (AND -> only both bits 11 return TRUE)
#   -> appending this last bit into our reverse by just adding it ->
#   -> this is going to place our less_signi n bit at correct place in reverse,
#    because we're populating backwards.
