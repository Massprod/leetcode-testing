# You are given a string text of words that are placed among some number of spaces.
# Each word consists of one or more lowercase English letters and are separated by at least one space.
# It's guaranteed that text contains at least one word.
# Rearrange the spaces so that there is an equal number of spaces between every pair
#  of adjacent words and that number is maximized.
# If you cannot redistribute all the spaces equally,
#  place the extra spaces at the end, meaning the returned string should be the same length as text.
# Return the string after rearranging the spaces.
# ------------------------------
# 1 <= text.length <= 100
# text consists of lowercase English letters and ' '.
# text contains at least one word.
from random import choice
from string import ascii_lowercase


def reorder_space(text: str) -> str:
    # working_sol (88.56%, 80.30%) -> (29ms, 16.45mb)  time: O(n) | space: O(n)
    spaces: int = 0
    words: list[str] = []
    cur_word: list[str] = []
    for char in text:
        if ' ' != char:
            cur_word.append(char)
        else:
            if cur_word:
                words.append(''.join(cur_word))
            cur_word = []
            spaces += 1
    if cur_word:
        words.append(''.join(cur_word))
    required_space_chunks: int = len(words) - 1
    if 0 == required_space_chunks:
        return ''.join(words) + ' ' * spaces
    leftovers: int = spaces % required_space_chunks
    size: int = spaces // required_space_chunks
    space_string: str = ' ' * size
    out: str = space_string.join(words) + ' ' * leftovers
    return out


# Time complexity: O(n) <- n - length of the input string `text`.
# W.e the case, we always manipulate with the same # of chars.
# Because we always traverse `text` chars to get all the `spaces` and `words` => O(n).
# Extra joining all the stored chars with the same number of spaces we had before, but in different order => O(2 * n).
# ------------------------------
# Auxiliary space: O(n)
# `words` <- in the worst case will store every char from `text`, if there's no spaces => O(n).
# `cur_word` <- also can be of size `n` when there are no spaces and other words => O(2 * n).
# `space_string + out` <- always of size `n` combined => O(3 * n).


test: str = "  this   is  a sentence "
test_out: str = "this   is   a   sentence"
assert test_out == reorder_space(test)

test = " practice   makes   perfect"
test_out = "practice   makes   perfect "
assert test_out == reorder_space(test)

test = ''.join([choice(choice([ascii_lowercase, " "])) for _ in range(100)])
print(test)
