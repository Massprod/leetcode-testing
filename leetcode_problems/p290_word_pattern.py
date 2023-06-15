# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection
#   between a letter in pattern and a non-empty word in s.
# --------------------
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


def word_pattern(pattern: str, s: str) -> bool:
    pass


test1 = "abba"
test1_s = "dog cat cat dog"
test1_out = True

test2 = "abba"
test2_s = "dog cat cat fish"
test2_out = False

test3 = "aaaa"
test3_s = "dog cat cat dog"
test3_out = False
