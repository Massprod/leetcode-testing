# You are given a string s consisting only of the characters '0' and '1'.
# In one operation, you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal.
# For example, the string "010" is alternating, while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.
# ---------------------
# 1 <= s.length <= 10 ** 4
# s[i] is either '0' or '1'.
from random import choice


def min_operations(s: str) -> int:
    # working_sol (93.70%, 5.67%) -> (42ms, 17.3mb)  time: O(n) | space: O(1)
    first_path: int = 0
    cor_sym: str = '0'
    # Start from '0'.
    for sym in s:
        if not cor_sym == sym:
            first_path += 1
        if cor_sym == '0':
            cor_sym = '1'
        else:
            cor_sym = '0'
    # First path already present.
    if not first_path:
        return first_path
    second_path: int = 0
    cor_sym = '1'
    # Start from '1'.
    for sym in s:
        if not cor_sym == sym:
            second_path += 1
        if cor_sym == '0':
            cor_sym = '1'
        else:
            cor_sym = '0'
    return min(first_path, second_path)


# Time complexity: O(n) <- n - length of input string `s`.
# Double traver of original input string `s` => O(2n).
# Auxiliary space: O(1).
# `cor_sym` always the same size + 2 extra INTs to store both path operations => O(1).


test: str = "0100"
test_out: int = 1
assert test_out == min_operations(test)

test = "10"
test_out = 0
assert test_out == min_operations(test)

test = "1111"
test_out = 2
assert test_out == min_operations(test)

test = ''.join([choice(['1', '0']) for _ in range(10 ** 4)])
print(test)
