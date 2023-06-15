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
    assigned_words: dict[str, str] = {}
    index: int = 0
    for _ in pattern:
        word: str = ""
        # s doesn't have all counterparts in pattern
        if index == len(s):
            return False
        elif _ not in assigned_words:
            for x in range(index, len(s)):
                if s[x] == " " or x == len(s) - 1:
                    if x == len(s) - 1:
                        word += s[x]
                    index += 1
                    assigned_words[_] = word
                    break
                word += s[x]
                index += 1
        elif _ in assigned_words:
            for x in range(index, len(s)):
                if s[x] == " " or x == len(s) - 1:
                    if x == len(s) - 1:
                        word += s[x]
                    index += 1
                    if not assigned_words[_] == word:
                        return False
                    break
                word += s[x]
                index += 1
    # pattern doesn't have all words from s
    if index < len(s):
        return False
    return True


# Well according to test5, order of reading should be considered,
# because there's a -> cat and b -> dog and if we ignore order it's should be correct(True).
# But correct answer is False, so we're reading in order.
# --------------------
# For a pairing between X and Y (where Y need not be different from X) to be a bijection,
# four properties must hold:
#   1 -> each element of X must be paired with at least one element of Y,
#   2 -> no element of X may be paired with more than one element of Y,
#   3 -> each element of Y must be paired with at least one element of X, and
#   4 -> no element of Y may be paired with more than one element of X.
# Guess ordering isn't problem and I need just to check evey symbol in pattern
# corresponds with exactly one string in s.
# !
# Here follow means a full match. !
# Or order should be the same?
# W.e let's read with correct order for now.


test1 = "abba"
test1_s = "dog cat cat dog"
test1_out = True
print(word_pattern(test1, test1_s))

test2 = "abba"
test2_s = "dog cat cat fish"
test2_out = False
print(word_pattern(test2, test2_s))

test3 = "aaaa"
test3_s = "dog cat cat dog"
test3_out = False
print(word_pattern(test3, test3_s))

test4 = "abb"
test4_s = "dog cat cat dog"
test4_out = False
print(word_pattern(test4, test4_s))

test5 = "baba"
test5_s = "dog cat cat dog"
test5_out = False
print(word_pattern(test5, test5_s))
