# Given a positive integer n, find and return the longest
#  distance between any two adjacent 1's in the binary representation of n.
# If there are no two adjacent 1's, return 0.
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
# The distance between two 1's is the absolute difference between their bit positions.
# For example, the two 1's in "1001" have a distance of 3.
# ----------------------
# 1 <= n <= 10 ** 9


def binary_gap(n: int) -> int:
    # working_sol (51.11%, 17.32%) -> (36ms, 16.61mb)  time: O(n) | space: O(1)
    out: int = 0
    cur_dist: int = 0
    start: bool = False
    while n:
        if n & 1:
            if not start:
                start = True
                cur_dist = 0
            elif cur_dist:
                out = max(out, cur_dist)
                cur_dist = 0
        n >>= 1
        cur_dist += 1
    return out


# Time complexity: O(n)
# Always using every bit of the input value `n` => O(n).
# ----------------------
# Auxiliary space: O(1)
# Only constants used, none of them depends on input => O(1).


test: int = 22
test_out: int = 2
assert test_out == binary_gap(test)

test = 8
test_out = 0
assert test_out == binary_gap(test)

test = 5
test_out = 2
assert test_out == binary_gap(test)

test = 6
test_out = 1
assert test_out == binary_gap(test)
