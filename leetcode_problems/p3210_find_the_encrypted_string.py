# You are given a string s and an integer k.
# Encrypt the string using the following algorithm:
#  - For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
# Return the encrypted string.
# -------------------
# 1 <= s.length <= 100
# 1 <= k <= 10 ** 4
# s consists only of lowercase English letters.
from random import choice
from string import ascii_lowercase


def get_encrypted_string(s: str, k: int) -> str:
    # working_sol (100%, 83.54%) -> (0ms, 16.56mb)  time: O(s) | spae: O(s)
    cyclic: str = s + s
    out: str = ''.join(
        [cyclic[(index + k) % len(s)] for index in range(len(s))]
    )
    return out


# Time complexity: O(s)
# Creating `cyclic` with 2 combined `s` => O(s)
# Extra traversing whole input string `s` to get correct encrypted version => O(2 * s).
# -------------------
# Auxiliary space: O(s)
# `cyclic` <- allocates space for double `s` => O(2 * s).
# `out` <- allocates space for the same `s` sized string => O(3 * s).


test: str = "dart"
test_k: int = 3
test_out: str = "tdar"
assert test_out == get_encrypted_string(test, test_k)

test = "aaa"
test_k = 1
test_out = "aaa"
assert test_out == get_encrypted_string(test, test_k)

test = ''.join([choice(ascii_lowercase) for _ in range(100)])
print(test)
