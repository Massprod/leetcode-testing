# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.
# ----------------------
# 1 <= sentences.length <= 100
# 1 <= sentences[i].length <= 100
# sentences[i] consists only of lowercase English letters and ' ' only.
# sentences[i] does not have leading or trailing spaces.
# All the words in sentences[i] are separated by a single space.


def most_words_found(sentences: list[str]) -> int:
    # working_sol (92.71%, 94.03%) -> (38ms, 16.44mb)  time: O(n * k) | space: O(k)
    out: int = 0
    for sentence in sentences:
        out = max(out, len(sentence.split()))
    return out


# Time complexity: O(n * k) <- n - length of the input array `sentences`, k - average sentence length in `sentences`
# Essentially, we're just using every char in every `sentence` once => O(n * k).
# ----------------------
# Auxiliary space: O(k)
# `split` <- creates an array with all the words from `sentence` => O(k).


test: list[str] = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
test_out: int = 6
assert test_out == most_words_found(test)

test = ["please wait", "continue to fight", "continue to win"]
test_out = 3
assert test_out == most_words_found(test)
