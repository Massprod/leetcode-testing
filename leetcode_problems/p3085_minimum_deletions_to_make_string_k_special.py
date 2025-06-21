# You are given a string word and an integer k.
# We consider word to be k-special if |freq(word[i]) - freq(word[j])|
#  <= k for all indices i and j in the string.
# Here, freq(x) denotes the frequency of the character x in word,
#  and |y| denotes the absolute value of y.
# Return the minimum number of characters you need to delete to make word k-special.
# -------------------------
# 1 <= word.length <= 10 ** 5
# 0 <= k <= 10 ** 5
# word consists only of lowercase English letters.
from collections import Counter


def minimum_deletions(word: str, k: int) -> int:
    # working_sol (93.80%, 70.54%) -> (51ms, 18.07mb)  time: O(n + C ** 2) | space: O(C)
    # { char: frequency }
    count: dict[str, int] = Counter(word)
    out: int = len(word)
    for a_frequency in count.values():
        delete: int = 0
        for b_frequency in count.values():
            if a_frequency > b_frequency:
                delete += b_frequency
            elif b_frequency > a_frequency + k:
                delete += b_frequency - (a_frequency + k)
        out = min(out, delete)

    return out


# Time complexity: O(n + C ** 2) <- n - length of the input string `word`,
#                                   C - available characted => englAlph => 26.
# -------------------------
# Auxiliary space: O(C)
# `count` <- allocates space for each unique char from the `word` => O(C).


test: str = "aabcaba"
test_k: int = 0
test_out: int = 3
assert test_out == minimum_deletions(test, test_k)

test = "dabdcbdcdcd"
test_k = 2
test_out = 2
assert test_out == minimum_deletions(test, test_k)

test = "aaabaaa"
test_k = 2
test_out = 1
assert test_out == minimum_deletions(test, test_k)
