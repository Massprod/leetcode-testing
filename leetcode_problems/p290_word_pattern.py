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
    # working_sol (79.34%, 69.6%) -> (39ms, 16.3mb)  time: O(n + m) | space: O(n + m)
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
                    # if reassign happens -> insta False
                    if word in assigned_words.values() and _ not in assigned_words:
                        return False
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
                    # if reassign happens -> insta False
                    if word in assigned_words.values() and _ not in assigned_words:
                        return False
                    if not assigned_words[_] == word:
                        return False
                    break
                word += s[x]
                index += 1
    # pattern doesn't have all words from s
    if index < len(s):
        return False
    return True

# Time complexity: O(n + m) -> traversing whole pattern once => O(n) ->
# n - len of input_pattern^^| -> but for every symbol in a pattern we're starting word_search in s,
# m - len of input_s^^|       in the worst case, it can be a pattern with 1 symbol and s with only 1 word ->
#                             -> so we're traversing pattern as O(n) and extra checking all indexes in s => O(m) ->
#                             -> overall we're checking whole pattern and whole s => O(n + m).
#                  Θ((log n) + (log m)) -> on the median we're breaking at some part of pattern ->
#                                       -> or we're checking whole pattern and only part of s. => O((log n) + (log m)).
# Auxiliary space: O(n + m) -> in the worst case, we're storing every symbol in pattern and
#                              their counterpart(word) from s, as key=value pairs => O(n + m).
#                           ! there's extra spaces between words, so it's (m - spaces_num)^^,
#                             but they're constant -> because every word is separated by other with 1 space. !
# --------------------
# Failed first commit, because missed part with reassigning same word for a multiple times.
# --------------------
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
assert test1_out == word_pattern(test1, test1_s)

test2 = "abba"
test2_s = "dog cat cat fish"
test2_out = False
print(word_pattern(test2, test2_s))
assert test2_out == word_pattern(test2, test2_s)

test3 = "aaaa"
test3_s = "dog cat cat dog"
test3_out = False
print(word_pattern(test3, test3_s))
assert test3_out == word_pattern(test3, test3_s)

test4 = "abb"
test4_s = "dog cat cat dog"
test4_out = False
print(word_pattern(test4, test4_s))
assert test4_out == word_pattern(test4, test4_s)

test5 = "baba"
test5_s = "dog cat cat dog"
test5_out = False
print(word_pattern(test5, test5_s))
assert test5_out == word_pattern(test5, test5_s)

# test6 - failed -> missed part with reassigning same word for a multiple times.
test6 = "abba"
test6_s = "dog dog dog dog"
test6_out = False
print(word_pattern(test6, test6_s))
assert test6_out == word_pattern(test6, test6_s)
