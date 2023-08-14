# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# -------------------
# 1 <= s.length <= 3 * 10 ** 5
# s consist of printable ASCII characters.
from string import ascii_lowercase, ascii_uppercase
from random import choice


def reverse_vowels(s: str) -> str:
    # working_sol (96.46%, 70.38%) -> (48ms, 17.3mb)  time: O(n) | space: O(n)
    # Vowels to check.
    vowels: set[str] = set('aAeEiIoOuU')
    # String can't be changed, so we need something to store and switch.
    s: list[str] = list(s)
    # Using window to switch all vowels.
    # We just need to reverse STRING with only vowels in it,
    # inside our input_string.
    left_l: int = 0
    right_l: int = len(s) - 1
    while left_l < right_l:
        while left_l < right_l and s[left_l] not in vowels:
            left_l += 1
        while left_l < right_l and s[right_l] not in vowels:
            right_l -= 1
        s[left_l], s[right_l] = s[right_l], s[left_l]
        left_l += 1
        right_l -= 1
    return ''.join(s)


# Time complexity: O(n) -> traversing input_array, once to create list and extra one to switch => O(2n).
# n - len of input_array^^|
# Auxiliary space: O(n) -> creating list with size of input_array => O(n) -> extra set with all vowels to use, and
#                          2 constant INTs, they don't depend on input => O(1).
# -------------------
# Ok. I hope that understood correctly, just reserve all VOWELS as a string inside. Without any other condition.
# Then it can be done with stack or dict with saving indexes. Or actually a window, left|right and switch them
# until left == right.


test: str = "hello"
test_out: str = "holle"
assert test_out == reverse_vowels(test)

test = "leetcode"
test_out = "leotcede"
assert test_out == reverse_vowels(test)

test = ''
for _ in range(10 ** 5):
    test += choice([choice(ascii_uppercase), choice(ascii_lowercase)])
# print(test)
