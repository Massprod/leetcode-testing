# Given a string array words, return the maximum value of length(word[i]) * length(word[j])
#  where the two words do not share common letters.
# If no such two words exist, return 0.
# -------------------------
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.
from random import choice
from string import ascii_lowercase


def max_product(words: list[str]) -> int:
    # working_sol (73.34%, 57.65%) -> (335ms, 19.76mb)  time: O((n * k) ** 2) | space: O(n + k)
    out: int = 0
    # [ (word_bit_mask, word_length) ]
    all_masks: list[tuple[int, int]] = []
    for index in range(len(words)):
        mask: int = 0
        word: str = words[index]
        for char in word:
            mask |= 1 << (ord(char) - 97)
        # We can have duplicated chars, so we need extra length of the `word`.
        all_masks.append((mask, len(word)))
    # Check every possible combination of words we can have.
    for index in range(len(all_masks)):
        for an_index in range(index, len(all_masks)):
            mask1: int = all_masks[index][0]
            mask2: int = all_masks[an_index][0]
            if mask1 & mask2:
                continue
            len_word1: int = all_masks[index][1]
            len_word2: int = all_masks[an_index][1]
            out = max(out, len_word1 * len_word2)
    return out


# Time complexity: O((n * k) ** 2) <- n - length of the input array `words`, k - average length of the word in `words`.
# Always traversing every word from `words` and building bit_mask for it == using every char => O(n * k).
# Extra traversing every mask == word in `words`, with inner loop for other masks,
#   and the first iteration of this loop will take O((n * k) ** 2) => O(n * k + (n * k) ** 2).
# -------------------------
# Auxiliary space: O(n + k)
# For every word in `words` we create a tuple with 2 INTs => O(n).
# Extra we use `word` to temporarily store used word => O(n + k).


test: list[str] = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
test_out: int = 16
assert test_out == max_product(test)

test = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
test_out = 4
assert test_out == max_product(test)

test = ["a", "aa", "aaa", "aaaa"]
test_out = 0
assert test_out == max_product(test)

test = ["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]
test_out = 15
assert test_out == max_product(test)

test = [''.join([choice(ascii_lowercase) for _ in range(1000)]) for _ in range(1000)]
print(test)
