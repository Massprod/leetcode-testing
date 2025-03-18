# You are given a string target.
# Alice is going to type target on her computer using a special keyboard
#  that has only two keys:
#  - Key 1 appends the character "a" to the string on the screen.
#  - Key 2 changes the last character of the string on the screen
#     to its next character in the English alphabet.
#    For example, "c" changes to "d" and "z" changes to "a".
# Note that initially there is an empty string "" on the screen,
#  so she can only press key 1.
# Return a list of all strings that appear on the screen as Alice types target,
#  in the order they appear, using the minimum key presses.
# -------------------------
# 1 <= target.length <= 400
# target consists only of lowercase English letters.
from pyperclip import copy

from random import choice

from string import ascii_lowercase


def string_sequence(target: str) -> list[str]:
    # working_sol (80%, 20%) -> (19ms, 26.7mb)  time: O(n) | space: O(n)
    out: list[str] = []
    cur_str: str = ''
    index: int = 0
    while len(cur_str) != len(target):
        new_str: str = 'a'
        out.append(cur_str + new_str)
        while new_str != target[index]:
            chr_ascii: int = (ord(new_str) + 1)
            if 123 <= chr_ascii:
                chr_ascii = 97
            new_str = chr(chr_ascii)
            out.append(cur_str + new_str)
        cur_str += new_str
        index += 1

    return out


# Time complexity: O(n) <- n - length of the input string `target`.
# In the worst case we're getting target of `zzzzzz` and we will transform from `a`
#  with the maximum steps => O(n * 26).
# -------------------------
# Auxiliary space: O(n)
# `out` <- allocates space for all of these steps => O(n * 26).


test: str = 'abc'
test_out: list[str] = ["a", "aa", "ab", "aba", "abb", "abc"]
assert test_out == string_sequence(test)

test = 'he'
test_out = ["a", "b", "c", "d", "e", "f", "g", "h", "ha", "hb", "hc", "hd", "he"]
assert test_out == string_sequence(test)

test = ''.join([choice(ascii_lowercase) for _ in range(400)])
copy(test)
