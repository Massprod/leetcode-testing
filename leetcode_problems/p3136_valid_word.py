# A word is considered valid if:
#  - It contains a minimum of 3 characters.
#  - It contains only digits (0-9), and English letters (uppercase and lowercase).
#  - It includes at least one vowel.
#  - It includes at least one consonant.
# You are given a string word.
# Return true if word is valid, otherwise, return false.
# Notes:
#  - 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
#  - A consonant is an English letter that is not a vowel.
# ----------------------------
# 1 <= word.length <= 20
# word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
from string import ascii_letters


def is_valid(word: str) -> bool:
    # working_sol (72.24%, 77.25%) -> (34ms, 16.50mb)  time: O(n) | space: O(1)
    if 3 > len(word):
        return False
    alphabet: set[str] = set(ascii_letters)
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_present: bool = False
    consonant_present: bool = False
    for char in word:
        digit: bool = char.isdigit()
        if char not in alphabet and not digit:
            return False
        if digit:
            continue
        if char in vowels:
            vowel_present = True
        elif char not in vowels:
            consonant_present = True
    return vowel_present and consonant_present


# Time complexity: O(n) <- n - length of the input string `word`.
# Always traversing every char from the input string `word`, once => O(n).
# ----------------------------
# Auxiliary space: O(1)
# Nothing depends on input => O(1).


test: str = "234Adas"
test_out: bool = True
assert test_out == is_valid(test)

test = "b3"
test_out = False
assert test_out == is_valid(test)

test = "a3$e"
test_out = False
assert test_out == is_valid(test)

test = "AhI"
test_out = True
assert test_out == is_valid(test)
