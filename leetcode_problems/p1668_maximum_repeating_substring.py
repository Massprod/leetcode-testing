# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
# The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence.
# If word is not a substring of sequence, word's maximum k-repeating value is 0.
# Given strings sequence and word, return the maximum k-repeating value of word in sequence.
# -------------------------
# 1 <= sequence.length <= 100
# 1 <= word.length <= 100
# sequence and word contains only lowercase English letters.


def max_repeating(sequence: str, word: str) -> int:
    # working_sol (79.65%, 22.84%) -> (32ms, 16.55mb)  time: O(n * k) | space: O(n + n * k)
    out: int = 0
    cache: dict[int, int] = {}

    def check_sequence(start_index: int) -> int:
        nonlocal cache
        if start_index >= len(sequence):
            return 0
        if start_index in cache:
            return cache[start_index]
        seq: int = 0
        next_index: int = start_index + len(word)
        if sequence[start_index: next_index] == word:
            seq = 1 + check_sequence(next_index)
        cache[start_index] = seq
        return seq

    for index in range(len(sequence)):
        out = max(out, check_sequence(index))
    return out


# Time complexity: O(n * k) <- n - length of the input string `sequence`, k - length of the input string `word`.
# We always check every index, and are building a sequences from them.
# Because we're using `cache,` we always build from every index, once.
# Extra we're always creating a slices of the size `word` => O(n * k).
# -------------------------
# Auxiliary space: O(n + n * k)
# `cache` <- always holds every index of `sequence` => O(n).
# Extra creating a slices of `word` size, on every recursion call => O(n + n * k).


test: str = "ababc"
test_word: str = "ab"
test_out: int = 2
assert test_out == max_repeating(test, test_word)

test = "ababc"
test_word = "ba"
test_out = 1
assert test_out == max_repeating(test, test_word)

test = "ababc"
test_word = "ac"
test_out = 0
assert test_out == max_repeating(test, test_word)
