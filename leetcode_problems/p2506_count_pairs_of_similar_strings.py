# You are given a 0-indexed string array words.
# Two strings are similar if they consist of the same characters.
#  - For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
#  - However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1
#  and the two strings words[i] and words[j] are similar.
# ----------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consist of only lowercase English letters.


def similar_pairs(words: list[str]) -> int:
    # working_sol (73.12%, 97.38%) -> (62ms, 16.45mb)  time: O(n * (k * log k)) | space: O(n * k)
    all_options: dict[tuple, int] = {}
    for word in words:
        # Or we can use `int` and store bits.
        # But not remaking it.
        option: tuple = tuple(sorted(set(word)))
        if option in all_options:
            all_options[option] += 1
            continue
        all_options[option] = 1
    out: int = 0
    for value in all_options.values():
        out += (value * (value - 1)) // 2
    return out


# Time complexity: O(n * (k * log k)) <- n - length of the input array `words`,
#                                        k - average length of the word in `words`.
# For every word in `words` we will traverse all chars to get `set(word)` => O(k).
# Extra sort it O(k + k * log k).
# And we repeat for each word => O(n * (k + k * log k).
# Extra traversing every word, if every word had unique chars => O(n + n * (k + k * log k)).
# ----------------------
# Auxiliary space: O(n * k)
# In the worst case, every word is going to have unique chars.
# `all_options` <- will allocate space for every unique chars in word => O(n * k).


test: list[str] = ["aba", "aabb", "abcd", "bac", "aabc"]
test_out: int = 2
assert test_out == similar_pairs(test)

test = ["aabb", "ab", "ba"]
test_out = 3
assert test_out == similar_pairs(test)

test = ["nba", "cba", "dba"]
test_out = 0
assert test_out == similar_pairs(test)
