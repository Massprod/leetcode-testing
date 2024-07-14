# We have two special characters:
#  - The first character can be represented by one bit 0.
#  - The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0,
#  return true if the last character must be a one-bit character.
# ----------------------
# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.
from random import randint


def is_one_bit_character(bits: list[int]) -> bool:
    # working_sol (67.89%, 93.12%) -> (49ms, 16.46mb)  time: O(n) | space: O(1)
    # We build from left -> right.
    # And we care only about, how we build last char of the string.
    # If we're using to build two-bit char => False
    # Otherwise, it's solely used to build one-bit char by itself => True
    building: bool = False
    index: int = 0
    while index < len(bits) - 1:
        # We start to build two-bits chars => 10 or 11
        # If we're ending it => `1` => 11.
        if 1 == bits[index]:
            building = not building
        # If we're ending it with `0` => 10
        elif building:
            building = not building
        index += 1
    return not building


# Time complexity: O(n) <- n - length of the input array `bits`.
# Always traversing input array `bits` for `n - 1` indexes, once => O(n - 1).
# ----------------------
# Auxiliary space: O(1)
# Only 2 constant vars used: `bool` + `int`.
# None of them depends on input => O(1).


test: list[int] = [1, 0, 0]
test_out: bool = True
assert test_out == is_one_bit_character(test)

test = [1, 1, 1, 0]
test_out = False
assert test_out == is_one_bit_character(test)

test = [randint(0, 1) for _ in range(999)] + [0]
print(test)
