# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each word consists of lowercase and uppercase English letters.
# A sentence can be shuffled by appending the 1-indexed word position to each word
#  then rearranging the words in the sentence.
# For example, the sentence "This is a sentence" can be shuffled as
#  "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words,
#  reconstruct and return the original sentence.
# ------------------------
# 2 <= s.length <= 200
# s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
# The number of words in s is between 1 and 9.
# The words in s are separated by a single space.
# s contains no leading or trailing spaces.


def sort_sentence(s: str) -> str:
    # working_sol (92.52%, 14.31%) -> (27ms, 16.50mb)  time: O(s) | space: O(s)
    words: list[str] = s.split(' ')
    out: list[str] = ['' for _ in words]
    for word in words:
        out[int(word[-1]) - 1] = word[:-1]
    return ' '.join(out)


# Time complexity: O(s)
# Traversing whole `s` for splitting, once => O(s).
# In the worst case there's 2 words, so we extra traverse `len(s) - 1` chars to build `out` => O(s + (s - 1)).
# ------------------------
# Auxiliary space: O(s)
# `out` <- will hold every word from `words` and in our worst_case it's `s - 1` chars => O(s - 1).


test: str = "is2 sentence4 This1 a3"
test_out: str = "This is a sentence"
assert test_out == sort_sentence(test)

test = "Myself2 Me1 I4 and3"
test_out = "Me Myself and I"
assert test_out == sort_sentence(test)
