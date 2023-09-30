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
    # working_sol (89.5%, 88.96%) -> (32ms, 16.2mb)  time: O(min(n, m)) | space: O(n + m)
    # ! s does not contain any leading or trailing spaces.
    #   All the words in s are separated by a single space. !
    all_words: list[str] = s.split(' ')
    # Every symbol in pattern should correspond to 1 word.
    if len(pattern) != len(all_words):
        return False
    # (symbol: word) <- assign every symbol in pattern to some word.
    used_syms: dict[str, str] = {}
    # (word) <- every assigned word, we can't reassign them.
    used_words: set[str] = set()
    for x in range(len(all_words)):
        # Assigned.
        if pattern[x] in used_syms:
            # But not to this word.
            if used_syms[pattern[x]] != all_words[x]:
                return False
        # Not assigned.
        else:
            # But word is already assigned.
            if all_words[x] in used_words:
                return False
            used_syms[pattern[x]] = all_words[x]
            used_words.add(all_words[x])
    return True


# Time complexity: O(min(n, m)) -> split() input string 's' => O(m) -> traverse of created array with size == 'pattern'.
# n - len of input string 'pattern'^^| Because we break if len(s) != len(pattern), we can say: O(min(n, m)).
# m - len of input string 's'^^|       We either break after split() or we will check n indexes.
# Auxiliary space: O(n + m) -> in the worst case, we're storing every symbol in pattern and
#                              their counterpart(word) from s, as key=value pairs => O(n + m) ->
#                              -> extra list with all words from 's' => O(m) ->
#                              -> extra set with all words from 's' => O(m) => O(n + 3m).
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
# Guess ordering isn't problem and I need just to check every symbol in pattern
#  corresponds with exactly one string in s.
# !
# Here follow means a full match. !
# Or order should be the same?
# W.e let's read with correct order for now.


test: str = "abba"
test_s: str = "dog cat cat dog"
test_out: bool = True
assert test_out == word_pattern(test, test_s)

test = "abba"
test_s = "dog cat cat fish"
test_out = False
assert test_out == word_pattern(test, test_s)

test = "aaaa"
test_s = "dog cat cat dog"
test_out = False
assert test_out == word_pattern(test, test_s)

test = "abb"
test_s = "dog cat cat dog"
test_out = False
assert test_out == word_pattern(test, test_s)

test = "baba"
test_s = "dog cat cat dog"
test_out = False
assert test_out == word_pattern(test, test_s)

# test - Failed -> missed part with reassigning same word for a multiple times.
test = "abba"
test_s = "dog dog dog dog"
test_out = False
assert test_out == word_pattern(test, test_s)
