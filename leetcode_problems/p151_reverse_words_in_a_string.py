# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.
# -------------------
# 1 <= s.length <= 10 ** 4
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
# -------------------
# Follow-up: If the string data type is mutable in your language,
# can you solve it in-place with O(1) extra space?


def reverse_words_rebuild(s: str) -> str:
    # working_sol (74.89%, 84.85%) -> (42ms, 16.3mb)  time: O(n) | space: O(n)
    # Combine of all reverse words.
    new_words: str = ''
    # Words one by one.
    new_word: str = ''
    index: int = len(s) - 1
    while index >= 0:
        # Spaces added as extra and sliced after,
        # so they can be ignored 24/7.
        if s[index] == ' ':
            index -= 1
            continue
        # Only correct words without spaces is needed.
        while index >= 0 and s[index] != ' ':
            new_word += s[index]
            index -= 1
        # Reverse and add correct words, with extra space ->
        new_words += new_word[::-1] + ' '
        new_word = ''
    # -> slice extra space on last word.
    return new_words[:-1]


# Time complexity: O(n) -> traversing once through whole input_string => O(n) -> reversing every word, and in the
# n - len of input_string^^| worst case without empty spaces we will reverse actual input_string => O(2n) ->
#                            -> extra slicing should be O(n) as well, so it's somewhat O(3n) => O(n) drop const anyway.
# Space complexity: O(n) -> new_words with size of n, and new_word is always empty when we increment new_words => O(n).
# -------------------
# Basic rebuilding with O(2n) space is easy, so it's better to try O(1).
# ! Strings are not mutable in Python. ! <- Sadly, we can't.


test: str = "the sky is blue"
test_out: str = "blue is sky the"
assert test_out == reverse_words_rebuild(test)

test = "  hello world  "
test_out = "world hello"
assert test_out == reverse_words_rebuild(test)

test = "a good   example"
test_out = "example good a"
assert test_out == reverse_words_rebuild(test)
