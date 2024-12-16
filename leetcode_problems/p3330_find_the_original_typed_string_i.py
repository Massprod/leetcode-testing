# Alice is attempting to type a specific string on her computer.
# However, she tends to be clumsy and may press a key for too long,
#  resulting in a character being typed multiple times.
# Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.
# You are given a string word, which represents the final output displayed on Alice's screen.
# Return the total number of possible original strings that Alice might have intended to type.
# -------------------------
# 1 <= word.length <= 100
# word consists only of lowercase English letters.
import pyperclip
from random import choice
from string import ascii_lowercase


def possible_string_count(word: str) -> int:
    # working_sol: (87.36%, 5.21%) -> (31ms, 17.14mb)  time: O(n) | space: O(1)
    # Essentially all we care is a substrings with size more than 2
    #  and repeated chars.
    # For every chars except `first` we can delete it and get a new substring.
    # So, we just count this duplicates.
    out: int = 1  # any `word` is already correct substring
    for index in range(1, len(word)):
        if word[index] == word[index - 1]:
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input string `word`.
# Always traversing whole input string `word`, once => O(n).
# -------------------------
# Auxiliary space: O(1).
# Only one extra INT used => O(1) 


test: str = "abbcccc"
test_out: int = 5
assert test_out == possible_string_count(test)

test = "abcd"
test_out = 1
assert test_out == possible_string_count(test)

test = "aaaa"
test_out = 4
assert test_out == possible_string_count(test)

test = ''.join([choice(ascii_lowercase) for _ in range(100)])
pyperclip.copy(test)
