# Given an integer n, you must transform it into 0 using the following operations any number of times:
#   - Change the rightmost (0th) bit in the binary representation of n.
#   - Change the ith bit in the binary representation of n if the (i-1)th bit
#      is set to 1 and the (i-2)th through 0th bits are set to 0.
# Return the minimum number of operations to transform n into 0.
# -------------------
# 0 <= n <= 10 ** 9


def min_one_bit_ops(n: int) -> int:
    # working_sol (83.77%, 21.43%) -> (36ms, 16.41mb)  time: O(log(log n) * log n) | space: O(1)
    return n ^ min_one_bit_ops(n >> 1) if n else 0


# Time complexity: O(log(log n) * log n)
# Auxiliary space: O(1)
# -------------------
# Editorial for GrayCode. This version is for any integer size, instead of only 32bit in editorial.


test: int = 3
test_out: int = 2
assert test_out == min_one_bit_ops(test)

test = 6
test_out = 4
assert test_out == min_one_bit_ops(test)

test = 999
test_out = 698
assert test_out == min_one_bit_ops(test)

test = 41235
test_out = 49634
assert test_out == min_one_bit_ops(test)
