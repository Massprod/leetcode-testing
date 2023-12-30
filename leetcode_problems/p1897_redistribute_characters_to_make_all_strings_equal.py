# You are given an array of strings words (0-indexed).
# In one operation, pick two distinct indices i and j,
#  where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
# Return true if you can make every string in words equal using any number of operations,
#  and false otherwise.
# --------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
from collections import Counter


def make_equal(words: list[str]) -> bool:
    # working_sol (95.24%, 9.52%) -> (46ms, 17.5mb)  time: O(n * m) | space: O(n * m)
    # We can make them equal only if we can divide all characters equally.
    all_chars: dict[str, int] = Counter(''.join(words))
    for char in all_chars:
        if all_chars[char] % len(words):
            return False
    return True


# Time complexity: O(n * m) <- n - length of input array `words`, m - average length of strings inside `words`.
# Worst case: every word in `words` have unique symbols
# Traversing whole `words` to get all characters => O(n * m).
# Extra traversing all symbols to check if we can divide them equally => O(n * m).
# --------------------
# Auxiliary space: O(n * m).
# Because we store every character, with the same worst case we will just store (n * m) chars => O(n * m).


test: list[str] = ["abc", "aabc", "bc"]
test_out: bool = True
assert test_out == make_equal(test)

test = ["ab", "a"]
test_out = False
assert test_out == make_equal(test)
