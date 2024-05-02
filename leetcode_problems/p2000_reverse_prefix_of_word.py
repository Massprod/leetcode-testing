# Given a 0-indexed string word and a character ch,
#  reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d",
#  then you should reverse the segment that starts at 0 and ends at 3 (inclusive).
# The resulting string will be "dcbaefd".
# Return the resulting string.
# ---------------------
# 1 <= word.length <= 250
# word consists of lowercase English letters.
# ch is a lowercase English letter.


def reverse_prefix(word: str, ch: str) -> str:
    # working_sol (54.03%, 93.22%) -> (35ms, 16.44mb)  time: O(n) | space: O(n)
    out: str = ''
    for index, char in enumerate(word):
        if ch == char:
            out = word[index::-1] + word[index + 1:]
            break
    return out if out else word


# Time complexity: O(n) <- n - length of input string `word`
# Worst case: we will need to traverse (n - 1) indexes to get our `ch`,
#  and then we need to reverse these (n - 1) indexes => O(2n).
# ---------------------
# Auxiliary space: O(n)
# Same worst case, we will create temp array with (n - 1) size and `out` will be a size of `n` anyway => O(2n).


test: str = "abcdefd"
test_ch: str = "d"
test_out: str = "dcbaefd"
assert test_out == reverse_prefix(test, test_ch)

test = "xyxzxe"
test_ch = "z"
test_out = "zxyxxe"
assert test_out == reverse_prefix(test, test_ch)

test = "abcd"
test_ch = "z"
test_out = "abcd"
assert test_out == reverse_prefix(test, test_ch)
