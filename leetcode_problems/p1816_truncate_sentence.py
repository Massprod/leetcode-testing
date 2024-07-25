# A sentence is a list of words that are separated
#  by a single space with no leading or trailing spaces.
# Each of the words consists of only uppercase and lowercase English letters (no punctuation).
#  - For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence `s` and an integer `k`.
# You want to truncate `s` such that it contains only the first `k` words.
# Return `s` after truncating it.
# -------------------
# 1 <= s.length <= 500
# k is in the range [1, the number of words in s].
# s consist of only lowercase and uppercase English letters and spaces.
# The words in s are separated by a single space.
# There are no leading or trailing spaces.


def truncate_sentence(s: str, k: int) -> str:
    # working_sol (99.92%, 27.85%) -> (18ms, 16.57mb)  time: O(s + k) | space: O(s)
    out: list[str] = s.split(' ')
    return ' '.join(out[:k])


# Time complexity: O(s + k)
# We always split whole input string `s` into pieces separated by ` ` => O(s).
# ! actually I could just take only `k` first words, but w.e !
# Extra slicing `k` elements from `out` of size `s` => O(s + k).
# -------------------
# Auxiliary space: O(s)
# Essentially, we're just copying every char from `s` to `out` => O(s).


test: str = "Hello how are you Contestant"
test_k: int = 4
test_out: str = "Hello how are you"
assert test_out == truncate_sentence(test, test_k)

test = "What is the solution to this problem"
test_k = 4
test_out = "What is the solution"
assert test_out == truncate_sentence(test, test_k)

test = "chopper is not a tanuki"
test_k = 5
test_out = "chopper is not a tanuki"
assert test_out == truncate_sentence(test, test_k)
