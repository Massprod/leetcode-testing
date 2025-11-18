# Given a binary string s, return the number of substrings with all characters 1's.
# Since the answer may be too large, return it modulo 10 ** 9 + 7.
# --- --- --- ---
# 1 <= s.length <= 10 ** 5
# s[i] is either '0' or '1'.
from random import choice
from pyperclip import copy


def numb_sub(s: str) -> int:
    # working_solution: (66.67%, 97.75%) -> (15ms, 17.96mb)  Time: O(n) Space: O(1)
    out: int = 0
    streak:int = 0
    num_one: str = '1'
    num_zero: str = '0'

    for char in s:
        if num_one == char:
            streak += 1
        elif num_zero == char:
            out += (streak + 1) * streak // 2
            streak = 0
    
    if streak:
       out += (streak + 1) * streak // 2 
    
    return out % (10 ** 9 + 7)


# Time complexity: O(s)
# Always traversing the whole input string `s`, once => O(s).
# --- --- --- ---
# Space complexity: O(1)


test: str = '0110111'
test_out: int = 9
assert test_out == numb_sub(test)

test = '101'
test_out = 2
assert test_out == numb_sub(test)

test = '111111'
test_out = 21
assert test_out == numb_sub(test)

test = ''.join([choice(['1', '0']) for _ in range(10 ** 5)])
copy(test)
