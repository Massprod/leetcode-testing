# Given a string s, calculate its reverse degree.
# The reverse degree is calculated as follows:
#  1. For each character, multiply its position in the reversed alphabet
#  ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
#  2. Sum these products for all characters in the string.
# Return the reverse degree of s.
# --------------------
# 1 <= s.length <= 1000
# s contains only lowercase English letters.


def reverse_degree(s: str) -> int:
    # working_sol (75.95%, 98.83%) -> (7ms, 17.54mb)  time: O(s) | space: O(1)
    out: int = 0
    for index, char in enumerate(s):
        deg: int = ((122 - ord(char)) + 1) * (index + 1)
        out += deg

    return out


# Time complexity: O(s).
# Traversing whole input string `s`, once => O(s).
# --------------------
# Auxiliary space: O(1)


test: str = 'abc'
test_out: int = 148
assert test_out == reverse_degree(test)

test = 'zaza'
test_out = 160
assert test_out == reverse_degree(test)
