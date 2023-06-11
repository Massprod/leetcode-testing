# Write a function that takes the binary representation of an unsigned integer
# and returns the number of '1' bits it has (also known as the Hamming weight).
# --------------------
# The input must be a binary string of length 32.
# --------------------
# Follow up: If this function is called many times, how would you optimize it?


def hamming_weight(n: int) -> int:
    # working_sol (53.4%, 39.5%) -> (45ms, 16.2mb)  time: O(n) | space: O(1)
    mask: int = 1
    count: int = 0
    while n:
        count += n & mask
        n = n >> 1
    return count

# Time complexity: O(n) -> looping until we delete every less_signi_bit and n becomes 0 => O(n).
# Auxiliary space: O(1) -> 2 extra INTs, 1 can be deleted, doesn't depend on input => O(1)
# --------------------
# Basic bit manipulation with deleting lsb and counting this 1 bit value.


test1 = 0o0000000000000000000000000001011
test1_out = 3
print(hamming_weight(test1))
assert test1_out == hamming_weight(test1)

test2 = 0o0000000000000000000000010000000
test2_out = 1
print(test2)
print(hamming_weight(test2))
assert test2_out == hamming_weight(test2)

test3 = 0o11111111111111111111111111111101
test3_out = 31
print(hamming_weight(test3))
assert test3_out == hamming_weight(test3)
