# You are given a 0-indexed string s that has lowercase English letters
#  in its even indices and digits in its odd indices.
# There is a function shift(c, x), where c is a character
#  and x is a digit, that returns the xth character after c.
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
# Return s after replacing all digits.
# It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
# ----------------------
# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# shift(s[i-1], s[i]) <= 'z' for all odd indices i.


def replace_digits(s: str) -> str:
    # working_sol (35.74%, 59.59%) -> (38ms, 16.49mb)  time: O(s) | space: O(s)

    def shift(char: str, shift: int) -> str:
        return chr(ord(char) + shift)

    out: list[str] = []
    for index in range(len(s)):
        if index % 2:
            out.append(
                shift(s[index - 1], int(s[index]))
            )
        else:
            out.append(s[index])
    return ''.join(out)


# Time complexity: O(s)
# Always using every index of `s`, once => O(s).
# ----------------------
# Auxiliary space: O(s)
# Every char from `s` is stored in `out`, even after shift => O(s).


test: str = "a1c1e1"
test_out: str = "abcdef"
assert test_out == replace_digits(test)

test = "a1b2c3d4e"
test_out = "abbdcfdhe"
assert test_out == replace_digits(test)
