# You are given a 0-indexed array of strings words and a character x.
# Return an array of indices representing the words that contain the character x.
# Note that the returned array may be in any order.
# ----------------------
# 1 <= words.length <= 50
# 1 <= words[i].length <= 50
# x is a lowercase English letter.
# words[i] consists only of lowercase English letters.


def find_words_containing(words: list[str], x: str) -> list[int]:
    # working_sol (45.66%, 98.76%) -> (62ms, 16.40mb)  time: O(n * k) | space: O(n)
    out: list[int] = []
    for index, word in enumerate(words):
        if x in word:
            out.append(index)
    return out


# Time complexity: O(n * k) <- n - length of the input array `words`, k - average length of the word in `words`.
# Always traversing every char of word in `words` => O(n * k).
# ----------------------
# Auxiliary space: O(n)
# `out` <- will hold all the indexes of `words`, every word contains `x` => O(n).


test: list[str] = ["leet", "code"]
test_x: str = "e"
test_out: list[int] = [0, 1]
assert test_out == find_words_containing(test, test_x)

test = ["abc", "bcd", "aaaa", "cbc"]
test_x = "a"
test_out = [0, 2]
assert test_out == find_words_containing(test, test_x)

test = ["abc", "bcd", "aaaa", "cbc"]
test_x = "z"
test_out = []
assert test_out == find_words_containing(test, test_x)
