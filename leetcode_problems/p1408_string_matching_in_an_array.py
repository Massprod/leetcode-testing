# Given an array of string words, return all strings in words that is a substring of another word.
# You can return the answer in any order.
# A substring is a contiguous sequence of characters within a string
# -------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.


def string_matching(words: list[str]) -> list[str]:
    # working_sol (83.74%, 77.33%) -> (36ms, 16.44mb)  time: O(n * (n * k)) | space: O(n * k)
    out: list[str] = []
    for word in words:
        for other_word in words:
            if word != other_word and word in other_word:
                out.append(word)
                break
    return out


# Time complexity: O(n * (n * k)) <- k - average length of word in `words`, n - length of the input array `words`
# Always traversing every word in `words` and comparing it with every word in `words` => O(n * (n * k)).
# -------------------
# Auxiliary space: O(n * k)
# In the worst case, every string in `words` is going to be correct substring.
# But one of them should contain all of these substrings, so `out` will store `n - 1` strings => O((n - 1) * k).


test: list[str] = ["mass", "as", "hero", "superhero"]
test_out: list[str] = ["as", "hero"]
assert test_out == string_matching(test)

test = ["leetcode", "et", "code"]
test_out = ["et", "code"]
assert test_out == string_matching(test)

test = ["blue", "green", "bu"]
test_out = []
assert test_out == string_matching(test)
