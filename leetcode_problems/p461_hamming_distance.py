# The Hamming distance between two integers is the number
#  of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.
# ----------------
# 0 <= x, y <= 2 ** 31 - 1


def hamming_distance(x: int, y: int) -> int:
    # working_sol (92.21%, 62.57%) -> (30ms, 16.45mb)  time: O(len(bin(x ^ y))) | space: O(1)
    # ! For binary strings a and b the Hamming distance
    #   is equal to the number of ones (population count) in a XOR b. !
    # We can use it for INTs if we consider their sequences of bits.
    out: int = 0
    val: int = x ^ y
    while val > 0:
        # Count every 1 bit in (x XOR y).
        if val & 1:
            out += 1
        val >>= 1
    return out


# Time complexity: O(len(bin(x ^ y))).
# Essentially we're just traversing whole binary string of (x ^ y).
# ----------------
# Auxiliary space: O(1).
# Guess we can call it constant, because in our case we're just creating INT(`val`) == x ^ y.
# And this `val` is always in 32bits range.
# ----------------
# https://en.wikipedia.org/wiki/Hamming_distance


test_x: int = 1
test_y: int = 4
test_out: int = 2
assert test_out == hamming_distance(test_x, test_y)

test_x = 3
test_y = 1
test_out = 1
assert test_out == hamming_distance(test_x, test_y)
