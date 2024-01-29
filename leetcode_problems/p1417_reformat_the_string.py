# You are given an alphanumeric string s.
# (Alphanumeric string is a string consisting of lowercase English letters and digits).
# You have to find a permutation of the string where no letter is followed by another letter
#  and no digit is followed by another digit.
# That is, no two adjacent characters have the same type.
# Return the reformatted string or return an empty string if it is impossible to reformat the string.
# ----------------------
# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.
from random import choice
from string import ascii_lowercase, digits


def reformat(s: str) -> str:
    # working_sol (91.48%, 67.61%) -> (37ms, 16.68mb)  time: O(s) | space: O(s)
    chars: list[str] = []
    digits: list[str] = []
    for sym in s:
        if sym.isdigit():
            digits.append(sym)
        else:
            chars.append(sym)
    out: str = ''
    # We can only reformat correctly if 1 symbol diff OR equal number of digits and chars.
    if abs(len(chars) - len(digits)) > 1:
        return out
    # For correct reformatted string, we need to start from Highest option.
    # Like: 123abcd => a1b2c3d , otherwise => 1a2b3cd.
    # If they're equal, then its doesn't matter.
    lower: list[str] = digits if len(chars) > len(digits) else chars
    higher: list[str] = chars if len(chars) > len(digits) else digits
    # But if someone Higher, we need to add this extra symbol.
    last_sym: str = ''
    if len(chars) != len(digits):
        last_sym = chars[-1] if len(chars) > len(digits) else digits[-1]
    for index in range(len(lower)):
        out += higher[index] + lower[index]
    return out + last_sym


# Time complexity: O(s).
# Traversing whole input string `s` once to get all digits and chars => O(s).
# Extra using all symbols again to build reformatted string => O(s).
# ----------------------
# Auxiliary space: O(s).
# Always store whole `s` in `chars` and `digits`, and output string `out` will be the same size => O(2s).


test: str = "a0b1c2"
test_out: str = "a0b1c2"
assert test_out == reformat(test)

test = "leetcode"
test_out = ""
assert test_out == reformat(test)

test = "1229857369"
test_out = ""
assert test_out == reformat(test)

test = ''.join(choice(ascii_lowercase + digits) for _ in range(500))
print(test)
