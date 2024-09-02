# You are given a string word.
# A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.
# -------------------
# 1 <= word.length <= 50
# word consists of only lowercase and uppercase English letters.
from string import ascii_lowercase


def number_of_special_chars(word: str) -> int:
    # working_sol (59.33%, 99.73%) -> (37ms, 16.30mb)  time: O(n) | space: O(1)
    # { char: [lower_present, upper_present] }
    all_chars: dict[str, list[int]] = {
        char: [0, 0] for char in ascii_lowercase
    }
    for char in word:
        if char in all_chars:
            all_chars[char][0] = 1
            continue
        lower_ver: str = char.lower()
        if lower_ver in all_chars:
            all_chars[lower_ver][1] = 1
    out: int = 0
    for char, present in all_chars.items():
        if all(present):
            out += 1
    return out


# Time complexity: O(n) <- length of the input string `word`.
# Always using every char from input string `word`, once => O(n).
# -------------------
# Auxiliary space: O(1).
# `all_chars` <- always of the same size => O(1).
# Extra only 1 constant INT `out` is used => O(1).


test: str = "aaAbcBC"
test_out: int = 3
assert test_out == number_of_special_chars(test)

test = "abc"
test_out = 0
assert test_out == number_of_special_chars(test)

test = "abBCab"
test_out = 1
assert test_out == number_of_special_chars(test)
