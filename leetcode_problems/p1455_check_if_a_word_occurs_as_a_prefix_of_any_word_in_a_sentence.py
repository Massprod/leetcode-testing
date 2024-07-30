# Given a sentence that consists of some words separated by a single space,
#  and a searchWord, check if searchWord is a prefix of any word in sentence.
# Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word.
# If searchWord is a prefix of more than one word,
#  return the index of the first word (minimum index).
# If there is no such word return -1.
# A prefix of a string s is any leading contiguous substring of s.
# -----------------------
# 1 <= sentence.length <= 100
# 1 <= searchWord.length <= 10
# sentence consists of lowercase English letters and spaces.
# searchWord consists of lowercase English letters.


def is_prefix_of_word(sentence: str, search_word: str) -> int:
    # working_sol (94.55%, 57.74%) -> (26ms, 16.48mb)  time: O(n) | space: O(n)
    for index, word in enumerate(sentence.split(' ')):
        if word.startswith(search_word):
            return index + 1
    return -1


# Time complexity: O(n) <- n - length of the input string `sentence`,
#                          k - length of the input string `search_word`.
# In the worst case, we're going to have all words in sentence of the equal length,
#  and `search_word` will be incorrect word for them, but only differ by the last char.
# So, we will traverse the whole `sentence` to get all the words => O(n)
# Extra traverse every word from `sentence` and check `len(word) - 1` indexes,
#  this is essentially traversing whole `sentence` again, -some spaces => O(2 * n).
# -----------------------
# Auxiliary space: O(n)
# `split` <- will give us array of `sentence` without space => O(n).


test: str = "i love eating burger"
test_word: str = "burg"
test_out: int = 4
assert test_out == is_prefix_of_word(test, test_word)

test = "this problem is an easy problem"
test_word = "pro"
test_out = 2
assert test_out == is_prefix_of_word(test, test_word)

test = "i am tired"
test_word = "you"
test_out = -1
assert test_out == is_prefix_of_word(test, test_word)
