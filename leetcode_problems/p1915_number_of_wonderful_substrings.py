# A wonderful string is a string where at most one letter appears an odd number of times.
#  - For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters ('a' through 'j'),
#  return the number of wonderful non-empty substrings in word.
# If the same substring appears multiple times in word, then count each occurrence separately.
# A substring is a contiguous sequence of characters in a string.
# ------------------------
# 1 <= word.length <= 10 ** 5
# word consists of lowercase English letters from 'a' to 'j'.


def wonderful_substrings(word: str) -> int:
    # working_sol (65.39%, 96.15%) -> (1329ms, 17.34mb)  time: O(n) | space: O(n)
    frequency: dict[int, int] = {0: 1}
    mask: int = 0
    out: int = 0
    uniques: set[str] = set(word)
    for char in word:
        mask ^= (1 << (ord(char) - 97))
        if mask in frequency:
            out += frequency[mask]
            frequency[mask] += 1
        else:
            frequency[mask] = 1
        for val in uniques:
            odds: int = ord(val) - 97
            if (mask ^ (1 << odds)) in frequency:
                out += frequency[mask ^ (1 << odds)]
    return out


# Time complexity: O(n) <- n - length of input string `word`
# For every `char` in `word` we create mask and iterate through all placement options == 10 at max => O(n * 10).
# ------------------------
# Auxiliary space: O(n)
# We can have `word` with only unique symbols, so all of them will be stored in `frequency` => O(n)


test: str = "aba"
test_out: int = 4
assert test_out == wonderful_substrings(test)

test = "aabb"
test_out = 9
assert test_out == wonderful_substrings(test)

test = "he"
test_out = 2
assert test_out == wonderful_substrings(test)
