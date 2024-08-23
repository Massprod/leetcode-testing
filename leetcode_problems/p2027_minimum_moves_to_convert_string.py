# You are given a string s consisting of n characters which are either 'X' or 'O'.
# A move is defined as selecting three consecutive characters of s and converting them to 'O'.
# Note that if a move is applied to the character 'O', it will stay the same.
# Return the minimum number of moves required so that all the characters of s are converted to 'O'.
# -----------------------
# 3 <= s.length <= 1000
# s[i] is either 'X' or 'O'.
from random import choice


def minimum_move(s: str) -> int:
    # working_sol (95.30%, 23.52%) -> (27ms, 16.52mb)  time: O(s) | space: O(1)
    out: int = 0
    cur_seq: int = 0
    x_used: bool = False
    for char in s:
        if 'X' == char:
            x_used = True
        if x_used:
            cur_seq += 1
            if cur_seq == 3:
                if x_used:
                    out += 1
                cur_seq = 0
                x_used = False
    if x_used and cur_seq:
        out += 1
    return out


# Time complexity: O(s)
# Always traversing input string `s`, once => O(s).
# -----------------------
# Auxiliary space: O(1).
# Only 2 constant INTs used, none of them depends on input => O(1).


test: str = "XXX"
test_out: int = 1
assert test_out == minimum_move(test)

test = "XXOX"
test_out = 2
assert test_out == minimum_move(test)

test = "OOOO"
test_out = 0
assert test_out == minimum_move(test)

test = ''.join([choice(['O', 'X']) for _ in range(1000)])
print(test)
