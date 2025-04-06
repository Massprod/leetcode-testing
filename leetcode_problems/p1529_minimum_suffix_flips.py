# You are given a 0-indexed binary string target of length n.
# You have another binary string s of length n that is initially set to all zeros.
# You want to make s equal to target.
# In one operation, you can pick an index i where 0 <= i < n
#  and flip all bits in the inclusive range [i, n - 1].
# Flip means changing '0' to '1' and '1' to '0'.
# Return the minimum number of operations needed to make s equal to target.
# -----------------------
# n == target.length
# 1 <= n <= 10 ** 5
# target[i] is either '0' or '1'.
from pyperclip import copy

from random import randint


def min_flips(target: str) -> int:
    # working_sol (64.78%, 78.41%) -> (20ms, 17.93mb)  time: O(n) | space: O(1)
    out: int = 0
    check_chars: str = '001'
    check_ind: int = 1
    # No matter from where we start (left or right),
    #  the best approach is still to flip them one by one.
    for bit in target:
        if check_chars[check_ind] == bit:
            continue
        check_ind *= -1
        out += 1

    return out


# Time complexity: O(n) <- n - length of the input string `target`.
# Always traversing whole input string `target`, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# Only constant values are used, none of them depends on input => O(1).


test: str = "10111"
test_out: int = 3
assert test_out == min_flips(test)

test = "101"
test_out = 3
assert test_out == min_flips(test)

test = "00000"
test_out = 0
assert test_out == min_flips(test)

test = ''.join([str(randint(0, 1)) for _ in range(10 ** 5)])
copy(test)
