# Given an integer n, return the number of strings of length n that consist only
#  of vowels (a, e, i, o, u) and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i, s[i]
#  is the same as or comes before s[i+1] in the alphabet.
# --------------------------
# 1 <= n <= 50
from functools import cache


def count_vowel_strings(n: int) -> int:
    # working_sol (100.00%, 26.01%) -> (0ms, 17.93mb)  time: O(n) | space: O(n)
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']

    @cache
    def build(length: int, prev_start: str) -> int:
        nonlocal vowels
        if 0 >= length:
            return 1
        
        out: int = 0
        for char in vowels:
            if char > prev_start:
                continue
            out += build(length - 1, char)

        return out
    
    return build(n, 'z')


# Time complexity: O(n)
# For each `char` we could use to build our `length`, we always have 5 options.
# And because we're using the same chars and caching results.
# Essentially, we're just having traverse of `n` chars for 5 time on each index => O(n * 5).
# --------------------------
# Auxiliary space: O(n)
# Every result is cached => O(n * 5).


test: int = 1
test_out: int = 5
assert test_out == count_vowel_strings(test)

test = 2
test_out = 15
assert test_out == count_vowel_strings(test)

test = 33
test_out = 66045
assert test_out == count_vowel_strings(test)
