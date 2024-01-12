# You are given a string s of even length.
# Split this string into two halves of equal lengths,
#  and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels
#  ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
# Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.
# --------------------------
# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.
from random import choice
from string import ascii_letters


def halves_are_alike(s: str) -> bool:
    # working_sol (95.66%, 19.92%) -> (32ms, 17.42mb)  time: O(n) | space: O(1)
    # Main thing, is that we don't care about anything except # of vowels.
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    out: int = 0
    # We can split in halves only by the middle.
    middle: int = len(s) // 2
    # And we need the same amount of Any vowels in first and second halves.
    for x in range(middle):
        if s[x] in vowels:
            out += 1
    for x in range(middle, len(s)):
        if s[x] in vowels:
            out -= 1
    return False if out else True


# Time complexity: O(n) <- n - length of input string `s`.
# We traverse input string `s` only once, to count both halves => O(n).
# --------------------------
# Auxiliary space: O(1).
# Set with `vowels` is always constant and doesn't depend on input.
# And Two extra INTs both of them doesn't depend on input => O(1).


test: str = "book"
test_out: bool = True
assert test_out == halves_are_alike(test)

test = "textbook"
test_out = False
assert test_out == halves_are_alike(test)

test = ''.join([choice(ascii_letters) for _ in range(1000)])
print(test)
