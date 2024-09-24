# You are given a 0-indexed array words consisting of distinct strings.
# The string words[i] can be paired with the string words[j] if:
#  - The string words[i] is equal to the reversed string of words[j].
#  - 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.
# Note that each string can belong in at most one pair.
# ------------------------
# 1 <= words.length <= 50
# words[i].length == 2
# words consists of distinct strings.
# words[i] contains only lowercase English letters.
from collections import Counter


def maximum_number_of_string_pairs(words: list[str]) -> int:
    # working_sol (74.68%, 67.39%) -> (46ms, 16.50mb)  time: O(n * k) | space: O(n * k)
    out: int = 0
    # { word: occurrences }
    fast_words: dict[str, int] = Counter(words)
    for word in words:
        rever_word: str = word[::-1]
        if rever_word in fast_words:
            if word == rever_word:
                if 1 < fast_words[rever_word]:
                    out += 1
                    fast_words[rever_word] -= 2
            elif 1 <= fast_words[rever_word]:
                fast_words[rever_word] -= 1
                fast_words[word] -= 1
                out += 1
    return out


# Time complexity: O(n * k) <- n - length of the input array `words`, k - avg length of strings inside `words`.
# Always traversing every word in `words` to store in `fast_words` => O(n * k).
# Extra traversing every word with reversing it => O(n * k * 3).
# ------------------------
# Auxiliary space: O(n * k)
# `fast_words` <- always contains all strings from `words`, because we guaranteed to have them unique => O(n * k).
# `rever_word` <- string with the avg size == `k` => O(n * k + k).


test: list[str] = ["cd", "ac", "dc", "ca", "zz"]
test_out: int = 2
assert test_out == maximum_number_of_string_pairs(test)

test = ["ab", "ba", "cc"]
test_out = 1
assert test_out == maximum_number_of_string_pairs(test)

test = ["aa", "ab"]
test_out = 0
assert test_out == maximum_number_of_string_pairs(test)
