# You are given two strings order and s.
# All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted.
# More specifically, if a character x occurs before a character y in order,
#  then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.
# ----------------------------
# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.
from random import choice, shuffle
from string import ascii_lowercase


def custom_sort_string(order: str, s: str) -> str:
    # working_sol (81.57%, 91.57%) -> (31ms, 16.44mb)  time: O(n * log n) | space: O(n)
    cor_order: dict[str, int] = {char: index for index, char in enumerate(order)}
    # All we care about is placing, out of order chars in the End of a string.
    out: str = ''.join(sorted(s, key=lambda x: cor_order[x] if x in cor_order else 300))
    return out


# Time complexity: O(n * log n) n - length of input string `s`
# Basic built in sort() => O(n * log n).
# ----------------------------
# Auxiliary space: O(n).
# Creating extra array of size `n` and creating string `out` from it with the same size `n` => O(n).


test: str = "cba"
test_s: str = "abcd"
test_out: str = "cbad"
assert test_out == custom_sort_string(test, test_s)

test = "bcafg"
test_s = "abcd"
test_out = "bcad"
assert test_out == custom_sort_string(test, test_s)

test_pre: list[str] = list(ascii_lowercase)
shuffle(test_pre)
test = ''.join(test_pre)
test_s = ''.join([choice(ascii_lowercase) for _ in range(200)])
print(test)
print('====================!')
print(test_s)
