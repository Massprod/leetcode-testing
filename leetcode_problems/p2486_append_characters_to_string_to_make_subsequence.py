# You are given two strings s and t consisting of only lowercase English letters.
# Return the minimum number of characters that need to be appended
#  to the end of s so that t becomes a subsequence of s.
# A subsequence is a string that can be derived from another string
#  by deleting some or no characters without changing the order of the remaining characters.
# ---------------------------
# 1 <= s.length, t.length <= 10 ** 5
# s and t consist only of lowercase English letters.
from string import ascii_lowercase
from random import choice


def append_characters(s: str, t: str) -> int:
    # working_sol (89.94%, 72.52%) -> (50ms, 17.54mb)  time: O(n) | space: O(1)
    present: int = 0
    for char in s:
        if t[present] == char:
            present += 1
            if present >= len(t):
                break
    return len(t) - present


# Time complexity: O(n) <- n - length of an input string `s`.
# In the worst case, we're always traversing whole `s`, once => O(s)
# ---------------------------
# Auxiliary space: O(1)
# Only one constant INT used `present` doesn't depend on input => O(1)


test_s: str = "coaching"
test_t: str = "coding"
test_out: int = 4
assert test_out == append_characters(test_s, test_t)

test_s = "abcde"
test_t = "a"
test_out = 0
assert test_out == append_characters(test_s, test_t)

test_s = "z"
test_t = "abcde"
test_out = 5
assert test_out == append_characters(test_s, test_t)

test_s = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
test_t = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
print(test_s)
print('--------------')
print(test_t)
