# An n-bit gray code sequence is a sequence of 2n integers where:
#   Every integer is in the inclusive range [0, 2n - 1],
#   The first integer is 0,
#   An integer appears no more than once in the sequence,
#   The binary representation of every pair of adjacent integers differs by exactly one bit, and
#   The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.
# 1 <= n <= 16


def gray_code(n: int) -> list[int]:
    pass


test1 = 2
test1_out = [0, 1, 3, 2]

test2 = 1
test2_out = [0, 1]
