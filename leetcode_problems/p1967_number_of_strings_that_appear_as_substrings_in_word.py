# Given an array of strings patterns and a string word,
#  return the number of strings in patterns that exist as a substring in word.
# A substring is a contiguous sequence of characters within a string.
# -----------------------
# 1 <= patterns.length <= 100
# 1 <= patterns[i].length <= 100
# 1 <= word.length <= 100
# patterns[i] and word consist of lowercase English letters.


def num_of_strings(patterns: list[str], word: str) -> int:
    # working_sol (86.91%, 52.13%) -> (34ms, 16.56mb)  time: O(n * k) | space: O(1)
    out: int = 0
    for pattern in patterns:
        # Or sliding window with `pattern`, but w.e
        if pattern in word:
            out += 1
    return out


# Time complexity: O(n * k) <- n - length of the input `word`, k - length of the input array `patterns`.
# In the worst case, every `pattern` == `word`.
# We will traverse every `pattern` => O(n * k).
# -----------------------
# Auxiliary space: O(1).


test: list[str] = ["a", "abc", "bc", "d"]
test_word: str = "abc"
test_out: int = 3
assert test_out == num_of_strings(test, test_word)

test = ["a", "b", "c"]
test_word = "aaaaabbbbb"
test_out = 2
assert test_out == num_of_strings(test, test_word)

test = ["a", "a", "a"]
test_word = "ab"
test_out = 3
assert test_out == num_of_strings(test, test_word)
