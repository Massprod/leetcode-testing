# Given a string s, reverse the string according to the following rules:
#  - All the characters that are not English letters remain in the same position.
#  - All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.
# ---------------------
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
from random import choice
from string import ascii_letters


def reverse_only_letters(s: str) -> str:
    # working_sol (72.33%, 94.51%) -> (33ms, 16.38mb)  time: O(s) | space: O(s)
    out: list[str] = list(s)
    left_l: int = 0
    right_l: int = len(s) - 1
    while left_l < right_l:
        #                                       lowercase                            uppercase
        while left_l < right_l and not 65 <= ord(s[left_l]) <= 90 and not 97 <= ord(s[left_l]) <= 122:
            left_l += 1
        while left_l < right_l and not 65 <= ord(s[right_l]) <= 90 and not 97 <= ord(s[right_l]) <= 122:
            right_l -= 1
        out[left_l], out[right_l] = out[right_l], out[left_l]
        left_l += 1
        right_l -= 1
    return ''.join(out)


# Time complexity: O(s)
# Always using every char in `s` to create an array `out` => O(s).
# Extra traversing every index of the `s`, once => O(2s).
# ---------------------
# Auxiliary space: O(s)
# `out` <- always of the same size as the input string `s` => O(s).


test: str = "ab-cd"
test_out: str = "dc-ba"
assert test_out == reverse_only_letters(test)

test = "a-bC-dEf-ghIj"
test_out ="j-Ih-gfE-dCba"
assert test_out == reverse_only_letters(test)

test = "Test1ng-Leet=code-Q!"
test_out = "Qedo1ct-eeLg=ntse-T!"
assert test_out == reverse_only_letters(test)

test = ''.join([choice(ascii_letters + ''.join(['.', '1', '2', '-'])) for _ in range(100)])
print(test)
