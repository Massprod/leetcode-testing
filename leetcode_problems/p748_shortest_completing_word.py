# Given a string licensePlate and an array of strings words,
#  find the shortest completing word in words.
# A completing word is a word that contains all the letters in licensePlate.
# Ignore numbers and spaces in licensePlate, and treat letters as case insensitive.
# If a letter appears more than once in licensePlate,
#  then it must appear in the word the same number of times or more.
# For example, if licensePlate = "aBc 12c",
#  then it contains letters 'a', 'b' (ignoring case), and 'c' twice.
# Possible completing words are "abccdef", "caaacab", and "cbca".
# Return the shortest completing word in words. It is guaranteed an answer exists.
# If there are multiple shortest completing words, return the first one that occurs in words.
# ----------------------
# 1 <= licensePlate.length <= 7
# licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 15
# words[i] consists of lower case English letters.
from collections import defaultdict


def shortest_completing_word(license_plate: str, words: list[str]) -> str:
    # working_sol (49.25%, 88.18%) -> (79ms, 16.79mb)  time: O(k * (g + n)) | space: O(n + max(words))
    # {char: occurrences}
    plate_chars: dict[str, int] = defaultdict(int)
    for char in license_plate:
        char_ascii: int = ord(char)
        if 65 <= char_ascii <= 90 or 97 <= char_ascii <= 122:
            plate_chars[char.lower()] += 1
    out: str = 'a' * 16
    min_word_length: int = 16
    for word in words:
        if len(word) < min_word_length:
            min_word_length = len(word)
    for word in words:
        # {char: occurrences}
        word_chars: dict[str, int] = defaultdict(int)
        for char in word:
            if char in plate_chars:
                word_chars[char] += 1
        cor: bool = False
        for char in plate_chars:
            if word_chars[char] < plate_chars[char]:
                cor = False
                break
            cor = True
        if cor:
            if len(out) > len(word):
                out = word
                if len(out) == min_word_length:
                    return out
    return out


# Time complexity: O(k * (g + n)) <- n - length of the input string `license_plate`,
#                                    k - length of the input array `words`,
#                                    g - average length of words in `words`.
# Always traversing `license_plate` to get all chars and occurrences => O(n).
# Traversing whole `words` to get minimum lengths presented in the array => O(n + k).
# Traversing whole `words` again, but with counting chars for every word => O(k * g).
# In the worst case, we will check every symbol and word with `plate_chars`
# So, for every word we counted, we're going to traverse `plate_chars` (every symbol in `license_plate` is unique
#  and `plate_chars` keys == `n` => O(n + k + k * (g + n)).
# ----------------------
# Auxiliary space: O(n + max(words)).
# `plate_chars` will hold every unique symbol of `license_plate`.
# `word_chars` will allocate space for a maximum sized word from `words` => O(n + max(words)).


test_plate: str = "1s3 PSt"
test_words: list[str] = ["step", "steps", "stripe", "stepple"]
test_out: str = "steps"
assert test_out == shortest_completing_word(test_plate, test_words)

test_plate = "1s3 456"
test_words = ["looks", "pest", "stew", "show"]
test_out = "pest"
assert test_out == shortest_completing_word(test_plate, test_words)
