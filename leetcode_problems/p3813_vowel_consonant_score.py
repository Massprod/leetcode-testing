# You are given a string s consisting of lowercase English letters, spaces, and digits.
# Let v be the number of vowels in s and c be the number of consonants in s.
# A vowel is one of the letters 'a', 'e', 'i', 'o', or 'u',
#  while any other letter in the English alphabet is considered a consonant.
# The score of the string s is defined as follows:
#  - If c > 0, the score = floor(v / c)
#    where floor denotes rounding down to the nearest integer.
#  - Otherwise, the score = 0.
# Return an integer denoting the score of the string.
# --- --- --- ---
# 1 <= s.length <= 100
# s consists of lowercase English letters, spaces and digits.
import math


def vowel_consonant_score(s: str) -> int:
    # working_solution: (100%, 20.74%) -> (0ms, 19.57mb)  Time: O(s) Space: O(1)
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}
    num_vowels: int = 0
    num_consonants: int = 0

    for char in s:
        if not char or char.isdigit() or ' ' == char:
            continue
        if char in vowels:
            num_vowels += 1
        else:
            num_consonants += 1
    if 0 >= num_consonants:
        return 0
    
    out: int = math.floor(num_vowels / num_consonants)
    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(1)


test: str = 'cooear'
test_out: int = 2
assert test_out == vowel_consonant_score(test)

test = 'axeyizou'
test_out = 1
assert test_out == vowel_consonant_score(test)

test = 'au 123'
test_out = 0
assert test_out == vowel_consonant_score(test)
