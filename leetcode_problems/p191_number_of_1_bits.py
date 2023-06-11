# Write a function that takes the binary representation of an unsigned integer
# and returns the number of '1' bits it has (also known as the Hamming weight).
# --------------------
# The input must be a binary string of length 32.
# --------------------
# Follow up: If this function is called many times, how would you optimize it?


def hamming_weight(n: int) -> int:
    pass


test1 = 0o0000000000000000000000000001011
test1_out = 3
print(test1)

test2 = 0o0000000000000000000000010000000
test2_out = 1
print(test2)

test3 = 11111111111111111111111111111101
test3_out = 31
print(test3)