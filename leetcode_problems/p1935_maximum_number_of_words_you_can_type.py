# There is a malfunctioning keyboard where some letter keys do not work.
# All other keys on the keyboard work properly.
# Given a string text of words separated by a single space (no leading or trailing spaces)
#  and a string brokenLetters of all distinct letter keys that are broken,
#  return the number of words in text you can fully type using this keyboard.
# -------------------
# 1 <= text.length <= 10 ** 4
# 0 <= brokenLetters.length <= 26
# text consists of words separated by a single space without any leading or trailing spaces.
# Each word only consists of lowercase English letters.
# brokenLetters consists of distinct lowercase English letters.


def can_be_typed_words(text: str, broken_letters: str) -> int:
    # working_sol (67.28%, 49.66%) -> (35ms, 16.62mb)  time: O(n + k) | space: O(n + k)
    broken: set[str] = set(broken_letters)
    words: list[str] = text.split(' ')
    out: int = 0
    for word in words:
        out += 1
        for char in word:
            if char in broken:
                out -= 1
                break
    return out


# Time complexity: O(n + k) <- n - length of the input string `text`, k - length of the input string `broken_letters`.
# Always traversing whole `text` to get all the words => O(n).
# Extra traversing every char in words to get correct ones => O(n + n).
# Extra traversing `broken_letters` to get all unique chars, once => O(2 * n + k).
# -------------------
# Auxiliary space: O(n + k)
# `broken` <- allocates space for each char from `broken_letters` => O(k).
# In the worst case there's only 1 word in `text`.
# `words` <- allocates space for each char from `text` => O(n).


test: str = "hello world"
test_broken: str = "ad"
test_out: int = 1
assert test_out == can_be_typed_words(test, test_broken)

test = "leet code"
test_broken = "lt"
test_out = 1
assert test_out == can_be_typed_words(test, test_broken)

test = "leet code"
test_broken = "e"
test_out = 0
assert test_out == can_be_typed_words(test, test_broken)
