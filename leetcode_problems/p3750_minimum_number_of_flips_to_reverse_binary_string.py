# You are given a positive integer n.
# Let s be the binary representation of n without leading zeros.
# The reverse of a binary string s is obtained by writing the characters
#  of s in the opposite order.
# You may flip any bit in s (change 0 → 1 or 1 → 0).
# Each flip affects exactly one bit.
# Return the minimum number of flips required to make s equal
#  to the reverse of its original form.
# --- --- --- ---
# 1 <= n <= 10 ** 9


def minimum_flips(n: int) -> int:
    # working_solution: (100%, 36.94%) -> (0ms, 17.87mb)  Time: O(n) Space: O(n)
    current: str = str(bin(n)[2:])  # slice `0b`
    reverse: str = current[::-1]
    out: int = 0

    for index in range(len(current)):
        out += 1 if current[index] != reverse[index] else 0 
    
    return out


# Time complexity: O(n)
# Traversing every bit of the `n`, twice => O(2 * n).
# --- --- --- ---
# Space complexity: O(n)
# `current` <- allocates space for each bit of the `n` => O(n).
# `reverse` <- allocates space for each bit of the `n` => O(2 * n).


test: int = 7
test_out: int = 0
assert test_out == minimum_flips(test)

test = 10
test_out = 4
assert test_out == minimum_flips(test)
