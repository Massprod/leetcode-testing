# The complement of an integer is the integer you get when you flip all the 0's to 1's
#  and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.
# ----------------
# 0 <= n < 10 ** 9


def bitwise_complement(n: int) -> int:
    # working_sol (97.26%, 88.81%) -> (28ms, 16.2mb)  time: O(K) | space: O(1)
    # Essentially we need to just reverse 1 -> 0, 0 -> 1.
    bit_mask: int = 0
    # Create mask with '1' placed, for every bit of n.
    for _ in bin(n)[2:]:
        bit_mask = (bit_mask << 1) + 1
    # Reverse them with XOR.
    # 1 ^ 1 -> 0 , 0 ^ 1 -> 1.
    out: int = n ^ bit_mask
    return out


# Time complexity: O(K) -> converting input_value into binary representation and for every bit: shift + 1 => O(n) ->
# K - len of input_binary string^^| -> extra XOR input_value on created mask => O(1).
# Auxiliary space: O(1) -> only 2 extra constant INTs used, none of them depends on input => O(1).


test: int = 5
test_out: int = 2
assert test_out == bitwise_complement(test)

test = 7
test_out = 0
assert test_out == bitwise_complement(test)

test = 10
test_out = 5
assert test_out == bitwise_complement(test)
