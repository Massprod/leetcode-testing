# You are given a positive integer n.
# Let even denote the number of even indices in the binary representation of n with value 1.
# Let odd denote the number of odd indices in the binary representation of n with value 1.
# Note that bits are indexed from right to left in the binary representation of a number.
# Return the array [even, odd].
# ---------------------
# 1 <= n <= 1000


def even_odd_bits(n: int) -> list[int]:
    # working_sol (28.18%, 40.90%) -> (42ms, 16.51mb)  time: O(n) | space: O(1)
    even: bool = True
    out: list[int] = [0, 0]
    while n:
        if even:
            if n & 1:
                out[0] += 1
        else:
            if n & 1:
                out[1] += 1
        even = not even
        n >>= 1
    return out


# Time complexity: O(n)
# Always depleting `n` to `0` => O(n).
# ---------------------
# Auxiliary space: O(1)
# `out` <- always contains 2 INTs, nothing depends on input => O(1).


test: int = 50
test_out: list[int] = [1, 2]
assert test_out == even_odd_bits(test)

test = 2
test_out = [0, 1]
assert test_out == even_odd_bits(test)
